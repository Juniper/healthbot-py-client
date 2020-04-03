import requests
from requests.models import Response
import logging

import re
import os
import time

from jnpr.healthbot.urlfor import UrlFor
from jnpr.healthbot.modules import devices
from jnpr.healthbot.modules import rules
from jnpr.healthbot.modules import playbooks
from jnpr.healthbot.modules import database
from jnpr.healthbot.modules import settings
from jnpr.healthbot.modules import profiles
from jnpr.healthbot.modules import administration

from jnpr.healthbot.swagger.api.authentication_api import AuthenticationApi
from jnpr.healthbot.swagger.api_client import ApiClient
from jnpr.healthbot.swagger.configuration import Configuration
from jnpr.healthbot.swagger.models.health_schema import HealthSchema
from jnpr.healthbot.swagger.models.refresh_token import RefreshToken
from jnpr.healthbot.swagger.models.token import Token

from jnpr.healthbot.swagger.rest import ApiException
from pathlib import Path

import jwt

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


logger = logging.getLogger(__file__)


class HealthBotClient(object):

    apiopt_candidate = "/?working=true"

    def __init__(
            self,
            server: str,
            user: str,
            password: str,
            *args, **kwargs):
        """
        An instance of this class represents the HealthBot Service

        :param str server: HealthBot Server IP Address
        :param str user: HealthBot Server (not the Linux user) UserName
        :param str password: HealthBot Server (not the Linux user) password
        :param int port: *OPTIONAL* HealthBot Server port (defaults to 8080)

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from pprint import pprint

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx', port=8000) as hb:

                # Get list of all existing devices
                print(hb.device.get_ids())

                # Get config details of a given device id
                pprint(hb.device.get('core-01'))

                # Get config details of all the device
                pprint(hb.device.get())

                # Get device facts of a given device id
                pprint(hb.device.get_facts('avro'))

                # Get device facts for all the devices in HB
                pprint(hb.device.get_facts())

                # Add a device
                from jnpr.healthbot import DeviceSchema
                ds = DeviceSchema(device_id='xyz', host='xx.xxx.xxx.xxx',
                      authentication={"password": {"password": "xxxxx", "username": "xxxxx"}})

                # we can also later assign values like this
                ds.description = "HbEZ testing"

                # This will add device in candidate DB
                hb.device.add(schema=ds)

                # Add device group
                print(hb.device_group.add(device_group_name="edge",
                description="All devices on the edge", devices=['demo']))

                # commit changes to master DB
                hb.commit()

                # get details of a given topic/rule
                pprint(hb.rule.get('linecard.ospf', 'check-ddos-statistics'))

        """
        self.server = server
        self.user = user
        self.password = password

        self.port = kwargs.get('port', 8080)

        self.url = "https://" + server + ":" + str(self.port) + "/api/" + self.api_version

        if server is None or server is "":
            raise ValueError("You must provide 'server' of HealthBot")

        if user is None or user is "":
            raise ValueError("You must provide 'user' of HealthBot")

        if password is None or password is "":
            raise ValueError("You must provide 'password' of HealthBot")

        self._hbot_session = None
        self._user_token = None
        self.api_client = None
        self._auth = None
        self.connected = False
        self._token_expire_time = None

    def open(self):
        """
        Open session with HealthBot server. First sets user token (for healthbot
        3.0.0 and above) and check a top level URL for confirmation of API to be
        working.

        """
        self.set_user_token()
        try:
            req = self.hbot_session.get(self.url + '/')
            self.connected = True
            # HTTP errors are not raised by default, this statement does that
            req.raise_for_status()
        except Exception as ex:
            logger.error("Error: {}".format(ex))
            raise ex
        else:
            logger.debug(
                "Connected to HealthBot Server({}) on port {}".format(
                    self.server, self.port))
        self.urlfor = UrlFor(self)
        self.device = devices.Device(self)
        self.device_group = devices.DeviceGroup(self)
        self.network_group = devices.NetworkGroup(self)
        self.rule = rules.Rule(self)
        self.topic = rules.Topic(self)
        self.playbook = playbooks.Playbook(self)
        self.settings = settings.Settings(self)
        self.profile = profiles.Profile(self)
        self.administration = administration.Administration(self)
        return True

    login = open

    @property
    def hbot_session(self):
        """
        Property provides requests module session object. Also help in updating
        Access token key when expires. Any call to hbot_session.apis should go
        through this property to keep a check on token key expiry.

        """
        if self._hbot_session is None:
            self._hbot_session = requests.Session()
            self._hbot_session.headers.update(
                {"Accept": "application/json", "Content-Type": "application/json"}
            )
            self._hbot_session.verify = False
        # this call should make sure to check for token expiry
        self.user_token
        return self._hbot_session

    @property
    def user_token(self):
        if self._token_expire_time and time.time() >= self._token_expire_time:
            logger.debug("Token expired, hence refreshing")
            self._user_token = self._auth.refresh_token(token=Token(
                refresh_token=self._user_token.refresh_token))
            self._hbot_session.headers.update({
                'Authorization': 'Bearer ' + self._user_token.access_token})
            self._token_expire_time = self._get_token_expire()
        return self._user_token

    def set_user_token(self):
        """
        From HealthBot 3.0.0 APIs will be token based. This function helps in
        setting user based token. This token will be used in header of any
        REST API calls.

        """
        conf = Configuration()
        conf.host = self.url
        conf.verify_ssl = False
        self.api_client = ApiClient(configuration=conf)
        self._auth = AuthenticationApi(api_client=self.api_client)
        try:
            self._user_token = self._auth.user_login(
                credential={"userName": self.user, "password": self.password})
            self._token_expire_time = self._get_token_expire()
            self.hbot_session.headers.update({
                'Authorization': 'Bearer ' + self._user_token.access_token})
            self.connected = True
        except ApiException as ex:
            logger.debug("Check if given HealthBot version support authorization key")
            # set user/password used by older healthbot version APIs
            self.hbot_session.auth = (self.user, self.password)
        except Exception as ex:
            logger.error("User Login Error: {}".format(ex))
            raise ex

    def _get_token_expire(self):
        """
        USing PyJWT module, decode exisiing access token to figure our token
        expiry time (in seconds).

        """
        obj = jwt.decode(self._user_token.access_token, 'secret', verify=False)
        timeout = obj.get('exp', 0) - obj.get('iat')
        logger.debug("Access authorization key expiration timeout: {}".format(
            timeout))
        return time.time() + timeout

    def logout(self):
        """
        Call user logout function to discard access tokens.

        """
        if self._user_token:
            refresh_token = RefreshToken(token=self._user_token.refresh_token)
            self._auth.user_logout(refresh_token=refresh_token)

    @property
    def tsdb(self):
        """
        Connection to the tsdb

        :return: InfluxDBClient
        """
        return database.Database(self)

    @tsdb.setter
    def tsdb(self, value):
        """ read-only property """
        raise RuntimeError("tsdb is read-only!")

    @property
    def api_version(self):
        """ placeholder for rest API version check

        :returns:
            str: API server version.
        """

        return 'v1'

    @property
    def version(self):
        """ TO get the version of Healthbot Server

        :returns:
            str: API server version.
        """
        system_details_url = self.urlfor.system_details()
        resp = self.api.get(system_details_url)
        if resp.status_code == 200:
            hb_version = resp.json().get('version', '')
            obj = re.search(r'HealthBot (\d\.\d\.\d)', hb_version)
            if obj:
                return obj.group(1)
        # older version of Healtbot, so return default supported version
        return '2.0.1'

    @property
    def api(self):
        return self.hbot_session

    def commit(self):
        """
        Commit any candidate configuration

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import DeviceSchema

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                ds = DeviceSchema(device_id='xyz', host='xx.xxx.xxx.xxx',
                      authentication={"password": {"password": "xxxxx", "username": "xxxxx"}})

                # we can also later assign values like this
                ds.description = "HbEZ testing"

                # This will add device in candidate DB
                hb.device.add(schema=ds)

                # commit changes to master DB
                hb.commit()

        :raises: Any requests exception

        :returns: True when OK
        """
        response = self.hbot_session.post(
            "{api}/configuration".format(api=self.url))
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return response.ok

    def rollback(self):
        """
        Rollback any candidate configuration

        Example:
        ::

            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                # This will delete device in candidate DB
                hb.device.delete('xyz')

                # rollback candidate configuration
                hb.rollback()

        :raises: Any requests exception

        :returns: True when OK
        """
        response = self.hbot_session.delete(
            "{api}/configuration".format(api=self.url))
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return response.ok

    def upload_helper_file(self, filename):
        """
        Upload a "helper-file" to the server.  A helper-file, cab be
         YAML/.py/.rule/.playbook file.

        :param str filename: The name of the file to be uploaded.
        """

        # when using the 'files' option to POST, we must remove the content-type from the
        # headers since the requests library uses/fills this in according to
        # the file

        c_type = self.hbot_session.headers.pop('Content-Type')
        try:
            file_p = Path(os.path.abspath(filename))
            # upload rule/playbook file
            if filename.endswith('.rule'):
                url = self.urlfor.topics()
                files = {'topics': file_p.open('rb')}
            elif filename.endswith('.playbook'):
                url = self.urlfor.playbooks()
                files = {'playbooks': file_p.open('rb')}
            else:
                url = self.urlfor.helper_files(name=file_p.name)
                files = {'up_file': file_p.open('rb')}
            response = self.hbot_session.post(url=url, files=files)

            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
        finally:
            self.hbot_session.headers['Content-Type'] = c_type
        return True

    def _create_schema(self, response: requests.models.Response, schema):
        attribute_map = schema.attribute_map
        if not isinstance(response, dict):
            attributes = dict()
            if isinstance(response, Response):
                response = response.json()
                attribute_map_values = attribute_map.values()
                attribute_map_reversed = {v: k for k, v in attribute_map.items()}
                for key, value in response.items():
                    if key in attribute_map_values:
                        attributes[attribute_map_reversed[key]] = response.get(key)
            else:
                response = response.to_dict()
                for key, value in response.items():
                    if key in attribute_map:
                        attributes[key] = response.get(key)
            return schema(**attributes)

    def _create_payload(self, schemaObj):
        """
        remove keys which got None as value

        :param payload: dict which needs clean up of None values
        :return: dict of payload without None values
        """
        payload = schemaObj.to_dict()
        # remove None values
        attribute_map = schemaObj.attribute_map
        attributes = dict()
        for key, value in payload.items():
            if value is not None:
                if key in attribute_map:
                    if isinstance(value, dict):
                        childSchema = getattr(schemaObj, key)
                        if isinstance(childSchema, dict):
                            # childSchema is not any schema, hence set it to
                            # payload
                            attributes[attribute_map[key]] = payload.get(key)
                        else:
                            attributes[attribute_map[key]
                                       ] = self._create_payload(childSchema)
                    elif isinstance(value, list) and filter(
                            lambda i: isinstance(i, dict), value):
                        childSchemas = getattr(schemaObj, key)
                        attributes[attribute_map[key]] = []
                        for childSchema in childSchemas:
                            attributes[attribute_map[key]].append(
                                self._create_payload(childSchema))
                    else:
                        attributes[attribute_map[key]] = payload.get(key)
        return attributes

    def health(self):
        """
        Returns health of network-groups and devices in device-groups
        `HealthSchema <jnpr.healthbot.swagger.models.html#healthschema>`_

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                print(hb.health())

        :return: `HealthSchema <jnpr.healthbot.swagger.models.html#healthschema>`_
        """

        health_url = self.urlfor.health()
        resp = self.api.get(health_url)

        if resp.status_code == 404:
            return {}
        return self._create_schema(resp, HealthSchema)

    def close(self):
        self.hbot_session.close()
        self.connected = False

    def __repr__(self):
        return "HealthBot(%s)" % self.server
    # -----------------------------------------------------------------------
    # Context Manager
    # -----------------------------------------------------------------------

    def __enter__(self):
        self.login()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logout()
        self.connected = False

    def __repr__(self):
        return "HealthBot(%s)" % self.server
