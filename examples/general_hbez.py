from jnpr.healthbot import HealthBotClient
from pprint import pprint
from jnpr.healthbot import DeviceGroupSchema

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'

with HealthBotClient(ip, gui_username, gui_password, port=8080) as hb:

    print(hb.version)
    pprint(hb.device.get_ids())
    pprint(hb.device_group.get())

    # Handling devices
    pprint(hb.device.get_ids())
    pprint(hb.device.add("test", "1.1.1.1", "admin", "Admin@123"))
    pprint(hb.device.add("teakwood", "1.1.1.1", "admin", "Admin@123"))
    hb.commit()
    pprint(hb.device.get_ids())
    pprint(hb.device.delete("test"))
    hb.commit()
    pprint(hb.device.get_ids())
    pprint(hb.device.get('test'))

    schemaObj = hb.device.get('test')
    schemaObj.description = 'changed description'
    hb.device.update(schemaObj)
    pprint(hb.device.get('test'))
    pprint(hb.device.get_facts())
    pprint(hb.device.health('test'))
    pprint(hb.device.health('svl1r'))

    # Handling device-groups
    pprint(hb.device_group.get())
    dgs = DeviceGroupSchema(device_group_name="edge",
                            description="All devices on the edge",
                            devices=['test'])
    hb.device_group.add(dgs)
    hb.commit()
    pprint(hb.device_group.get("edge"))
    hb.device_group.delete("egde")
    hb.commit()
    pprint(hb.device_group.get("edge"))

    dgs = hb.device_group.get('edge')
    dgs.devices.append("teakwood")
    hb.device_group.update(dgs)
    hb.commit()
    print(hb.device_group.get('edge'))

    dgs = hb.device_group.get('edge')
    dgs.devices.remove("teakwood")
    hb.device_group.update(dgs)
    hb.commit()
    print(hb.device_group.get('edge'))

    # Handling playbooks
    pprint(hb.playbook.get())
    pprint(hb.playbook.get('linecard-kpis-playbook'))

    pprint(hb.rule.get('linecard.ospf', 'check-ddos-statistics'))







