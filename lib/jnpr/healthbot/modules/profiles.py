from jnpr.healthbot.swagger.models.ca_profile_schema import CaProfileSchema
from jnpr.healthbot.swagger.models.local_certificate_schema import LocalCertificateSchema
from jnpr.healthbot.swagger.models.ssh_key_profile_schema import SshKeyProfileSchema
from jnpr.healthbot.exception import SchemaError, NotFoundError

from jnpr.healthbot.modules import BaseModule

import logging
logger = logging.getLogger(__file__)


class Profile(object):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """

        self._hbot = hbot
        self.data_summarization = DataSummarization(hbot)
        self.security = Security(hbot)


class Security(object):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """

        self._hbot = hbot
        self.ca_profile = CaProfile(hbot)
        self.local_certificate = LocalCertificate(hbot)
        self.ssh_key_profile = SshKeyProfile(hbot)


class CaProfile(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def get(self, name: str = None, uncommitted: bool = True):
        """
        Get `CaProfileSchema(s) <jnpr.healthbot.swagger.models.html#caprofileschema>`_ for
        given ca profile name or list for all

        :param name: ID of name
        :param bool uncommitted: True includes fetches uncommitted changes,
            False restricts data set to only committed changes

        Example:
            ::
                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.settings.security.ca_profile.get('xyz')

                    # for all
                    print(hb.settings.security.ca_profile.get()

        :return: `CaProfileSchema(s) <jnpr.healthbot.swagger.models.html#caprofileschema>`_
        """
        if name is not None:
            ca_profile_url = self.hbot.urlfor.ca_profile(name)
            if uncommitted:
                ca_profile_url += self.hbot.apiopt_candidate
            response = self.api.get(ca_profile_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(
                response, CaProfileSchema)
        else:
            ca_profiles_url = self.hbot.urlfor.ca_profiles()
            if uncommitted:
                ca_profiles_url += self.hbot.apiopt_candidate
            response = self.api.get(ca_profiles_url)
            response_json = response.json()
            if response.status_code != 200:
                logger.error(response.text)
                raise NotFoundError(response_json)
            existing_ca_profiles = response_json['ca-profile']
            ca_profiles_list = []
            for ca_profile in existing_ca_profiles:
                obj = self.hbot._create_schema(ca_profile, CaProfileSchema)
                ca_profiles_list.append(obj)

            return ca_profiles_list

    def add(self, schema: CaProfileSchema = None, **kwargs):
        """
        Add ca profile to HealthBot.
        The onus of uploading helper file certificate_authority_crt is on user.
        They should use hb.upload_helper_file API to make sure these crt file
        are uploaded in system.
        We don't do that validation as user can also upload these file after
        configuring profiles.

        :param object schema: `CaProfileSchema <jnpr.healthbot.swagger.models.html#caprofileschema>`_
        :param object kwargs: key values, which can be used to create
            CaProfileSchema
            Check `CaProfileSchema <jnpr.healthbot.swagger.models.html#caprofileschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import CaProfileSchema

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                ca_prof_schema = CaProfileSchema(certificate_authority_crt='abc.crt', name='hbez')
                hb.settings.security.ca_profile.add(ca_prof_schema)

        :returns: True when OK

        """
        if schema is None:
            schema = CaProfileSchema(**kwargs)
        payload = self.hbot._create_payload(schema)
        ca_profile_url = self.hbot.urlfor.ca_profile(payload['name'])
        response = self.api.post(ca_profile_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def delete(self, name: str):
        """
        Remove ca profile from security settings

        :param str name: The name of the ca_profile to be deleted

        Example:
        ::
            hb.settings.security.ca_profile.delete('xyz')
            hb.commit()

        :returns: True when OK
        """

        ca_profile_url = self.hbot.urlfor.ca_profile(name)
        response = self.api.delete(ca_profile_url)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()

        return True

    def update(self, schema: CaProfileSchema = None, **kwargs):
        """
        Update `CaProfileSchema <jnpr.healthbot.swagger.models.html#caprofileschema>`_ for
        given ca profile schema

        Passing Schema invoke `put` and kwargs `post`

        :param obj schema: `CaProfileSchema <jnpr.healthbot.swagger.models.html#caprofileschema>`_
        :param object kwargs: key values, which can be used to create
            CaProfileSchema
            Check `CaProfileSchema <jnpr.healthbot.swagger.models.html#caprofileschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schemaObj = hb.settings.security.ca_profile.get('xyz')
                schemaObj.certificate_authority_crt = 'pqr.crt'
                hb.settings.security.ca_profile.update(schemaObj)

        :returns: True when OK
        """
        if schema is None:
            schema = CaProfileSchema(**kwargs)
            call = self.api.post
        else:
            if not isinstance(schema, CaProfileSchema):
                raise SchemaError(CaProfileSchema)
            call = self.api.put
        payload = self.hbot._create_payload(schema)
        name = schema.name
        ca_profile_url = self.hbot.urlfor.ca_profile(name)
        response = call(ca_profile_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True


class LocalCertificate(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def get(self, name: str = None, uncommitted: bool = True):
        """
        Get `LocalCertificateSchema(s) <jnpr.healthbot.swagger.models.html#localcertificateschema>`_ for
        given local certificate name or list for all

        :param name: ID of name
        :param bool uncommitted: True includes fetches uncommitted changes,
            False restricts data set to only committed changes

        Example:
            ::
                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.settings.security.local_certificate.get('xyz')

                    # for all
                    print(hb.settings.security.local_certificate.get()

        :return: `LocalCertificateSchema(s) <jnpr.healthbot.swagger.models.html#localcertificateschema>`_
        """
        if name is not None:
            local_cert_url = self.hbot.urlfor.local_certificate(name)
            if uncommitted:
                local_cert_url += self.hbot.apiopt_candidate
            response = self.api.get(local_cert_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(
                response, LocalCertificateSchema)
        else:
            local_certs_url = self.hbot.urlfor.local_certificates()
            if uncommitted:
                local_certs_url += self.hbot.apiopt_candidate
            response = self.api.get(local_certs_url)
            response_json = response.json()
            if response.status_code != 200:
                logger.error(response.text)
                raise NotFoundError(response_json)
            existing_local_certificates = response_json['local-certificate']
            local_certificates_list = []
            for local_certificate in existing_local_certificates:
                obj = self.hbot._create_schema(local_certificate, LocalCertificateSchema)
                local_certificates_list.append(obj)

            return local_certificates_list

    def add(self, schema: LocalCertificateSchema = None, **kwargs):
        """
        Add local certificate to security settings of HealthBot.
        The onus of uploading helper file (cert and key) is on user.
        They should use hb.upload_helper_file API to make sure these crt/key
        file are uploaded in system.
        We don't do that validation as user can also upload these file after
        configuring profiles.

        :param object schema: `LocalCertificateSchema <jnpr.healthbot.swagger.models.html#localcertificateschema>`_
        :param object kwargs: key values, which can be used to create
            LocalCertificateSchema
            Check `LocalCertificateSchema <jnpr.healthbot.swagger.models.html#localcertificateschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import LocalCertificateSchema

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                local_cert_schema = LocalCertificateSchema(client_crt='abc.crt', client_key='pqr.key', name='hbez')
                hb.settings.security.local_certificate.add(local_cert_schema)

        :returns: True when OK

        """
        if schema is None:
            schema = LocalCertificateSchema(**kwargs)
        payload = self.hbot._create_payload(schema)
        local_certificate_url = self.hbot.urlfor.local_certificate(payload['name'])
        response = self.api.post(local_certificate_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def delete(self, name: str):
        """
        Remove local certificate from security settings

        :param str name: The name of the local_certificate to be deleted

        Example:
        ::
            hb.settings.security.local_certificate.delete('xyz')
            hb.commit()

        :returns: True when OK
        """

        local_certificate_url = self.hbot.urlfor.local_certificate(name)
        response = self.api.delete(local_certificate_url)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()

        return True

    def update(self, schema: LocalCertificateSchema = None, **kwargs):
        """
        Update `LocalCertificateSchema <jnpr.healthbot.swagger.models.html#localcertificateschema>`_ for
        given local certificate schema

        Passing Schema invoke `put` and kwargs `post`

        :param obj schema: `LocalCertificateSchema <jnpr.healthbot.swagger.models.html#localcertificateschema>`_
        :param object kwargs: key values, which can be used to create
            LocalCertificateSchema
            Check `LocalCertificateSchema <jnpr.healthbot.swagger.models.html#localcertificateschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schemaObj = hb.settings.security.local_certificate.get('xyz')
                schemaObj.client_key = 'xyz.key'
                hb.settings.security.local_certificate.update(schemaObj)

        :returns: True when OK
        """
        if schema is None:
            schema = LocalCertificateSchema(**kwargs)
            call = self.api.post
        else:
            if not isinstance(schema, LocalCertificateSchema):
                raise SchemaError(LocalCertificateSchema)
            call = self.api.put
        payload = self.hbot._create_payload(schema)
        name = schema.name
        local_certificate_url = self.hbot.urlfor.local_certificate(name)
        response = call(local_certificate_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True


class SshKeyProfile(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def get(self, name: str = None, uncommitted: bool = True):
        """
        Get `SshKeyProfileSchema(s) <jnpr.healthbot.swagger.models.html#sshkeyprofileschema>`_ for
        given ssh key profile name or list for all

        :param name: ID of name
        :param bool uncommitted: True includes fetches uncommitted changes,
            False restricts data set to only committed changes

        Example:
            ::
                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.settings.security.ssh_key_profile.get('xyz')

                    # for all
                    print(hb.settings.security.ssh_key_profile.get()

        :return: `SshKeyProfileSchema(s) <jnpr.healthbot.swagger.models.html#sshkeyprofileschema>`_
        """
        if name is not None:
            ssh_key_profile_url = self.hbot.urlfor.ssh_key_profile(name)
            if uncommitted:
                ssh_key_profile_url += self.hbot.apiopt_candidate
            response = self.api.get(ssh_key_profile_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(
                response, SshKeyProfileSchema)
        else:
            ssh_key_profiles_url = self.hbot.urlfor.ssh_key_profiles()
            if uncommitted:
                ssh_key_profiles_url += self.hbot.apiopt_candidate
            response = self.api.get(ssh_key_profiles_url)
            response_json = response.json()
            if response.status_code != 200:
                logger.error(response.text)
                raise NotFoundError(response_json)
            existing_ssh_key_profiles = response_json['ssh-key-profile']
            ssh_key_profiles_list = []
            for ssh_key_profile in existing_ssh_key_profiles:
                obj = self.hbot._create_schema(ssh_key_profile, SshKeyProfileSchema)
                ssh_key_profiles_list.append(obj)

            return ssh_key_profiles_list

    def add(self, schema: SshKeyProfileSchema = None, **kwargs):
        """
        Add ssh key profile to HealthBot.
        The onus of uploading helper file ssh_private_key_file is on user.
        They should use hb.upload_helper_file API to make sure these key file
        are uploaded in system.
        We don't do that validation as user can also upload these file after
        configuring profiles.

        :param object schema: `SshKeyProfileSchema <jnpr.healthbot.swagger.models.html#sshkeyprofileschema>`_
        :param object kwargs: key values, which can be used to create
            SshKeyProfileSchema
            Check `SshKeyProfileSchema <jnpr.healthbot.swagger.models.html#sshkeyprofileschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import SshKeyProfileSchema

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                ssh_key_prof_schema = SshKeyProfileSchema(name='hbez', ssh_private_key_file='abc.crt',
                    ssh_private_key_passphrase='%$#@#')
                hb.settings.security.ssh_key_profile.add(ssh_key_prof_schema)

        :returns: True when OK

        """
        if schema is None:
            schema = SshKeyProfileSchema(**kwargs)
        payload = self.hbot._create_payload(schema)
        ssh_key_profile_url = self.hbot.urlfor.ssh_key_profile(payload['name'])
        response = self.api.post(ssh_key_profile_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def delete(self, name: str):
        """
        Remove ssh key profile from security settings

        :param str name: The name of the ssh key profile to be deleted

        Example:
        ::
            hb.settings.security.ssh_key_profile.delete('xyz')
            hb.commit()

        :returns: True when OK
        """

        ssh_key_profile_url = self.hbot.urlfor.ssh_key_profile(name)
        response = self.api.delete(ssh_key_profile_url)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()

        return True

    def update(self, schema: SshKeyProfileSchema = None, **kwargs):
        """
        Update `SshKeyProfileSchema <jnpr.healthbot.swagger.models.html#sshkeyprofileschema>`_ for
        given ssh key profile schema

        Passing Schema invoke `put` and kwargs `post`

        :param obj schema: `SshKeyProfileSchema <jnpr.healthbot.swagger.models.html#sshkeyprofileschema>`_
        :param object kwargs: key values, which can be used to create
            SshKeyProfileSchema
            Check `SshKeyProfileSchema <jnpr.healthbot.swagger.models.html#sshkeyprofileschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schemaObj = hb.settings.security.ssh_key_profile.get('xyz')
                schemaObj.certificate_authority_crt = 'pqr.crt'
                hb.settings.security.ssh_key_profile.update(schemaObj)

        :returns: True when OK
        """
        if schema is None:
            schema = SshKeyProfileSchema(**kwargs)
            call = self.api.post
        else:
            if not isinstance(schema, SshKeyProfileSchema):
                raise SchemaError(SshKeyProfileSchema)
            call = self.api.put
        payload = self.hbot._create_payload(schema)
        name = schema.name
        ssh_key_profile_url = self.hbot.urlfor.ssh_key_profile(name)
        response = call(ssh_key_profile_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True


class DataSummarization(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)
        self.raw = Raw(hbot)


class Raw(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def get(self): pass

    def add(self): pass

    def delete(self, name: str): pass

    def update(self): pass
