import unittest
from nose.plugins.attrib import attr

from mock import patch, PropertyMock

from jnpr.healthbot import HealthBotClient
from jnpr.healthbot import CaProfileSchema
from jnpr.healthbot import LocalCertificateSchema
from jnpr.healthbot import SshKeyProfileSchema
from requests.models import Response
from . import _mock_user_login

@attr('unit')
class TestProfiles(unittest.TestCase):

    @patch('jnpr.healthbot.healthbot.requests.Session')
    @patch('jnpr.healthbot.swagger.api.authentication_api.AuthenticationApi.user_login')
    def setUp(self, mock_user_login, mock_request):
        self.mock_user_login = _mock_user_login
        self.mock_request = mock_request
        with patch('jnpr.healthbot.healthbot.HealthBotClient.version',
                   new_callable=PropertyMock) as mock_ver:
            with patch('jnpr.healthbot.healthbot.HealthBotClient.config_url',
                       new_callable=PropertyMock) as mock_cnf:
                mock_ver.return_value = '2.1.0'
                mock_cnf.return_value = "https://1.1.1.1:8080/api/v1"
                self.conn = HealthBotClient(
                    server='1.1.1.1',
                    user='test',
                    password='password123').open()

    def tearDown(self) -> None:
        self.conn.close()

    def test_add_caprofile(self):
        ca_prof_schema = CaProfileSchema(
            certificate_authority_crt='abc.crt', name='hbez')
        self.assertTrue(
            self.conn.settings.security.ca_profile.add(ca_prof_schema))
        self.assertTrue(
            self.conn.settings.security.ca_profile.add(
                certificate_authority_crt='abc.crt',
                name='hbez'))

    def test_get_caprofile(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.profile.security.ca_profile.get()
        self.assertEqual(ret[0].certificate_authority_crt, "test.crt")
        ret = self.conn.profile.security.ca_profile.get("hbez")
        self.assertEqual(ret.certificate_authority_crt, "test.crt")

    def test_update_caprofile(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.profile.security.ca_profile.get("hbez")
        ret.certificate_authority_crt = "changed.crt"
        self.assertTrue(self.conn.profile.security.ca_profile.update(ret))
        self.assertTrue(self.conn.profile.security.ca_profile.update(
            certificate_authority_crt='changed.crt', name='hbez'))

    def test_delete_caprofile(self):
        self.mock_request().get.side_effect = self._mock_manager
        self.conn.profile.security.ca_profile.delete("hbez")
        self.assertEqual(self.mock_request().mock_calls[2][0],
                         'delete')

    def test_add_local_certificate(self):
        local_cert_schema = LocalCertificateSchema(
            client_crt='abc.crt', client_key='pqr.key', name='hbez')
        self.assertTrue(
            self.conn.settings.security.local_certificate.add(local_cert_schema))
        self.assertTrue(self.conn.settings.security.local_certificate.add(
            client_crt='abc.crt', client_key='pqr.key', name='hbez'))

    def test_get_local_certificate(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.profile.security.local_certificate.get()
        self.assertEqual(ret[0].client_crt, "test.crt")
        ret = self.conn.profile.security.local_certificate.get("hbez")
        self.assertEqual(ret.client_crt, "test.crt")

    def test_update_local_certificate(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.profile.security.local_certificate.get("hbez")
        ret.client_crt = "changed.crt"
        self.assertTrue(
            self.conn.profile.security.local_certificate.update(ret))
        self.assertTrue(self.conn.profile.security.local_certificate.update(
            client_crt='changed.crt', client_key='pqr.key', name='hbez'))

    def test_delete_local_certificate(self):
        self.mock_request().get.side_effect = self._mock_manager
        self.conn.profile.security.local_certificate.delete("hbez")
        self.assertEqual(self.mock_request().mock_calls[2][0],
                         'delete')

    def test_add_ssh_key_profile(self):
        ssh_key_prof_schema = SshKeyProfileSchema(
            name='hbez',
            ssh_private_key_file='abc.crt',
            ssh_private_key_passphrase='%$#@#')
        self.assertTrue(
            self.conn.settings.security.ssh_key_profile.add(ssh_key_prof_schema))
        self.assertTrue(
            self.conn.settings.security.ssh_key_profile.add(
                name='hbez',
                ssh_private_key_file='abc.crt',
                ssh_private_key_passphrase='%$#@#'))

    def test_get_ssh_key_profile(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.profile.security.ssh_key_profile.get()
        self.assertEqual(ret[0].ssh_private_key_file, "test.key")
        ret = self.conn.profile.security.ssh_key_profile.get("hbez")
        self.assertEqual(ret.ssh_private_key_file, "test.key")

    def test_update_ssh_key_profile(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.profile.security.ssh_key_profile.get("hbez")
        ret.ssh_private_key_file = "changed.crt"
        self.assertTrue(
            self.conn.profile.security.ssh_key_profile.update(ret))
        self.assertTrue(
            self.conn.profile.security.ssh_key_profile.update(
                name='hbez',
                ssh_private_key_file='changed.crt',
                ssh_private_key_passphrase='%$#@#'))

    def test_delete_ssh_key_profile(self):
        self.mock_request().get.side_effect = self._mock_manager
        self.conn.profile.security.ssh_key_profile.delete("hbez")
        self.assertEqual(self.mock_request().mock_calls[2][0],
                         'delete')

    def _mock_manager(self, *args):
        class MockResponse(Response):
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            @property
            def text(self):
                return 'did you just hit an error'

            def json(self):
                return self.json_data

            def to_dict(self):
                return self.json_data

            def raise_for_status(self):
                return None

        if args[0] == 'https://1.1.1.1:8080/api/v1/profile/security/ca-profiles/?working=true':
            return MockResponse({
                "ca-profile": [
                    {
                        "certificate-authority-crt": "test.crt",
                        "name": "hbez"
                    }
                ]
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/profile/security/ca-profile/hbez/?working=true':
            return MockResponse({
                "certificate-authority-crt": "test.crt",
                "name": "hbez"
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/profile/security/local-certificates/?working=true':
            return MockResponse({
                "local-certificate": [
                    {
                        "client-crt": "test.crt",
                        "client-key": "test.key",
                        "name": "hbez"
                    }
                ]
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/profile/security/local-certificate/hbez/?working=true':
            return MockResponse({
                "client-crt": "test.crt",
                "client-key": "test.key",
                "name": "hbez"
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/profile/security/ssh-key-profiles/?working=true':
            return MockResponse({
                "ssh-key-profile": [
                    {
                        "name": "hbez",
                        "ssh-private-key-file": "test.key",
                        "ssh-private-key-passphrase": "$9$AQhzt1heK87dsWLZUiHmP1RE"
                    }
                ]
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/profile/security/ssh-key-profile/hbez/?working=true':
            return MockResponse({
                "name": "hbez",
                "ssh-private-key-file": "test.key",
                "ssh-private-key-passphrase": "$9$AQhzt1heK87dsWLZUiHmP1RE"
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/notification/error/?working=true':
            obj = MockResponse(None, 404)

            def fn():
                raise ValueError
            obj.raise_for_status = fn
            return obj
        return MockResponse(None, 404)
