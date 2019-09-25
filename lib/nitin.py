from jnpr.healthbot import HealthBotClient
hb = HealthBotClient('10.102.245.137', 'root', 'Embe1mpls')

from jnpr.healthbot import PlayBookInstanceBuilder
pbb = PlayBookInstanceBuilder(hb, playbook='system-kpis-playbook', instance='HbEZ-instance1', device_group_name='nitin')
# var = pbb.rule_variables["system.storage/check-storage"]
# var.storage_usage_high_threshold=100000
pbb.apply()
hb.commit()


import requests




# def create_playbook_instance(playbookname,instance,device_group):
#     try:
#         pbb = PlayBookInstanceBuilder(hb, playbook=playbookname, instance=instance, device_group_name=device_group)
#         # print(pbb.apply())
#         print(pbb.delete())
#         hb.commit()
#     except requests.exceptions.HTTPError as e:
#         print(e)
#
#
# create_playbook_instance(playbookname="system-kpis-playbook",instance="inst",device_group="g1")
#
# create_playbook_instance(playbookname="system-kpis-playbook",instance="inst1",device_group="g1")

from pprint import pprint
# hb = HealthBotClient('10.209.7.33', 'regress', 'MaRtInI')
# hb = HealthBotClient('10.221.134.177', 'root', 'root')
#
#
# scedulerSchema = hb.settings.scheduler.get(name="s1")
# print(scedulerSchema)
# scedulerSchema.end_time = '2019-10-11T10:30:00Z'
# hb.settings.scheduler.update(schema=scedulerSchema)

# from jnpr.healthbot import CaProfileSchema
# ca_prof_schema = CaProfileSchema(certificate_authority_crt='abc.crt', name='hbez')
# hb.settings.security.ca_profile.add(ca_prof_schema)

# pprint(hb.profile.ca_profile.get())

# from jnpr.healthbot import DeviceSchema
# ds = DeviceSchema(device_id='demo', host='10.221.136.140',
#                   authentication={"password": {"password": "MaRtInI", "username": "regress"}})
# # print(hb.device.add(schema=ds))
#
# print(hb.device.add(device_id='demo1', system_id='HbEZ', host='10.221.136.140',  i_agent={"port":830}))
#
# from jnpr.healthbot import DeviceGroupSchema
# dgs = DeviceGroupSchema(device_group_name="nitin", devices=['demo1'])
# print(hb.device_group.add(dgs))
# print(hb.commit())
#
# #
# # print(hb.device.get('demo1'))
# from jnpr.healthbot import PlayBookInstanceBuilder
# pbb = PlayBookInstanceBuilder(hb, playbook='system-kpis-playbook', instance='HbEZ-instance1', device_group_name='nitin')
# # # var = pbb.rule_variables["system.storage/check-storage"]
# # # var.storage_usage_high_threshold=100000
# pbb.apply()
# print(hb.commit(rollback_on_error=True))
import requests
requests.put()
# pbb = PlayBookInstanceBuilder(hb, 'forwarding-table-summary', 'HbEZ-instance', 'edge')
# pbb.apply()

# pbb.delete()
# hb.commit()

# # pprint(hb.device.get_ids())

#
# ds = DeviceSchema(device_id='demo',host='1.1.1.1',i_agent={"port":830},open_config={"port":123456})
# print(hb.device.add(schema=ds))
# ds = DeviceSchema(device_id='demo',host='1.1.1.1',i_agent={"port":830},open_config={"port":123})
# print(hb.device.add(schema=ds))

# schemaObj = hb.device.get('vmx')
# schemaObj.system_id = 'changed description'
# hb.device.update(schemaObj)
# pprint(hb.device.get_facts('vmx'))
# pprint(hb.device.get_facts())
# pprint(hb.device.get())
#

# #
# ds = DeviceSchema(device_id='demo', host='10.221.136.140',
#                   authentication={"password": {"password": "MaRtInI", "username": "regress"}})
# print(hb.device.add(schema=ds))
# hb.commit()
#
# dev = hb.device.get('demo')
# pprint(dev)
#
# dev.system_id = None
# print(hb.device.update(dev))
#
# hb.device.update(device_id="demo", host='10.221.136.140', system_id="test:HbEZ")
# dev = hb.device.get('demo')
# pprint(dev)
# print(hb.commit())
# print(hb.rollback())
#
# print(hb.device)
#
# from jnpr.healthbot import DeviceGroupSchema
# dgs = DeviceGroupSchema(device_group_name="edge", devices=['demo'])
# # dgs.description="All devices on the edge"
# print(hb.device_group.add(dgs))
# hb.commit()
#
# print(hb.device.delete('demo'))
# print(hb.device.delete('demo', True))
# print(hb.device_group.delete('edge'))
#
# from jnpr.healthbot import DeviceGroupSchema
# # dgs = DeviceGroupSchema()
# dgs = DeviceGroupSchema(device_group_name="edge")
# dgs.devices = ['demo']
# print(hb.device_group.add(device_group_name="edge", description="All devices on the edge", devices=['demo']))
# hb.commit()
#
# print(hb.device_group.get('edge'))
# print(hb.device_group.get())
#
# dgs = hb.device_group.get('real')
# pprint(dgs)
# hb.device.delete('avro', force=True)
# from jnpr.healthbot import DevicegroupSchemaLogging
# logSchema = DevicegroupSchemaLogging('warn')
# hb.device_group.update(device_group_name='edge', logging=logSchema)
# dgs.devices = ['vmx']
# hb.device_group.update(dgs)
#
# print(hb.network_group.add(network_group_name="HbEZ"))
# obj = hb.network_group.get(network_group_name="HbEZ")
# obj.description = "HbEZ example"
# hb.network_group.update(obj)
# print(hb.network_group.get())
# print(hb.network_group.delete(network_group_name="HbEZ"))
#
# print(hb.rule.get('linecard.ospf', 'check-ddos-statistics'))
#
# from jnpr.healthbot import RuleSchema
# rs = RuleSchema(rule_name="hbez-fpc-heap-utilization")
# rs.description = "HealthBot EZ example"
# rs.synopsis = "Using python client for demo"
# rs.sensor = [{'description': 'Monitors FPC buffer, heap and cpu utilization',
#              'iAgent': {'file': 'fpc-utilization.yml',
#                         'frequency': '30s',
#                         'table': 'FPCCPUHEAPutilizationTable'},
#              'sensor_name': 'fpccpuheaputilization'}]
# rs.field = [{'constant': {'value': '{{fpc-buffer-usage-threshold}}'},
#             'description': 'This field is for buffer usage threshold',
#             'field_name': 'linecard-buffer-usage-threshold'},
#            {'constant': {'value': '{{fpc-cpu-usage-threshold}}'},
#             'description': 'This field is for linecard cpu usage threshold',
#             'field_name': 'linecard-cpu-usage-threshold'},
#            {'constant': {'value': '{{fpc-heap-usage-threshold}}'},
#             'description': 'This field is for linecard heap usage threshold',
#             'field_name': 'linecard-heap-usage-threshold'}]
# rs.keys = ['slot']
# rs.variable = [{'description': 'Linecard Buffer Memory usage threshold value',
#                'name': 'fpc-buffer-usage-threshold',
#                'type': 'int',
#                'value': '80'},
#               {'description': 'Linecard CPU usage threshold value',
#                'name': 'fpc-cpu-usage-threshold',
#                'type': 'int',
#                'value': '80'},
#               {'description': 'Linecard Heap Memory usage threshold value',
#                'name': 'fpc-heap-usage-threshold',
#                'type': 'int',
#                'value': '80'}]
# rs.trigger = [{'description': 'Sets health based on linecard buffer memory',
#               'frequency': '60s',
#               'synopsis': 'Linecard buffer memory kpi',
#               'term': [{'term_name': 'is-buffer-memory-utilization-greater-than-threshold',
#                         'then': {'status': {'color': 'red',
#                                             'message': 'FPC buffer memory '
#                                                        'utilization '
#                                                        '($memory-buffer-utilization) '
#                                                        'is over threshold '
#                                                        '($linecard-buffer-usage-threshold)'}},
#                         'when': {'greater_than': [{'left_operand': '$memory-buffer-utilization',
#                                                    'right_operand': '$linecard-buffer-usage-threshold'}]}},
#                        {'term_name': 'buffer-utilization-less-than-threshold',
#                         'then': {'status': {'color': 'green'}}}],
#               'trigger_name': 'fpc-buffer-memory-utilization'},
#              {'description': 'Sets health based on linecard cpu utilization',
#               'frequency': '60s',
#               'synopsis': 'Linecard cpu utilization kpi',
#               'term': [{'term_name': 'is-cpu-utilization-greater-than-80',
#                         'then': {'status': {'color': 'red',
#                                             'message': 'FPC CPU utilization '
#                                                        '($cpu-total) is over '
#                                                        'threshold '
#                                                        '($linecard-cpu-usage-threshold)'}},
#                         'when': {'greater_than': [{'left_operand': '$cpu-total',
#                                                    'right_operand': '$linecard-cpu-usage-threshold',
#                                                    'time_range': '180s'}]}},
#                        {'term_name': 'cpu-utilization-less-than-threshold',
#                         'then': {'status': {'color': 'green'}}}],
#               'trigger_name': 'fpc-cpu-utilization'},
#              {'description': 'Sets health based on linecard heap memory '
#                              'utilization',
#               'frequency': '60s',
#               'synopsis': 'Linecard heap memory kpi',
#               'term': [{'term_name': 'is-heap-memory-utilization-greater-than-threshold',
#                         'then': {'status': {'color': 'red',
#                                             'message': 'FPC heap memory '
#                                                        'utilization '
#                                                        '($memory-heap-utilization) '
#                                                        'is over threshold '
#                                                        '($linecard-heap-usage-threshold)'}},
#                         'when': {'greater_than': [{'left_operand': '$memory-heap-utilization',
#                                                    'right_operand': '$linecard-heap-usage-threshold'}]}},
#                        {'term_name': 'heap-memory-utilization-less-than-threshold',
#                         'then': {'status': {'color': 'green'}}}],
#               'trigger_name': 'fpc-heap-memory-utilization'}]
#
# print(hb.rule.add('hbez', schema=rs))
#
# obj = hb.rule.get(topic_name='hbez', rule_name="hbez-fpc-heap-utilization")
# obj.description = "HbEZ example"
# hb.rule.update('hbez', obj)
# hb.rule.delete(topic_name='hbez', rule_name="hbez-fpc-heap-utilization")
#
# print(hb.rule.get('linecard.statistics'))
# print(hb.topic.get('linecard.ospf'))
#
# from jnpr.healthbot import RetentionPolicySchema
#
# rps = RetentionPolicySchema(retention_policy_name='HbEZ-testing1')
# hb.settings.retention_policy.add(rps)
#
# rps = RetentionPolicySchema(retention_policy_name='HbEZ-testing2')
# hb.settings.retention_policy.add(rps)
#
# print(hb.settings.retention_policy)
#
# from jnpr.healthbot import SchedulerSchema
# sc = SchedulerSchema(name='HbEZ-schedule', repeat={'every': 'week'}, start_time="2019-07-22T05:32:23Z")
# hb.settings.scheduler.add(sc)



#
# from jnpr.healthbot import DestinationSchema
# ds = DestinationSchema(name='HbEZ-destination', email={'id': 'nitinkr@juniper.net'})
# hb.settings.destination.add(ds)
#
# from jnpr.healthbot import ReportSchema
# rs = ReportSchema(name="HbEZ-report", destination=['HbEZ-destination'], format="html", schedule=["HbEZ-schedule"])
# hb.settings.report.add(rs)
#
from jnpr.healthbot.modules.playbooks import PlayBookInstanceBuilder
#
# case where we dont need to set any variable
# pbb = PlayBookInstanceBuilder(hb, 'forwarding-table-summary', 'HbEZ-instance', 'edge')
# pbb = PlayBookInstanceBuilder(hb, 'icmp-probe', 'HbEZ-instance', 'edge')
# print(pbb.apply())
#
# from jnpr.healthbot.modules.playbooks import PlayBookInstanceBuilder
#
# pbb = PlayBookInstanceBuilder(hb, 'forwarding-table-summary', 'HbEZ-instance', 'Core')
#
# variable = pbb.rule_variables["protocol.routesummary/check-fib-summary"]
#
#
# variable.route_address_family = 'pqr'
# variable.route_count_threshold = 100
#
# # Apply variable to given device(s)
# pbb.apply(device_ids=['vmx'])
#
# #clear all the variable if you want to set it something else for group or other device(s)
# pbb.clear()
#
# variable = pbb.rule_variables["protocol.routesummary/check-fib-summary"]
# variable.route_address_family = 'abc'
# variable.route_count_threshold = 200
#
# pbb.apply()

#
# from jnpr.healthbot import HealthBotClient
# from jnpr.healthbot import DeviceSchema
# from pprint import pprint
#
# hb = HealthBotClient('10.221.134.177', 'root', 'root')
#
# pbb = PlayBookInstanceBuilder(hb, playbook='bgp-route-hijack-detection', instance='HbEZ-instance2',
#                               device_group_name='g1')
# # print(pbb.apply())
# pbb.delete()
# hb.commit()

# rs.field.append({'field-name': 'check',
#                        'sensor': [{'data-if-missing': {'value': 'check'},
#                                    'path': '/arp-information/ipv4/neighbors/neighbor/@ip',
#                                    'sensor-name': 'sensor1',
#                                    'where': [{'query': '/arp-information/ipv4/neighbors/neighbor/@ip ''== 12'}],
#                                    }],
#                        'type': 'string'})
#
# print(hb.rule.update('hbez', schema=rs))
# hb.commit()
# hb.commit()
# from jnpr.healthbot import SchedulerSchema
# sc = SchedulerSchema(name='HbEZ-schedule', repeat={'every': 'week'}, start_time="2019-07-22T05:32:23Z")
# sc.input = '10.221.136.116'
# hb.settings.scheduler.add(name='HbEZ-schedule', repeat={'every': 'week'}, start_time="2019-07-22T05:32:23Z")
# print(hb.version)
# ds = DeviceSchema(device_id='demo',
#                   host='10.221.139.212',
#                   i_agent={"port": 830},
#                   )

# print(hb.device.update(device_id='demo', host='10.221.139.212',       open_config={"port": 830}))
# print(hb.device.update(device_id='demo', host='10.221.139.212', system_id="HbEZ"))

# pbb = PlayBookInstanceBuilder(hb, playbook='system-kpis-playbook', instance='HbEZ-instance1', device_group_name='Core')
# var = pbb.rule_variables["system.storage/check-storage"]
# var.storage_usage_high_threshold=100000

# pbb = PlayBookInstanceBuilder(hb, 'forwarding-table-summary', 'HbEZ-instance', 'Core')
# # variable = pbb.rule_variables["protocol.routesummary/check-fib-summary"]
# pbb.apply()
# hb.commit()
# hb.device.update(device_id="demo", host='10.221.139.212', system_id="test:HbEZ")

