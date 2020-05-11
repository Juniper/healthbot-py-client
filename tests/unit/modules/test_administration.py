import unittest
from nose.plugins.attrib import attr

from mock import patch

from jnpr.healthbot import HealthBotClient
from requests.models import Response
from . import _mock_user_login


@attr('unit')
class TestAdministration(unittest.TestCase):

    @patch('jnpr.healthbot.healthbot.requests.Session')
    @patch('jnpr.healthbot.swagger.api.authentication_api.AuthenticationApi.user_login')
    def setUp(self, mock_user_login, mock_request):
        self.mock_user_login = _mock_user_login
        self.mock_request = mock_request
        self.mock_request().get.side_effect = self._mock_manager
        self.conn = HealthBotClient(
            server='1.1.1.1',
            user='test',
            password='password123').open()
        self.conn.api_client.call_api = self._mock_manager

    def tearDown(self) -> None:
        self.conn.close()

    def test_administration_group_get(self):
        ret = self.conn.administration.group.get(group_name="hboperator")
        self.assertEqual(ret.group_name, 'hboperator')

    def test_administration_group_get_all(self):
        ret = self.conn.administration.group.get()
        self.assertEqual(ret[0].group_name, 'hboperator')

    def test_administration_user_get(self):
        ret = self.conn.administration.user.get(user_name="xxx")
        print(ret)
        self.assertEqual(ret.user_name, 'xxx')

    def test_administration_add_user(self):
        self.conn.administration.user._admin_api.create_users = self._mock_manager
        from jnpr.healthbot import UserSchema, UserSchemaGroups
        group_id = self.conn.administration.group.get_groupid_from_group_name(
            'hboperator')
        user = UserSchema(
            user_name="xxx",
            first_name="xxx",
            last_name="xxx",
            password="xxx",
            email="xxx.xx@gmail.com",
            active=True,
            groups=[
                UserSchemaGroups(
                    group_id=group_id,
                    group_name="hboperator")])
        self.assertTrue(self.conn.administration.user.add(user))

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

        if args == () and 'users' in kwargs:
            return []
        elif args[0] == '/user/{userid}/' and args[1] == 'GET':
            from jnpr.healthbot import InlineResponse2004
            return InlineResponse2004(**{'active': True,
                                          'email': 'abcd.kri@gmail.com',
                                          'first_name': 'xxx',
                                          'last_name': 'kr12',
                                          'user_id': 'xxx-xx-xx-xxx-xxxx',
                                          'user_name': 'xxx'})

        elif args[0] == '/user/' and args[1] == 'GET':
            from jnpr.healthbot import InlineResponse2002
            return [InlineResponse2002(**{'active': True,
                                          'email': 'abcd.kri@gmail.com',
                                          'first_name': 'xxx',
                                          'last_name': 'kr12',
                                          'user_id': 'xxx-xx-xx-xxx-xxxx',
                                          'user_name': 'xxx'})]
        elif args[0] == '/group/' and args[1] == 'GET':
            from jnpr.healthbot import InlineResponse2008
            return [InlineResponse2008(**{'group_description': '',
                                          'group_id': 'xx-xx-xx-xxx-xxxx',
                                          'group_name': 'hboperator',
                                          'roles': None,
                                          'users': None})]
        elif args[0] == '/group/{groupid}/' and args[1] == 'GET':
            from jnpr.healthbot import Groups
            return Groups(**{'group_description': '',
                             'group_name': 'hboperator',
                             'roles': [{'roleId': 'xx-xxx-xxx',
                                        'roleName': 'token:write'},
                                       {'roleId': 'xx-xxy-xxx',
                                        'roleName': 'login:write'},
                                       {'roleId': 'xx-xxz-xxx',
                                        'roleName': 'user-profile:read'},
                                       {'roleId': 'xx-xxi-xxx',
                                        'roleName': 'logout:write'},
                                       {'roleId': 'xx-xxa-xxx',
                                        'roleName': 'first-login:write'}, ],
                             'users': [{'userId': 'xx-yyy-xxx',
                                        'userName': 'admin'}]})
        return MockResponse(None, 404)