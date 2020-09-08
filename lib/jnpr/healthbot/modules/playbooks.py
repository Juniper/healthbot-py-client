import time
import copy

from jnpr.healthbot.swagger.models.playbook_schema import PlaybookSchema
from jnpr.healthbot.swagger.models.rule_schema_variable import RuleSchemaVariable
from jnpr.healthbot.modules import BaseModule
from jnpr.healthbot.modules.rules import Rule
from jnpr.healthbot.modules.devices import Device, DeviceGroup

from jnpr.healthbot.exception import SchemaError, NotFoundError

import logging
logger = logging.getLogger(__file__)


class Playbook(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """

        super().__init__(hbot)

    def add(self, schema: PlaybookSchema = None, **kwargs):
        """
        Add playbook

        :param object schema: `PlaybookSchema <jnpr.healthbot.swagger.models.html#playbookschema>`_
        :param object kwargs: key values, which can be used to create
            PlaybookSchema
            Check `PlaybookSchema <jnpr.healthbot.swagger.models.html#playbookschema>`_
            for details about which all keys can be used

        Example:
        ::
            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                hb.playbook.add(playbook_name="HbEZ-example",
                        rules = ['protocol.infra/check-task-momory-usage'])

            # or
            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import PlaybookSchema

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                pbs = PlaybookSchema(playbook_name="HbEZ-example",
                        rules = ['protocol.infra/check-task-momory-usage'])
                hb.playbook.add(pbs)

        Returns:
            True if action successful
        """
        if schema is None:
            schema = PlaybookSchema(**kwargs)

        payload = self.hbot._create_payload(schema)

        payload_url = self.hbot.urlfor.playbook(payload['playbook-name'])
        resp = self.api.get(payload_url + self.hbot.apiopt_candidate)
        if resp.ok:
            return True
        response = self.api.post(payload_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()

        return True

    def delete(self, playbook_name: str):
        """
        Delete playbook

        :param str playbook_name: The playbook name to deleted

        Example:
        ::
            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                hb.playbook.delete('linecard-kpis-playbook')

        """

        payload = {'playbook-name': playbook_name}
        rule_url = self.hbot.urlfor.playbook(playbook_name)
        response = self.api.delete(rule_url, json=payload)
        if response.status_code != 204:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def get(self, playbook_name: str = None, uncommitted: bool = True):
        """
        get playbook details

        :param str playbook_name: Name of the playbook
        :param bool uncommitted: True includes fetches uncommitted changes,
                False restricts data set to only committed changes

        Example:
        ::
            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                print(hb.playbook.get('linecard-kpis-playbook'))

                # for all
                print(hb.playbook.get())

        """
        if playbook_name is not None:
            playbook_url = self.hbot.urlfor.playbook(playbook_name)
            if uncommitted:
                playbook_url += self.hbot.apiopt_candidate
            response = self.api.get(playbook_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(response, PlaybookSchema)
        else:
            playbook_list = []

            playbooks_list_url = self.hbot.urlfor.playbooks()
            if uncommitted:
                playbooks_list_url += self.hbot.apiopt_candidate
            resp = self.api.get(playbooks_list_url)

            if resp.status_code == 404:
                return False

            existing_playbooks = resp.json()['playbook']
            for playbook in existing_playbooks:
                obj = self.hbot._create_schema(playbook, PlaybookSchema)
                playbook_list.append(obj)

            return playbook_list

    def update(self, schema: PlaybookSchema = None, **kwargs):
        """
        Update `PlaybookSchema <jnpr.healthbot.swagger.models.html#playbookschema>`_ for
        given playbook schema

        Passing Schema invoke `put` and kwargs `post`

        :param obj schema: `PlaybookSchema <jnpr.healthbot.swagger.models.html#playbookschema>`_
        :param object kwargs: key values, which can be used to create
            PlaybookSchema
            Check `PlaybookSchema <jnpr.healthbot.swagger.models.html#playbookschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schemaObj = hb.playbook.get('xyz')
                schemaObj.description = 'changed description'
                hb.playbook.update(schemaObj)

        :returns: True when OK
        """
        if schema is None:
            schema = PlaybookSchema(**kwargs)
            call = self.api.post
        else:
            if not isinstance(schema, PlaybookSchema):
                raise SchemaError(PlaybookSchema)
            call = self.api.put
        payload = self.hbot._create_payload(schema)
        name = schema.playbook_name
        playbook_url = self.hbot.urlfor.playbook(name)
        response = call(playbook_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def upload_playbook_file(self, filename):
        """

        :param filename: File to be loaded
        :return: return True of OK
        """
        return self.hbot.upload_helper_file(filename)


class _RuleVariableClass(object):

    def __init__(self, values):
        super(_RuleVariableClass, self).__setattr__('_values', values)
        super(_RuleVariableClass, self).__setattr__('_variable_value', [])
        for item in values:
            name = item['name'].replace('-', '_')
            self.__dict__[name] = RuleSchemaVariable(**item).value
            self.__dict__['_{}_schema'.format(
                name)] = RuleSchemaVariable(**item)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            # To make sure value is as per rule/type defined
            self.__dict__['_{}_schema'.format(key)].value = value
            # value should be of string type in DeviceGroupVariableSchema
            self._variable_value.append({'name': key.replace('_', '-'),
                                         'value': str(value)})

    def __repr__(self):
        return str(self._values)


class PlayBookInstanceBuilder(Playbook):
    def __init__(self, hbot, playbook: str, instance: str = None,
                 device_group_name: str = None):
        """
        Help in building and applying playbook instance

        :param hbot: HealthBOtClient instance
        :param playbook: Playbook name for which instance need to be created
        :param instance: Playbook instance name
        :param device_group_name: Device group which will be associated with instance

        Example:
        ::
            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:

                from jnpr.healthbot import PlayBookInstanceBuilder
                pbb = PlayBookInstanceBuilder(hb, 'forwarding-table-summary', 'HbEZ-instance', 'Core')

                variable = pbb.rule_variables["protocol.routesummary/check-fib-summary"]
                variable.route_address_family = 'pqr'
                variable.route_count_threshold = 100

                # Apply variable to given device(s)
                pbb.apply(device_ids=['vmx'])

                #clear all the variable if you want to set it something else for group or other device(s)
                pbb.clear()

                variable = pbb.rule_variables["protocol.routesummary/check-fib-summary"]
                variable.route_address_family = 'abc'
                variable.route_count_threshold = 200

                pbb.apply()

                hb.commit()
        """
        Playbook.__init__(self, hbot)
        self.hbot = hbot
        self.playbook = playbook
        self.instance_id = instance
        self.device_group_name = device_group_name
        self._rule_variables = dict()
        self._rule_variables = self.rule_variables

    def apply(self, device_ids: list = None, commit: bool = False):
        """
        Apply the playbook instance

        :param device_ids: if the rule variables need to be associated for
            given device id(s). Default to device group
        :param commit: Pass true if need to commit the changes

        Example:
        ::

            from jnpr.healthbot import PlayBookInstanceBuilder
            pbb = PlayBookInstanceBuilder(hb, 'forwarding-table-summary', 'HbEZ-instance', 'Core')
            pbb.apply()

        :return: True if all OK
        """
        if self.device_group_name is None:
            raise RuntimeError("PlayBookInstanceBuilder object device group attribute not provided")
        device_instance = Device(self.hbot)
        device_group_instance = DeviceGroup(self.hbot)
        device_group = device_group_instance.get(self.device_group_name)
        if device_group is None:
            raise NotFoundError({'detail': 'No details for device group: {}'.format(
                self.device_group_name), 'status': 404})
        if device_ids is not None:
            for device_id in device_ids:
                if device_id not in device_group.devices:
                    raise RuntimeError("Given device id '{}' is not present".
                                       format(device_id))
                device = device_instance.get(device_id)
                device.variable = self.device_variable
                if not device_instance.update(device):
                    logger.error(
                        "Not able to update '{}' device id".format(device_id))
            device_group_variable = []

            for item in self.device_variable:
                tmp = copy.copy(item)
                tmp.pop('variable-value', None)
                device_group_variable.append(tmp)
            existing_variable = device_group.variable
            if existing_variable is None:
                device_group.variable = device_group_variable
            else:
                existing_variable.extend(device_group_variable)
                device_group.variable = existing_variable
            if not device_group_instance.update(device_group):
                logger.error(
                    "Not able to update '{}' device group".format(device_group))
                return False
        else:
            existing_variable = device_group.variable
            if existing_variable is None:
                device_group.variable = self.device_variable
            else:
                existing_variable.extend(self.device_variable)
                device_group.variable = existing_variable
            existing_playbooks = device_group.playbooks or []
            existing_playbooks.append(self.playbook)
            device_group.playbooks = existing_playbooks
            if not device_group_instance.update(device_group):
                logger.error(
                    "Not able to update '{}' device group".format(device_group))
                return False
        if commit:
            self.hbot.commit()
            return True
        return True

    def clear(self):
        """
        Clear the old set values to rule variables
        :return: None
        """
        self._rule_variables = dict()
        self._rule_variables = self.rule_variables

    def delete(self):
        """
        Delete playbook instance

        Example:
        ::

            from jnpr.healthbot import PlayBookInstanceBuilder
            pbb = PlayBookInstanceBuilder(hb, 'forwarding-table-summary', 'HbEZ-instance', 'Core')
            pbb.delete()

        :return: True if success
        """
        delete_playbook_from_group = True
        if self.device_group_name is None:
            raise RuntimeError("PlayBookInstanceBuilder object device group attribute not provided")
        device_instance = Device(self.hbot)
        device_group_instance = DeviceGroup(self.hbot)
        device_group = device_group_instance.get(self.device_group_name)
        if device_group is None:
            raise NotFoundError({'detail': 'No details for device group: {}'.format(
                self.device_group_name), 'status': 404})
        for device_id in device_group.devices:
            device = device_instance.get(device_id)
            existing_variables = device.variable or []
            if len(existing_variables) > 0:
                changed = False
                for variable in existing_variables:
                    if self.playbook == variable.get('playbook'):
                        if self.instance_id == variable.get('instance-id'):
                            device.variable.remove(variable)
                            changed = True
                        else:
                            delete_playbook_from_group = False
                if changed and not device_instance.update(device):
                    logger.error(
                        "Not able to update '{}' device id".format(device_id))
                    return False

        existing_variables = copy.copy(device_group.variable) or []
        changed = False
        if len(existing_variables) > 0:
            for variable in existing_variables:
                if self.playbook == variable.get('playbook'):
                    if self.instance_id == variable.get('instance-id'):
                        device_group.variable.remove(variable)
                        changed = True
                    else:
                        delete_playbook_from_group = False
            if changed and not device_group_instance.update(device_group):
                logger.error(
                    "Not able to update '{}' device id".format(device_id))
                return False
        if not changed:
            logger.error(
                "Does not exist '{}' instance-id".format(self.instance_id))
            return False
        if delete_playbook_from_group:
            update_playbooks = device_group.playbooks or []
            if self.playbook in update_playbooks:
                update_playbooks.remove(self.playbook)
                device_group.playbook = update_playbooks
                if not device_group_instance.update(device_group):
                    logger.error(
                        "Not able to update '{}' device group".format(device_group))
                    return False
        return True

    @property
    def playbook_schema(self):
        return self._get_playbook_schema()

    @playbook_schema.setter
    def playbook_schema(self, value):
        """ read-only property """
        raise RuntimeError("playbook_schema is read-only!")

    @property
    def rules(self):
        return self.playbook_schema.to_dict().get('rules', [])

    @rules.setter
    def rules(self, value):
        """ read-only property """
        raise RuntimeError("rules is read-only!")

    @property
    def rule_variables(self):
        for i in self.rules:
            if i not in self._rule_variables:
                variable = Rule(self.hbot).get(*i.split('/')).variable
                if variable is not None:
                    self._rule_variables[i] = _RuleVariableClass(variable)
                else:
                    self._rule_variables[i] = None
        return self._rule_variables

    @rule_variables.setter
    def rule_variables(self, value):
        """ read-only property """
        raise RuntimeError("rules_variables is read-only!")

    @property
    def device_variable(self):
        variable = []
        for key, val in self._rule_variables.items():
            tmp = dict()
            tmp['@'] = {'changed-seconds': int(time.time())}
            tmp['instance-id'] = self.instance_id
            tmp['rule'] = key
            tmp['playbook'] = self.playbook
            variable_value = val._variable_value if val is not None else []
            tmp['variable-value'] = variable_value
            variable.append(tmp)
        return variable

    def _get_playbook_schema(self):
        """
        Get PlaybookSchema for given playbook name

        :return: PlaybookSchema `PlaybookSchema <jnpr.healthbot.swagger.models.html#playbookschema>`_
        """
        # get playbook schema first
        try:
            logger.debug("Getting details of playbook '{}'".format(
                self.playbook))
            return self.get(self.playbook)
        except Exception as ex:
            logger.error("Got exception '{}' while getting details of "
                         "playbook '{}'".format(ex, self.playbook_name))
            raise ex
