import unittest
from nose.plugins.attrib import attr

from jnpr.healthbot import HealthBotClient
from jnpr.healthbot import DeviceSchema, DeviceGroupSchema
from jnpr.healthbot.exception import SchemaError
from mock import patch, PropertyMock
from requests.models import Response
from . import _mock_user_login

@attr('unit')
class TestDevices(unittest.TestCase):

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

    def test_add_device(self):
        self.mock_request().post.side_effect = self._mock_manager
        ret = self.conn.device.add('core', 'user', 'password')
        self.assertTrue(ret)

    def test_add_device_existing(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.device.add(
            'vmx', '10.221.136.140', 'user', 'password')
        self.assertTrue(ret)

    def test_add_device_using_schema(self):

        self.mock_request().post.side_effect = self._mock_manager
        from jnpr.healthbot import DeviceSchema

        ds = DeviceSchema(
            device_id='core',
            host='10.221.136.140',
            authentication={
                "password": {
                    "password": "xxxx",
                    "username": "xxxx"}})
        ret = self.conn.device.add(schema=ds)
        self.assertTrue(ret)

    def test_get_device_ids_default_empty(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.device.get_ids()
        self.assertEqual(ret, [])

    def test_delete_device(self):
        self.mock_request().delete.side_effect = self._mock_manager
        ret = self.conn.device.delete(device_id='core')
        self.assertTrue(ret)

    def test_delete_device_force(self):
        self.mock_request().delete.side_effect = self._mock_manager
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.device.delete(device_id='core', force=True)
        self.assertTrue(ret)
        self.assertEqual(self.mock_request().mock_calls[2][0], 'get')
        self.assertEqual(self.mock_request().mock_calls[4][0], 'put')
        self.assertEqual(self.mock_request().mock_calls[2][1][0],
                         'https://1.1.1.1:8080/api/v1/device-groups')
        self.assertEqual(self.mock_request().mock_calls[4][1][0],
                         'https://1.1.1.1:8080/api/v1/device-group/edge')
        self.assertEqual(self.mock_request().mock_calls[4][2]['json'],
                         {'description': 'testing', 'device-group-name': 'edge',
                          'devices': ['demo'], 'native-gpb': {'ports': [22000]},
                          'notification': {}, 'playbooks': ['eventd-debug-collection',
                                                            'eventd-kpis-playbook'],
                          'reports': [], 'variable': []})

    def test_get_device(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.device.get(device_id='core')
        self.assertIsInstance(ret, DeviceSchema)

    def test_get_devices(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.device.get()
        self.assertGreater(len(ret), 0)

    def test_update_device(self):
        self.mock_request().get.side_effect = self._mock_manager
        obj = self.conn.device.get(device_id='core')
        obj.description = 'test in progress'
        self.conn.device.update(schema=obj)
        self.assertEqual(
            self.mock_request().mock_calls[3][2]['json']['description'],
            'test in progress')

    def test_get_device_facts(self):
        self.mock_request().get.side_effect = self._mock_manager
        obj = self.conn.device.get_facts(device_id='core')
        self.assertIn('facts', obj)

    def test_get_devices_facts(self):
        self.mock_request().get.side_effect = self._mock_manager
        obj = self.conn.device.get_facts()
        self.assertNotEqual(len(obj), 0)

    def test_add_device_group(self):
        dgs = DeviceGroupSchema(device_group_name="edge",
                                description="All devices on the edge",
                                devices=['xyz'])
        self.assertTrue(self.conn.device_group.add(dgs))

    def test_add_device_group_wrong_schema(self):
        dgs = DeviceSchema(
            device_id='core',
            host='10.221.136.140',
            authentication={
                "password": {
                    "password": "xxxx",
                    "username": "xxxx"}})
        self.assertRaises(SchemaError, self.conn.device_group.add, dgs)

    def test_delete_device_group(self):
        self.assertTrue(
            self.conn.device_group.delete(
                device_group_name="edge"))

    def test_delete_device_group_force(self):
        self.mock_request().get.side_effect = self._mock_manager
        self.assertTrue(
            self.conn.device_group.delete(
                device_group_name="edge", force=True))

    def test_get_device_group(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.device_group.get('Core')
        self.assertEqual(ret.description, 'testing')

    def test_update_device_group(self):
        self.mock_request().get.side_effect = self._mock_manager
        obj = self.conn.device_group.get('Core')
        obj.description = 'test in progress'
        self.conn.device_group.update(schema=obj)
        self.assertEqual(
            self.mock_request().mock_calls[3][2]['json']['description'],
            'test in progress')

    def test_get_device_groups(self):
        self.mock_request().get.side_effect = self._mock_manager
        obj = self.conn.device_group.get()
        self.assertNotEqual(len(obj), 0)

    def test_check_device_in_group(self):
        self.mock_request().get.side_effect = self._mock_manager
        self.assertTrue(
            self.conn.device_group.check_device_in_group(
                'vmx', 'Core'))

    def test_add_device_in_group(self):
        self.mock_request().get.side_effect = self._mock_manager
        self.assertTrue(
            self.conn.device_group.add_device_in_group(
                'test', 'Core'))
        self.assertEqual(
            self.mock_request().mock_calls[4][2]['json']['devices'], [
                'vmx', 'core', 'test'])

    def test_add_device_in_group_with_group_data_none(self):
        self.mock_request().get.side_effect = self._mock_manager
        self.assertTrue(
            self.conn.device_group.add_device_in_group(
                'test', 'alpha'))
        self.assertEqual(
            self.mock_request().mock_calls[4][2]['json'],
            {'device-group-name': 'alpha', 'devices': ['test']})

    def test_add_network_group(self):
        self.mock_request().post.side_effect = self._mock_manager
        self.mock_request().get.side_effect = self._mock_manager
        from jnpr.healthbot.modules.devices import NetworkGroupSchema
        ngs = NetworkGroupSchema(network_group_name="HbEZ")
        ret = self.conn.network_group.add(schema=ngs)
        self.assertTrue(ret)

    def test_add_network_group_existing(self):
        self.mock_request().get.side_effect = self._mock_manager
        self.assertTrue(
            self.conn.network_group.add(
                network_group_name="HbEZ"))

    def test_get_network_group(self):
        self.mock_request().get.side_effect = self._mock_manager
        obj = self.conn.network_group.get(network_group_name="HbEZ")
        self.assertEqual(obj.description, "testing")

    def test_get_network_groups(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.network_group.get()
        self.assertGreater(len(ret), 0)

    def test_update_network_group(self):
        self.mock_request().get.side_effect = self._mock_manager
        obj = self.conn.network_group.get('HbEZ')
        obj.description = 'test in progress'
        self.conn.network_group.update(schema=obj)
        self.assertEqual(
            self.mock_request().mock_calls[3][2]['json']['description'],
            'test in progress')

    def test_delete_network_group(self):
        self.assertTrue(self.conn.network_group.delete(
            network_group_name="HbEZ"))

    def test_get_device_health(self):
        self.mock_request().get.side_effect = self._mock_manager
        health = self.conn.device.health('avro')
        self.assertEqual(health.color, 'red')

    def test_get_device_group_health(self):
        self.mock_request().get.side_effect = self._mock_manager
        health = self.conn.device_group.health('Core')
        self.assertEqual(health.color, 'yellow')

    def test_get_network_group_health(self):
        self.mock_request().get.side_effect = self._mock_manager
        health = self.conn.network_group.health('Core')
        self.assertEqual(health.color, 'yellow')

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

        if args[0] == 'https://1.1.1.1:8080/api/v1/device/core' and kwargs != {}:
            return MockResponse({}, 200)
        elif args[0] in ['https://1.1.1.1:8080/api/v1/device-groups',
                         'https://1.1.1.1:8080/api/v1/device-groups/?working=true']:
            return MockResponse({
                "device-group": [
                    {
                        "description": "learning",
                        "device-group-name": "Core",
                        "devices": [
                            "vmx"
                        ],
                        "native-gpb": {
                            "ports": [
                                22000
                            ]
                        },
                        "notification": {},
                        "playbooks": [
                            "eventd-debug-collection",
                            "eventd-kpis-playbook"
                        ],
                        "reports": [],
                        "variable": []
                    },
                    {
                        "description": "All devices on the edge",
                        "device-group-name": "edge",
                        "devices": [
                            "demo",
                            "core"
                        ],
                        "notification": {},
                        "playbooks": [],
                        "reports": []
                    },
                    {
                        "device-group-name": "real",
                        "devices": [
                            "avro"
                        ],
                        "notification": {},
                        "playbooks": [
                            "online-fpc-playbook",
                            "phyport"
                        ],
                        "reports": [],
                        "variable": [
                            {
                                "@": {
                                    "changed-seconds": 1563348601
                                },
                                "instance-id": "ge-1-0-0",
                                "playbook": "phyport",
                                "rule": "external/interface-info",
                                "variable-value": [
                                    {
                                        "name": "interface_name",
                                        "value": "ge-1/0/0"
                                    }
                                ]
                            },
                            {
                                "@": {
                                    "changed-seconds": 1563348601
                                },
                                "instance-id": "ge-1-0-1",
                                "playbook": "phyport",
                                "rule": "external/interface-info",
                                "variable-value": [
                                    {
                                        "name": "interface_name",
                                        "value": "ge-1/0/1"
                                    }
                                ]
                            },
                            {
                                "@": {
                                    "changed-seconds": 1563348601
                                },
                                "instance-id": "xyz",
                                "playbook": "online-fpc-playbook",
                                "rule": "linecard.statistics/update-online-fpc"
                            }
                        ]
                    },
                    {
                        "description": "xyz",
                        "device-group-name": "QFabric",
                        "devices": [
                            "vmx"
                        ],
                        "notification": {},
                        "playbooks": [],
                        "reports": [],
                        "variable": []
                    }
                ]
            }, 200)
        elif args[0] in ['https://1.1.1.1:8080/api/v1/device-group/Core/?working=true',
                         'https://1.1.1.1:8080/api/v1/device-group/Core']:
            return MockResponse({
                "description": "testing",
                "device-group-name": "Core",
                "devices": [
                    "vmx",
                    "core"
                ],
                "native-gpb": {
                    "ports": [
                        22000
                    ]
                },
                "notification": {},
                "playbooks": [
                    "eventd-debug-collection",
                    "eventd-kpis-playbook"
                ],
                "reports": [],
                "variable": []
            }, 200)
        elif args[0] in ['https://1.1.1.1:8080/api/v1/device-group/edge/?working=true',
                         'https://1.1.1.1:8080/api/v1/device-group/edge']:
            return MockResponse({
                "description": "testing",
                "device-group-name": "edge",
                "devices": [
                    "vmx",
                    "core"
                ],
                "native-gpb": {
                    "ports": [
                        22000
                    ]
                },
                "notification": {},
                "playbooks": [
                    "eventd-debug-collection",
                    "eventd-kpis-playbook"
                ],
                "reports": [],
                "variable": []
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/device-group/QFabric':
            return MockResponse({}, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/device/core':
            return MockResponse({}, 204)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/device/core/?working=true':
            return MockResponse({
                "authentication": {
                    "password": {
                        "password": "xxxx",
                        "username": "xxxx"
                    }
                },
                "device-id": "vmx",
                "host": "10.221.136.140",
                "open-config": {
                    "port": 32767
                },
                "system-id": "testing",
                "variable": [],
                "vendor": {
                    "juniper": {
                        "operating-system": "junos"
                    }
                }
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/device/core/facts/?working=true':
            return MockResponse({"device-id": "core",
                                 "facts": {"fpc": [],
                                           "hostname": "R1_re0",
                                           "platform": "MX960",
                                           "platform-info": [{"name": "re0",
                                                              "platform": "MX960"}],
                                           "product": "MX",
                                           }},
                                200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/devices/facts/?working=true':
            return MockResponse([{"device-id": "core",
                                  "facts": {"fpc": [],
                                            "hostname": "R1_re0",
                                            "platform": "MX960",
                                            "platform-info": [{"name": "re0",
                                                               "platform": "MX960"}],
                                            "product": "MX",
                                            }}],
                                200)
        if args[0] == 'https://1.1.1.1:8080/api/v1/devices/?working=true':
            return MockResponse({"device": [
                {
                    "authentication": {
                        "password": {
                            "password": "xxxxx",
                            "username": "xxxx"
                        }
                    },
                    "device-id": "vmx",
                    "host": "10.221.136.140",
                    "open-config": {
                        "port": 32767
                    },
                    "system-id": "testing",
                    "variable": [],
                    "vendor": {
                        "juniper": {
                            "operating-system": "junos"
                        }
                    }
                },
                {
                    "authentication": {
                        "password": {
                            "password": "xxxx",
                            "username": "xxxx"
                        }
                    },
                    "device-id": "avro",
                    "host": "10.209.14.109",
                    "open-config": {
                        "port": 32767
                    },
                    "vendor": {
                        "juniper": {
                            "operating-system": "junos"
                        }
                    }
                },
                {
                    "authentication": {
                        "password": {
                            "password": "xxxx",
                            "username": "xxx"
                        }
                    },
                    "device-id": "node1",
                    "host": "node1",
                    "open-config": {
                        "port": 32767
                    },
                    "vendor": {
                        "juniper": {
                            "operating-system": "junos"
                        }
                    }
                },
                {
                    "authentication": {
                        "password": {
                            "password": "xxxx",
                            "username": "xxxx"
                        }
                    },
                    "device-id": "demo",
                    "host": "10.221.136.140",
                    "system-id": "Demo:HbEZ"
                }
            ]
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/network-group/HbEZ/?working=true':
            obj = MockResponse({'description': "testing",
                                'network-group-name': 'HbEZ',
                                'notification': {},
                                'playbooks': [],
                                'reports': [],
                                'variable': None}, 200)
            return obj
        elif args[0] == 'https://1.1.1.1:8080/api/v1/network-groups/?working=true':
            obj = MockResponse({
                "network-group": [
                    {
                        "network-group-name": "HbEZ",
                        "notification": {},
                        "playbooks": [],
                        "reports": []
                    }
                ]
            }, 200)
            return obj
        elif args[0] == 'https://1.1.1.1:8080/api/v1/services/device-group/':
            return MockResponse(["edge"], 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/health-tree/avro':
            return MockResponse({'children': [{'children': [{'children': [{'children': [{'color': 'red',
                                                                                         'data': 'either is '
                                                                                         'down',
                                                                                         'name': 'check-status',
                                                                                         'timestamp': '2019-07-22T10:28:08Z'}],
                                                                           'color': 'red',
                                                                           'name': '_instance_id: ["ge-1-0-1", '
                                                                           '"ge-1-0-0"], '
                                                                           '_playbook_name: phyport, '
                                                                           'name: ge-1/0/1'},
                                                                          {'children': [{'color': 'red',
                                                                                         'data': 'either is '
                                                                                         'down',
                                                                                         'name': 'check-status',
                                                                                         'timestamp': '2019-07-22T10:28:08Z'}],
                                                                           'color': 'red',
                                                                           'name': '_instance_id: ["ge-1-0-1", '
                                                                           '"ge-1-0-0"], '
                                                                           '_playbook_name: phyport, '
                                                                           'name: ge-1/0/0'}],
                                                             'color': 'red',
                                                             'name': 'external'}],
                                               'color': 'red',
                                               'name': 'real'}],
                                 'color': 'red',
                                 'data': None,
                                 'name': 'avro',
                                 'timestamp': None},
                                200)
        elif args[0] in ['https://1.1.1.1:8080/api/v1/health-tree/device-group/Core',
                         'https://1.1.1.1:8080/api/v1/health-tree/Core']:
            return MockResponse({"children": [{"children": [{"children": [],
                                                             "name": "interface.statistics"},
                                                            {"children": [],
                                                             "name": "linecard.fpc"},
                                                            {"children": [],
                                                             "name": "linecard.ospf"},
                                                            {"children": [],
                                                             "name": "linecard.statistics"},
                                                            {"children": [],
                                                             "name": "system.statistics"}],
                                               "color": "yellow",
                                               "name": "vmx"}],
                                 "color": "yellow",
                                 "name": "Core"},
                                200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/health-tree/network-group/Core':
            return MockResponse({"children": [{"children": [{"children": [],
                                                             "name": "interface.statistics"},
                                                            {"children": [],
                                                             "name": "linecard.fpc"},
                                                            {"children": [],
                                                             "name": "linecard.ospf"},
                                                            {"children": [],
                                                             "name": "linecard.statistics"},
                                                            {"children": [],
                                                             "name": "system.statistics"}],
                                               "color": "yellow",
                                               "name": "vmx"}],
                                 "color": "yellow",
                                 "name": "Core"},
                                200)
        return MockResponse(None, 404)
