import unittest
from nose.plugins.attrib import attr

from mock import patch, PropertyMock

from jnpr.healthbot import HealthBotClient
from jnpr.healthbot.modules.rules import RuleSchema
from requests.models import Response
from . import _mock_user_login

@attr('unit')
class TestRules(unittest.TestCase):

    @patch('jnpr.healthbot.healthbot.requests.Session')
    @patch('jnpr.healthbot.swagger.api.authentication_api.AuthenticationApi.user_login')
    def setUp(self, mock_user_login, mock_request):
        self.mock_user_login = _mock_user_login
        self.mock_request = mock_request
        with patch('jnpr.healthbot.healthbot.HealthBotClient.version',
                   new_callable=PropertyMock) as mock_ver:
            with patch('jnpr.healthbot.healthbot.HealthBotClient.config_url',
                       new_callable=PropertyMock) as mock_cnf:
                mock_ver.return_value = '4.0.0'
                mock_cnf.return_value = "https://1.1.1.1:8080/api/v2/config"
                self.conn = HealthBotClient(
                    server='1.1.1.1',
                    user='test',
                    password='password123').open()

    def tearDown(self) -> None:
        self.conn.close()

    def test_add_rule(self):
        self.mock_request().get.side_effect = self._mock_manager
        rs = RuleSchema(rule_name="hbez-fpc-heap-utilization")
        rs.description = "HealthBot EZ example"
        rs.synopsis = "Using python client for demo"
        rs.sensor = [
            {
                'description': 'Monitors FPC buffer, heap and cpu utilization',
                'iAgent': {
                    'file': 'fpc-utilization.yml',
                    'frequency': '30s',
                    'table': 'FPCCPUHEAPutilizationTable'},
                'sensor_name': 'fpccpuheaputilization'}]
        rs.field = [{'constant': {'value': '{{fpc-buffer-usage-threshold}}'},
                     'description': 'This field is for buffer usage threshold',
                     'field_name': 'linecard-buffer-usage-threshold'},
                    {'constant': {'value': '{{fpc-cpu-usage-threshold}}'},
                     'description': 'This field is for linecard cpu usage threshold',
                     'field_name': 'linecard-cpu-usage-threshold'},
                    {'constant': {'value': '{{fpc-heap-usage-threshold}}'},
                     'description': 'This field is for linecard heap usage threshold',
                     'field_name': 'linecard-heap-usage-threshold'}]
        rs.keys = ['slot']
        rs.variable = [{'description': 'Linecard Buffer Memory usage threshold value',
                        'name': 'fpc-buffer-usage-threshold',
                        'type': 'int',
                        'value': '80'},
                       {'description': 'Linecard CPU usage threshold value',
                        'name': 'fpc-cpu-usage-threshold',
                        'type': 'int',
                        'value': '80'},
                       {'description': 'Linecard Heap Memory usage threshold value',
                        'name': 'fpc-heap-usage-threshold',
                        'type': 'int',
                        'value': '80'}]
        rs.trigger = [{'description': 'Sets health based on linecard buffer memory',
                       'frequency': '60s',
                       'synopsis': 'Linecard buffer memory kpi',
                       'term': [{'term_name': 'is-buffer-memory-utilization-greater-than-threshold',
                                 'then': {'status': {'color': 'red',
                                                     'message': 'FPC buffer memory '
                                                                'utilization '
                                                                '($memory-buffer-utilization) '
                                                                'is over threshold '
                                                                '($linecard-buffer-usage-threshold)'}},
                                 'when': {'greater_than': [{'left_operand': '$memory-buffer-utilization',
                                                            'right_operand': '$linecard-buffer-usage-threshold'}]}},
                                {'term_name': 'buffer-utilization-less-than-threshold',
                                 'then': {'status': {'color': 'green'}}}],
                       'trigger_name': 'fpc-buffer-memory-utilization'},
                      {'description': 'Sets health based on linecard cpu utilization',
                       'frequency': '60s',
                       'synopsis': 'Linecard cpu utilization kpi',
                       'term': [{'term_name': 'is-cpu-utilization-greater-than-80',
                                 'then': {'status': {'color': 'red',
                                                     'message': 'FPC CPU utilization '
                                                                '($cpu-total) is over '
                                                                'threshold '
                                                                '($linecard-cpu-usage-threshold)'}},
                                 'when': {'greater_than': [{'left_operand': '$cpu-total',
                                                            'right_operand': '$linecard-cpu-usage-threshold',
                                                            'time_range': '180s'}]}},
                                {'term_name': 'cpu-utilization-less-than-threshold',
                                 'then': {'status': {'color': 'green'}}}],
                       'trigger_name': 'fpc-cpu-utilization'},
                      {'description': 'Sets health based on linecard heap memory '
                                      'utilization',
                       'frequency': '60s',
                       'synopsis': 'Linecard heap memory kpi',
                       'term': [{'term_name': 'is-heap-memory-utilization-greater-than-threshold',
                                 'then': {'status': {'color': 'red',
                                                     'message': 'FPC heap memory '
                                                                'utilization '
                                                                '($memory-heap-utilization) '
                                                                'is over threshold '
                                                                '($linecard-heap-usage-threshold)'}},
                                 'when': {'greater_than': [{'left_operand': '$memory-heap-utilization',
                                                            'right_operand': '$linecard-heap-usage-threshold'}]}},
                                {'term_name': 'heap-memory-utilization-less-than-threshold',
                                 'then': {'status': {'color': 'green'}}}],
                       'trigger_name': 'fpc-heap-memory-utilization'}]

        self.assertTrue(self.conn.rule.add('external', schema=rs))

    def test_add_rule_without_schema(self):
        self.assertTrue(
            self.conn.rule.add(
                rule_name="hbez-fpc-heap-utilization",
                topic_name='test'))

    def test_schema_check(self):
        self.assertTrue(
            self.conn.rule.add(
                rule_name="hbez-fpc-heap-utilization",
                topic_name='test'))

    def test_get_rule(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.rule.get(
            topic_name='external',
            rule_name="hbez-fpc-heap-utilization")
        self.assertEqual(ret.description, 'HealthBot EZ example')

    def test_get_rules(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.rule.get(
            topic_name='external')
        self.assertEqual(ret[0].rule_name, 'interface-info')

    def test_delete_rule(self):
        ret = self.conn.rule.delete(
            topic_name='external',
            rule_name="hbez-fpc-heap-utilization")
        self.assertTrue(ret)
        self.assertEqual(self.mock_request().mock_calls[2][0],
                         'delete')

    def test_update_rule(self):
        self.mock_request().get.side_effect = self._mock_manager
        ret = self.conn.rule.get(
            topic_name='external',
            rule_name="hbez-fpc-heap-utilization")
        ret.keys = ['slot']
        self.conn.rule.update(topic_name='external', schema=ret)
        self.assertEqual(
            self.mock_request().mock_calls[3][2]['json']['keys'],
            ['slot'])

    def test_get_topic(self):
        self.mock_request().get.side_effect = self._mock_manager
        topic = self.conn.topic.get(topic_name='external')
        self.assertEqual(topic.topic_name,
                         'external')

    def test_get_topics(self):
        self.mock_request().get.side_effect = self._mock_manager
        topics = self.conn.topic.get()
        self.assertEqual(topics[0].description,
                         'Monitors the chassis temperatures of whole chassis')

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

        if args[0] == 'https://1.1.1.1:8080/api/v2/config/topic/external/?working=true':
            obj = MockResponse({
                "rule": [
                    {
                        "field": [
                            {
                                "description": "admin status",
                                "field-name": "admin",
                                "sensor": [
                                    {
                                        "path": "admin",
                                        "sensor-name": "phyport"
                                    }
                                ],
                                "type": "string"
                            },
                            {
                                "field-name": "name",
                                "sensor": [
                                    {
                                        "path": "name",
                                        "sensor-name": "phyport"
                                    }
                                ],
                                "type": "string"
                            },
                            {
                                "description": "oper status",
                                "field-name": "oper",
                                "sensor": [
                                    {
                                        "path": "oper",
                                        "sensor-name": "phyport"
                                    }
                                ],
                                "type": "string"
                            }
                        ],
                        "keys": [
                            "name"
                        ],
                        "rule-name": "interface-info",
                        "variable": [
                            {
                                "name": "interface_name",
                                "type": "sensor-argument"
                            }
                        ]
                    }
                ],
                "sub-topics": [],
                "topic-name": "external"
            }, 200)
            return obj
        elif args[0] == 'https://1.1.1.1:8080/api/v2/config/topic/external/rule/hbez-fpc-heap-utilization/?working=true':
            obj = MockResponse({"description": "HealthBot EZ example",
                                "field": [{"constant": {"value": "{{fpc-buffer-usage-threshold}}"},
                                           "description": "This field is for buffer usage threshold",
                                           "field-name": "linecard-buffer-usage-threshold"},
                                          {"constant": {"value": "{{fpc-cpu-usage-threshold}}"},
                                           "description": "This field is for linecard cpu usage threshold",
                                           "field-name": "linecard-cpu-usage-threshold"},
                                          ],
                                "keys": ["slot"],
                                "rule-name": "hbez-fpc-heap-utilization",
                                "sensor": [{"description": "Monitors FPC buffer, heap and cpu utilization",
                                            "iAgent": {"file": "fpc-utilization.yml",
                                                       "frequency": "30s",
                                                       "table": "FPCCPUHEAPutilizationTable"},
                                            "sensor-name": "fpccpuheaputilization"}],
                                "synopsis": "Using python client for demo",
                                "trigger": [{"description": "Sets health based on linecard buffer memory",
                                             "frequency": "60s",
                                             "synopsis": "Linecard buffer memory kpi",
                                             "trigger-name": "fpc-buffer-memory-utilization"},
                                            {"description": "Sets health based on linecard cpu utilization",
                                             "frequency": "60s",
                                             "synopsis": "Linecard cpu utilization kpi",
                                             "trigger-name": "fpc-cpu-utilization"},
                                            ],
                                "variable": [{"description": "Linecard Buffer Memory usage threshold value",
                                              "name": "fpc-buffer-usage-threshold",
                                              "type": "int",
                                              "value": "80"}]},
                               200)
            return obj
        elif args[0] == 'https://1.1.1.1:8080/api/v2/config/topics':
            return MockResponse({
                "topic": [
                    {
                        "description": "Monitors the chassis temperatures of whole chassis",
                        "topic-name": "external",
                        "rule": [{"description": "HealthBot EZ example",
                                  "field": [{"constant": {"value": "{{fpc-buffer-usage-threshold}}"},
                                             "description": "This field is for buffer usage threshold",
                                             "field-name": "linecard-buffer-usage-threshold"},
                                            {"constant": {"value": "{{fpc-cpu-usage-threshold}}"},
                                             "description": "This field is for linecard cpu usage threshold",
                                             "field-name": "linecard-cpu-usage-threshold"},
                                            ],
                                  "keys": ["slot"],
                                  "rule-name": "hbez-fpc-heap-utilization",
                                  "sensor": [{"description": "Monitors FPC buffer, heap and cpu utilization",
                                              "iAgent": {"file": "fpc-utilization.yml",
                                                         "frequency": "30s",
                                                         "table": "FPCCPUHEAPutilizationTable"},
                                              "sensor-name": "fpccpuheaputilization"}],
                                  "synopsis": "Using python client for demo",

                                  "trigger": [{"description": "Sets health based on linecard buffer memory",
                                               "frequency": "60s",
                                               "synopsis": "Linecard buffer memory kpi",
                                               "trigger-name": "fpc-buffer-memory-utilization"},
                                              {"description": "Sets health based on linecard cpu utilization",
                                               "frequency": "60s",
                                               "synopsis": "Linecard cpu utilization kpi",
                                               "trigger-name": "fpc-cpu-utilization"},
                                              ],
                                  "variable": [{"description": "Linecard Buffer Memory usage threshold value",
                                                "name": "fpc-buffer-usage-threshold",
                                                "type": "int",
                                                "value": "80"}]}]}]}, 200)
        return MockResponse(None, 404)
