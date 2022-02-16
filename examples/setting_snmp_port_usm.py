# Settings --> Ingest --> Snmp Notification
from jnpr.healthbot.swagger.models.snmp_notification_schema import SnmpNotificationSchema
from jnpr.healthbot.swagger.models.snmpnotification_schema_snmpnotification import SnmpnotificationSchemaSnmpnotification
from jnpr.healthbot.swagger.models.snmpnotification_schema_snmpnotification_v3 import SnmpnotificationSchemaSnmpnotificationV3

from jnpr.healthbot import HealthBotClient

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'

with HealthBotClient(ip, gui_username, gui_password, port=8080) as hb:

    # Adding SNMP notification settings wit USM
    schema = SnmpNotificationSchema(
        snmp_notification=SnmpnotificationSchemaSnmpnotification(
            port=199,
            v3=SnmpnotificationSchemaSnmpnotificationV3(
                usm={
                    "users": [
                                {
                                    "authentication": {
                                        "passphrase": "Testing@123",
                                        "protocol": "SHA"
                                    },
                                    "privacy": {
                                        "passphrase": "Testing@123",
                                        "protocol": "AES"
                                    },
                                    "username": "snmp-collector"
                                },
                                {
                                    "authentication": {
                                        "passphrase": "Testing@123",
                                        "protocol": "MD5"
                                    },
                                    "privacy": {
                                        "passphrase": "Testing@123",
                                        "protocol": "AES256"
                                    },
                                    "username": "cisco-collector"
                                }
                            ]}
            )))
    hb.settings.snmp_notification.add(schema)
    hb.commit()

    # Getting the configured SNMP notification settings
    print(hb.settings.snmp_notification.get())

    # Updating the configured SNMP notification settings
    schema_new = SnmpNotificationSchema(
        snmp_notification=SnmpnotificationSchemaSnmpnotification(
            port=161,
            v3=SnmpnotificationSchemaSnmpnotificationV3(
                usm={
                    "users": [
                        {
                            "authentication": {
                                "passphrase": "Testing@123",
                                "protocol": "MD5"
                            },
                            "privacy": {
                                "passphrase": "Testing@123",
                                "protocol": "AES256"
                            },
                            "username": "cisco-collector"
                        }
                    ]}
            )))
    hb.settings.snmp_notification.update(schema_new)
    hb.commit()

    # Deleting the configured SNMP notification settings
    hb.settings.snmp_notification.delete()
    hb.commit()
