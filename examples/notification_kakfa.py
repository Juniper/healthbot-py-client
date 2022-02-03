from jnpr.healthbot import HealthBotClient

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'


with HealthBotClient(ip, gui_username, gui_password, port=8080) as hb:
    hb.settings.notification.add(notification_name="sample", description=None, emails=None, microsoft_teams=None,
                                 slack=None, http_post=None, kafka_publish={'bootstrap-servers': ['hbkafka:9094'],
                                                                                  'use-hash-partitioner': False})
    hb.device_group.add(device_group_name="edge", description="All devices on the edge", devices=['demo'],
                        notification={'major': ["sample"], 'minor': ["sample"], 'normal': ["sample"]})

    hb.commit()
    print(hb.settings.notification.get(notification_name="sample"))
    print(hb.device_group.get(device_group_name="edge"))
