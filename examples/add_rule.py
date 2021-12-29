
from jnpr.healthbot import HealthBotClient
from jnpr.healthbot.modules.rules import RuleSchema
from jnpr.healthbot.swagger.models.rule_schema_field import RuleSchemaField
from jnpr.healthbot.swagger.models.rule_schema_constant import RuleSchemaConstant
from jnpr.healthbot.swagger.models.rule_schema_function import RuleSchemaFunction

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'


with HealthBotClient(ip, gui_username, gui_password, port=8080) as hb:
    rs = RuleSchema(rule_name="hbez-fpc-heap-utilization")
    rs.description = "HealthBot EZ example"
    rs.synopsis = "Using python client for demo"
    rs.sensor = [{'description': 'Monitors FPC buffer, heap and cpu utilization',
                  'iAgent': {'file': 'fpc-utilization.yml',
                             'frequency': '30s',
                             'table': 'FPCCPUHEAPutilizationTable'},
                  'sensor-name': 'fpccpuheaputilization'}]
    rs.field = [RuleSchemaField(constant=RuleSchemaConstant(value='{{fpc-buffer-usage-threshold}}'),
                                description='This field is for buffer usage threshold',
                                field_name='linecard-buffer-usage-threshold'),]
    rs.keys = ['slot']
    rs.variable = [{'description': 'Linecard Buffer Memory usage threshold value',
                    'name': 'fpc-buffer-usage-threshold',
                    'type': 'int',
                    'value': '80'}]
    rs.trigger = [
                  {'description': 'Sets health based on linecard heap memory '
                                  'utilization',
                   'frequency': '60s',
                   'synopsis': 'Linecard heap memory kpi',
                   'term': [{'term-name': 'is-heap-memory-utilization-greater-than-threshold',
                             'then': {'status': {'color': 'red',
                                                 'message': 'FPC heap memory '
                                                            'utilization '
                                                            '($memory-heap-utilization) '
                                                            'is over threshold '
                                                            '($linecard-heap-usage-threshold)'}},
                             'when': {'greater-than': [{'left-operand': '$memory-heap-utilization',
                                                        'right-operand': '$linecard-heap-usage-threshold'}]}},
                            {'term-name': 'heap-memory-utilization-less-than-threshold',
                             'then': {'status': {'color': 'green'}}}],
                   'trigger-name': 'fpc-heap-memory-utilization'}]

    rs.function = [
        RuleSchemaFunction(argument=[{"argument-name": "max_count","mandatory": [None]},
                                     {"argument-name": "min_count","mandatory": [None]}],
                           description=None, function_name="my_func1", method="diff_percentage",
                           path="diff-percentage.py")
        ]

    hb.rule.add('mytopic', schema=rs)
    hb.commit()

