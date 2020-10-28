import unittest
from nose.plugins.attrib import attr

from jnpr.healthbot import HealthBotClient
from jnpr.healthbot import PlaybookSchema
from jnpr.healthbot import PlayBookInstanceBuilder
from mock import patch, PropertyMock
from requests.models import Response
from . import _mock_user_login

@attr('unit')
class TestPlaybooks(unittest.TestCase):

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

    def test_add_playbook_using_schema_check_existance(self):
        self.mock_request().get.side_effect = self._mock_manager
        pbs = PlaybookSchema(playbook_name="automation-coredump-pb")
        pbs.description = "HbEZ Demo Examples"
        pbs.synopsis = 'fpc status'
        pbs.rules = ['hbez/hbez-fpc-heap-utilization']
        ret = self.conn.playbook.add(pbs)
        self.assertTrue(ret)

    def test_add_playbook_using_schema(self):
        self.mock_request().get.side_effect = self._mock_manager
        pbs = PlaybookSchema(playbook_name="testing")
        pbs.description = "HbEZ Demo Examples"
        pbs.rules = ['hbez/hbez-fpc-heap-utilization']
        self.assertTrue(self.conn.playbook.add(pbs))

    def test_delete_playbook(self):
        self.assertTrue(
            self.conn.playbook.delete(
                playbook_name="testing"))

    def test_get_playbook(self):
        self.mock_request().get.side_effect = self._mock_manager
        obj = self.conn.playbook.get(
            playbook_name="automation-coredump-pb")
        self.assertEqual(obj.rules, [
            "protocol-automation-coredumps/check-coredumps"
        ])

    def test_update_playbook(self):
        self.mock_request().get.side_effect = self._mock_manager
        obj = self.conn.playbook.get(
            playbook_name="automation-coredump-pb")
        obj.description = "testing"
        self.conn.playbook.update(obj)
        self.assertEqual(
            self.mock_request().mock_calls[3][2]['json']['description'],
            "testing")

    def test_get_playbooks(self):
        self.mock_request().get.side_effect = self._mock_manager
        obj = self.conn.playbook.get()
        self.assertGreaterEqual(len(obj), 1)

    def test_playbook_instance_builder_with_no_variable(self):
        self.mock_request().get.side_effect = self._mock_manager
        pbb = PlayBookInstanceBuilder(
            self.conn, 'automation-coredump-pb', 'HbEZ-instance',
            'Core')
        pbb.apply()
        self.assertEqual(self.mock_request().mock_calls[5][0], 'put')
        self.assertEqual(
            self.mock_request().mock_calls[5][1][0],
            'https://1.1.1.1:8080/api/v1/device-group/Core')

    def test_playbook_instance_builder_delete(self):
        self.mock_request().get.side_effect = self._mock_manager
        pbb = PlayBookInstanceBuilder(
            self.conn, 'automation-coredump-pb', 'HbEZ-instance',
            'Core')
        pbb.delete()
        self.assertEqual(self.mock_request().mock_calls[6][0], 'put')
        self.assertEqual(
            self.mock_request().mock_calls[6][1][0],
            'https://1.1.1.1:8080/api/v1/device/vmx')
        self.assertEqual(
            self.mock_request().mock_calls[10][1][0],
            'https://1.1.1.1:8080/api/v1/device-group/Core')

    def test_playbook_apply_commit(self):
        self.mock_request().get.side_effect = self._mock_manager
        with patch('jnpr.healthbot.healthbot.HealthBotClient.config_url',
                   new_callable=PropertyMock) as mock_cnf:
            mock_cnf.return_value = "https://1.1.1.1:8080/api/v1"
            pbb = PlayBookInstanceBuilder(
                self.conn, 'automation-coredump-pb', 'HbEZ-instance',
                'Core')
            pbb.apply(commit=True)
            self.assertEqual(self.mock_request().mock_calls[9][0], 'post')
            self.assertEqual(
                self.mock_request().mock_calls[9][1][0],
                'https://1.1.1.1:8080/api/v1/configuration')

    def test_playbook_instance_builder_with_no_device_group(self):
        from jnpr.healthbot.exception import NotFoundError
        self.mock_request().get.side_effect = self._mock_manager
        pbb = PlayBookInstanceBuilder(
            self.conn, 'automation-coredump-pb', 'xyz', 'real')
        self.assertRaises(NotFoundError, pbb.apply)

    def test_playbook_instance_builder_with_variable(self):
        self.mock_request().get.side_effect = self._mock_manager
        pbb = PlayBookInstanceBuilder(
            self.conn,
            'forwarding-table-summary',
            'HbEZ-instance',
            'Core')
        routesummary_fib_summary = pbb.rule_variables["protocol.routesummary/check-fib-summary"]
        routesummary_fib_summary.route_count_threshold = 200
        routesummary_fib_summary.route_address_family = 'abc'
        pbb.apply()
        self.assertEqual(self.mock_request().mock_calls[6][0], 'put')
        self.assertEqual(
            self.mock_request().mock_calls[6][1][0],
            'https://1.1.1.1:8080/api/v1/device-group/Core')

    def test_playbook_instance_builder_with_variable_per_device(self):
        self.mock_request().get.side_effect = self._mock_manager
        pbb = PlayBookInstanceBuilder(
            self.conn,
            'forwarding-table-summary',
            'HbEZ-instance',
            'Core')
        routesummary_fib_summary = pbb.rule_variables["protocol.routesummary/check-fib-summary"]
        routesummary_fib_summary.route_count_threshold = 200
        routesummary_fib_summary.route_address_family = 'abc'
        pbb.apply(device_ids=['vmx'])
        self.assertEqual(self.mock_request().mock_calls[7][0], 'put')
        self.assertEqual(
            self.mock_request().mock_calls[7][1][0],
            'https://1.1.1.1:8080/api/v1/device/vmx')

    def test_playbook_instance_builder_with_non_existing_device(self):
        self.mock_request().get.side_effect = self._mock_manager
        pbb = PlayBookInstanceBuilder(
            self.conn,
            'forwarding-table-summary',
            'HbEZ-instance',
            'Core')
        routesummary_fib_summary = pbb.rule_variables["protocol.routesummary/check-fib-summary"]
        routesummary_fib_summary.route_count_threshold = 200
        routesummary_fib_summary.route_address_family = 'abc'
        self.assertRaises(RuntimeError, pbb.apply, device_ids=['fake'])

    def test_clear(self):
        self.mock_request().get.side_effect = self._mock_manager
        pbb = PlayBookInstanceBuilder(
            self.conn,
            'forwarding-table-summary',
            'HbEZ-instance',
            'Core')
        routesummary_fib_summary = pbb.rule_variables["protocol.routesummary/check-fib-summary"]
        routesummary_fib_summary.route_count_threshold = 200
        routesummary_fib_summary.route_address_family = 'abc'
        pbb.clear()
        routesummary_fib_summary = pbb.rule_variables["protocol.routesummary/check-fib-summary"]
        self.assertEqual(
            routesummary_fib_summary.route_count_threshold,
            '10000')

    def test_playbook_schema_setter(self):
        self.mock_request().get.side_effect = self._mock_manager
        pbb = PlayBookInstanceBuilder(
            self.conn,
            'forwarding-table-summary',
            'HbEZ-instance',
            'Core')
        with self.assertRaises(RuntimeError):
            pbb.playbook_schema = 30

    def test_get_playbook_schema_error(self):
        self.mock_request().get.side_effect = self._mock_manager
        self.assertRaises(AttributeError, PlayBookInstanceBuilder, self.conn,
                          'dummy', 'HbEZ-instance', 'Core')

    def _mock_manager(self, *args):
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

        if args[0] == 'https://1.1.1.1:8080/api/v1/playbook/automation-coredump-pb/?working=true':
            obj = MockResponse({
                "playbook-name": "automation-coredump-pb",
                "rules": [
                    "protocol-automation-coredumps/check-coredumps"
                ]
            }, 200)
            return obj
        if args[0] == 'https://1.1.1.1:8080/api/v1/topic/protocol-automation-coredumps/rule/check-coredumps/?working=true':
            obj = MockResponse({"description": "This rule will monitor for the automation coredumps",
                                "field": [{"description": "Actual coredump filename",
                                           "field-name": "coredump-filename",
                                           "formula": {"user-defined-function": {"argument": [{"argument": "message",
                                                                                               "value": "$coredump-message"}],
                                                                                 "function-name": "get-core-filename-from-message"}},
                                           "type": "string"},
                                          {"description": "The actual syslog that appears when a coredump happens",
                                           "field-name": "coredump-message",
                                           "sensor": [{"path": "/junos/events/event/message",
                                                       "sensor-name": "coredump-detectors",
                                                       "where": [{"query": "/junos/events/event/message =~ /.*Core and context for (eventd|cscript).*/"}]}],
                                           "type": "string"},
                                          {"description": "Timestamp of the coredump as registered by the telemetry sensor",
                                           "field-name": "coredump-timestamp",
                                           "sensor": [{"path": "/junos/events/event/timestamp/seconds",
                                                       "sensor-name": "coredump-detectors"}],
                                           "type": "string"}],
                                "keys": ["coredump-message"],
                                "rule-name": "check-coredumps",
                                "sensor": [{"open-config": {"frequency": "0s",
                                                            "sensor-name": "/junos/events/event[id='SYSTEM']"},
                                            "sensor-name": "coredump-detectors"}],
                                "synopsis": "To monitor automation coredumps",
                                "trigger": [{"frequency": "15s",
                                             "term": [{"term-name": "core-generated",
                                                       "then": {"status": {"color": "red",
                                                                           "message": "Coredump was seen: $coredump-message"},
                                                                "user-defined-action": [{"argument": [{"argument": "local_dir_name",
                                                                                                       "value": "coredumps"}],
                                                                                         "function-name": "get-automation-traces"},
                                                                                        {"argument": [{"argument": "local_dir_name",
                                                                                                       "value": "coredump"},
                                                                                                      {"argument": "remote_dir_name",
                                                                                                       "value": "$coredump-filename"}],
                                                                                         "function-name": "get-file-from-device"},
                                                                                        {"argument": [{"argument": "local_dir_name",
                                                                                                       "value": "coredump"},
                                                                                                      {"argument": "remote_dir_name",
                                                                                                       "value": "/var/log/* /var/tmp/*"}],
                                                                                         "function-name": "get-log-file-from-device"}]},
                                                       "when": {"matches-with": [{"left-operand": "$coredump-message",
                                                                                  "right-operand": ".*Core and context.*",
                                                                                  "time-range": "30s"}]}},
                                                      {"term-name": "Core-not-generated",
                                                       "then": {"status": {"color": "green",
                                                                           "message": "No core found"}}}],
                                             "trigger-name": "core-generated"}]},
                               200)
            return obj
        if args[0] == 'https://1.1.1.1:8080/api/v1/playbooks/?working=true':
            obj = MockResponse({"playbook": [{"playbook-name": "netsvc-playbook",
                                              "rules": ["chassis.networkservices/netsvc-rule"]},
                                             {"playbook-name": "phyport",
                                              "rules": ["external/interface-info"]},
                                             {"playbook-name": "automation-coredump-pb",
                                              "rules": ["protocol-automation-coredumps/check-coredumps"]},
                                             {"description": "This playbook help to collect eventd debug logs",
                                              "playbook-name": "eventd-debug-collection",
                                              "rules": ["protocol-eventd-debug/collect-debugs"],
                                              "synopsis": "Collect eventd logs"}]},
                               200)
            return obj
        if args[0] == 'https://1.1.1.1:8080/api/v1/topic/protocol.routesummary/rule/check-fib-summary/?working=true':
            obj = MockResponse({
                "description": "Collects forwarding-table's total-route-count of each protocol and sets dynamic thresholds and notify anomaly when route count is abnormal",
                "field": [
                    {
                        "description": "Address family name to be monitored",
                        "field-name": "address-family",
                        "sensor": [
                            {
                                "path": "address-family",
                                "sensor-name": "fib-sensor",
                                "where": [
                                    {
                                        "query": "address-family =~ /^{{route-address-family}}$/"
                                    }
                                ]
                            }
                        ],
                        "type": "string"
                    },
                    {
                        "description": "Detects anamoly dynamically using kmeans algorithm",
                        "field-name": "dt-route-count",
                        "formula": {
                            "dynamic-threshold": {
                                "algorithm": "3sigma",
                                "field-name": "$route-count",
                                "learning-period": "7d",
                                "pattern-periodicity": "1h"
                            }
                        },
                        "type": "integer"
                    },
                    {
                        "description": "Route table type to be monitored",
                        "field-name": "route-table-type",
                        "sensor": [
                            {
                                "path": "route-table-type",
                                "sensor-name": "fib-sensor",
                                "where": [
                                    {
                                        "query": "route-table-type =~ /^{{table-type}}$/"
                                    }
                                ]
                            }
                        ],
                        "type": "string"
                    },
                    {
                        "description": "Route table name to be monitored",
                        "field-name": "table-name",
                        "sensor": [
                            {
                                "path": "table-name",
                                "sensor-name": "fib-sensor",
                                "where": [
                                    {
                                        "query": "table-name =~ /^{{route-table-name}}$/"
                                    }
                                ]
                            }
                        ],
                        "type": "string"
                    },
                    {
                        "constant": {
                            "value": "{{route-count-threshold}}"
                        },
                        "description": "Route count static threshold",
                        "field-name": "threshold",
                        "type": "integer"
                    }
                ],
                "keys": [
                    "address-family",
                    "route-table-type",
                    "table-name"
                ],
                "rule-name": "check-fib-summary",
                "sensor": [
                    {
                        "description": "iAgent sensor collect forwarding-table route-count stats from network device",
                        "iAgent": {
                            "file": "fib.yml",
                            "frequency": "10m",
                            "table": "FibSummaryTable"
                        },
                        "sensor-name": "fib-sensor",
                        "synopsis": "FIB iAgent sensor definition"
                    }
                ],
                "synopsis": "Forwarding-table protocols routes statistics analyzer",
                "trigger": [
                    {
                        "frequency": "10m",
                        "term": [
                            {
                                "term-name": "is-route-count-abnormal",
                                "then": {
                                    "status": {
                                        "color": "red",
                                        "message": "Route count of $table-name of $address-family of $route-table-type is ($route-count) abnormal"
                                    }
                                },
                                "when": {
                                    "greater-than-or-equal-to": [
                                        {
                                            "left-operand": "$route-count",
                                            "right-operand": "$threshold",
                                            "time-range": "30m"
                                        }
                                    ]
                                }
                            },
                            {
                                "term-name": "is-route-count-above-dt",
                                "then": {
                                    "status": {
                                        "color": "yellow",
                                        "message": "Route count of $table-name of $address-family of $route-table-type is ($route-count) is above dynamic threshold"
                                    }
                                },
                                "when": {
                                    "equal-to": [
                                        {
                                            "left-operand": "$dt-route-count",
                                            "right-operand": "1",
                                            "time-range": "30m"
                                        }
                                    ]
                                }
                            },
                            {
                                "term-name": "route-count-normal",
                                "then": {
                                    "status": {
                                        "color": "green",
                                        "message": "Route count of $table-name of $address-family of $route-table-type is ($route-count) normal"
                                    }
                                }
                            }
                        ],
                        "trigger-name": "fib-route-count"
                    }
                ],
                "variable": [
                    {
                        "description": "address-family names to monitor, regular expression, eg 'Internet|Internet6|MPLS|VPLS'",
                        "name": "route-address-family",
                        "type": "string",
                        "value": ".+"
                    },
                    {
                        "description": "Forwarding table's each protocol's route count threshold",
                        "name": "route-count-threshold",
                        "type": "int",
                        "value": "10000"
                    },
                    {
                        "description": "route table names to monitor, regular expression, eg 'default.inet|default.inet6|vpn_0.inet'",
                        "name": "route-table-name",
                        "type": "string",
                        "value": ".+"
                    },
                    {
                        "description": "route table types to monitor, regular expression, eg 'perm|intf|user'",
                        "name": "table-type",
                        "type": "string",
                        "value": ".+"
                    }
                ]
            },
                200)
            return obj
        if args[0] == 'https://1.1.1.1:8080/api/v1/playbook/forwarding-table-summary/?working=true':
            obj = MockResponse({
                "description": "Playbook monitors forwarding-table's each protocol's route count and notifies anomaly when route count is above static or dynamic threshold",
                "playbook-name": "forwarding-table-summary",
                "rules": [
                    "protocol.routesummary/check-fib-summary"
                ],
                "synopsis": "Forwarding table and protocol routes key performance indicators"
            }, 200)
            return obj
        elif args[0] == 'https://1.1.1.1:8080/api/v1/device-group/Core/?working=true':
            return MockResponse({"description": "testing",
                                 "device-group-name": "Core",
                                 "devices": ["vmx"],
                                 "native-gpb": {"ports": [22000]},
                                 "notification": {},
                                 "playbooks": ["eventd-debug-collection",
                                               "eventd-kpis-playbook",
                                               'automation-coredump-pb'],
                                 "reports": [],
                                 "variable": [{"@": {"changed-seconds": 1564722219},
                                               "instance-id": "HbEZ-instance",
                                               "playbook": "automation-coredump-pb",
                                               "rule": "x/y",
                                               "variable-value": []}]},
                                200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/device/vmx/?working=true':
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
                "variable": [{"@": {"changed-seconds": 1564722219},
                                               "instance-id": "HbEZ-instance",
                                               "playbook": "automation-coredump-pb",
                                               "rule": "x/y",
                                               "variable-value": []}],
                "vendor": {
                    "juniper": {
                        "operating-system": "junos"
                    }
                }
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/playbook/testing/?working=true':
            obj = MockResponse({
                "detail": "Playbook not found",
                "status": 404
            }, 404)
            return obj
        elif args[0] == 'https://1.1.1.1:8080/api/v1/device/vmx/?working=true':
            return MockResponse({
                "authentication": {
                    "password": {
                        "password": "xxxx",
                        "username": "xxxx"
                    }
                },
                "device-id": "vmx",
                "host": "10.221.xxx.xxx",
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
        return MockResponse(None, 404)
