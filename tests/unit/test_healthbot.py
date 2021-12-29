import unittest
from nose.plugins.attrib import attr

from jnpr.healthbot import HealthBotClient
from jnpr.healthbot.modules.devices import Device
from jnpr.healthbot.modules.playbooks import Playbook
from jnpr.healthbot.modules.rules import Rule

from mock import patch, PropertyMock
from requests.models import Response
from . import _mock_user_login


@attr('unit')
class TestHealthBotClient(unittest.TestCase):

    @patch('jnpr.healthbot.healthbot.requests.Session')
    @patch('jnpr.healthbot.swagger.api.authentication_api.AuthenticationApi.user_login')
    def setUp(self, mock_user_login, mock_request):
        self.mock_user_login = _mock_user_login
        self.mock_request = mock_request
        with patch('jnpr.healthbot.healthbot.HealthBotClient.version',
                   new_callable=PropertyMock) as mock_ver:
            with patch('jnpr.healthbot.healthbot.HealthBotClient.config_url',
                       new_callable=PropertyMock) as mock_cnf:
                with patch('jnpr.healthbot.healthbot.HealthBotClient.tenant',
                           new_callable=PropertyMock) as mock_tenant:

                    mock_ver.return_value = '4.0.0'
                    mock_cnf.return_value = "https://1.1.1.1:8080/api/v2/config"
                    mock_tenant.return_value = "default"
                    self.conn = HealthBotClient(
                        server='1.1.1.1',
                        user='test',
                        password='password123').open()

    def test_check_attributes(self):
        self.assertIsInstance(self.conn.device, Device)
        self.assertIsInstance(self.conn.playbook, Playbook)
        self.assertIsInstance(self.conn.rule, Rule)

    def test_check_mandatory_params(self):
        self.assertRaises(
            ValueError,
            HealthBotClient,
            server="",
            user='test',
            password='password123')
        self.assertRaises(
            ValueError,
            HealthBotClient,
            server="1.1.1.1",
            user="",
            password='password123')
        self.assertRaises(
            ValueError,
            HealthBotClient,
            server="1.1.1.1",
            user="test",
            password="")

    def test_version_new_versions(self):
        self.mock_request().get.side_effect = self._mock_manager
        self.assertEqual(self.conn.version, '4.0.0')

    def test_version_old_versions(self):
        self.assertEqual(self.conn.version, "4.0.0")

    @patch('jnpr.healthbot.healthbot.requests.Session')
    @patch('jnpr.healthbot.swagger.api.authentication_api.AuthenticationApi.user_login')
    @patch('jnpr.healthbot.swagger.api.authentication_api.AuthenticationApi.user_logout')
    def test_context_manager(self, mock_user_logout, mock_user_login, mock_request):
        self.mock_user_login = _mock_user_login
        with patch('jnpr.healthbot.healthbot.HealthBotClient.version',
                   new_callable=PropertyMock) as mock_ver:
            with patch('jnpr.healthbot.healthbot.HealthBotClient.config_url',
                       new_callable=PropertyMock) as mock_cnf:
                mock_ver.return_value = '2.0.1'
                mock_cnf.return_value = "https://1.1.1.1:8080/api/v2/config"
                with HealthBotClient(server='1.1.1.1', user='test',
                                     password='password123') as conn:
                    self.assertEqual(conn.version, '2.0.1')

    def test_rollback(self):
        self.conn.rollback()
        self.assertEqual(self.mock_request().mock_calls[2][0],
                         'delete')

    def test_commit(self):
        with patch('jnpr.healthbot.healthbot.HealthBotClient.config_url',
                   new_callable=PropertyMock) as mock_cnf:
            mock_cnf.return_value = "https://1.1.1.1:8080/api/v2/config"
            self.conn.commit()
            self.assertEqual(self.mock_request().mock_calls[2][0],
                             'post')
            self.assertEqual(self.mock_request().mock_calls[2][1],
                             ('https://1.1.1.1:8080/api/v2/config/configuration',))

    @patch('jnpr.healthbot.healthbot.Path.open')
    def test_upload_helper_file(self, mock_open):
        self.mock_request().post.side_effect = self._mock_manager
        self.assertTrue(self.conn.upload_helper_file('text.rule'))
        self.assertTrue(self.conn.upload_helper_file('text.playbook'))
        self.assertTrue(self.conn.upload_helper_file('text'))

    def test_get_health(self):
        self.mock_request().get.side_effect = self._mock_manager
        health = self.conn.health()
        self.assertEqual(health.network_health, {'HbEZ': 'gray'})

    def _mock_manager(self, *args, **kwargs):
        class MockResponse(Response):
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

            def to_dict(self):
                return self.json_data

            def raise_for_status(self):
                return None

        if 'url' in kwargs:
            if kwargs['url'] == 'https://1.1.1.1:8080/api/v2/config/files/helper-files/text':
                return MockResponse({}, 200)
            if kwargs['url'] == 'https://1.1.1.1:8080/api/v2/config/topics':
                return MockResponse({}, 200)
            if kwargs['url'] == 'https://1.1.1.1:8080/api/v2/config/playbooks':
                return MockResponse({}, 200)
        if args[0] == 'https://1.1.1.1:8080/api/v2/system-details':
            return MockResponse({
                "server-time": "2019-07-24T12:51:20Z",
                "version": "HealthBot 4.0.0"
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v2/system-details':
            return MockResponse({
                "server-time": "2019-07-24T12:51:20Z",
                "version": "HealthBot 4.0.0"
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v2/health':
            return MockResponse({
                "device-health": {
                    "EVO": {
                        "EVO_Core": "gray"
                    },
                    "avro": {
                        "edge": "gray",
                        "real": "gray"
                    },
                    "demo": {},
                    "node1": {
                        "QFabric": "gray"
                    },
                    "vmx": {
                        "Core": "gray"
                    }
                },
                "network-health": {
                    "HbEZ": "gray"
                }
            }, 200)
        return MockResponse(None, 404)
