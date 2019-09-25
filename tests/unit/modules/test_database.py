import unittest
from nose.plugins.attrib import attr

from mock import patch

from jnpr.healthbot import HealthBotClient


@attr('unit')
class TestRules(unittest.TestCase):

    @patch('jnpr.healthbot.healthbot.requests.Session')
    def setUp(self, mock_request):
        self.mock_request = mock_request
        self.conn = HealthBotClient(
            server='1.1.1.1',
            user='test',
            password='password123')

    def test_get_table(self):
        self.mock_request().get.side_effect = self._mock_manager
        obj = self.conn.tsdb.get_table()
        self.assertEqual(obj.name, 'test')

    def _mock_manager(self, *args):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

            def raise_for_status(self):
                return None

        if args[0] == 'https://1.1.1.1:8080/api/v1/data/database/table':
            return MockResponse({
                "name": "test", "type": "Field table"
            }, 200)
