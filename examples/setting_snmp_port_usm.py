# Settings --> Ingest --> Snmp Notification


from jnpr.healthbot import HealthBotClient
SNMP_ENDPOINT = "/ingest/snmp-notification"

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'

with HealthBotClient(ip, gui_username, gui_password, port=8080) as hb:
    snmp_url = hb.config_url + SNMP_ENDPOINT

    # Adding snmp port only in Snmp Notification
    snmp_payload = \
        {
            "snmp-notification": {
                "port": 2029,           # Replace your port here
                "v3": {
                    "usm": {
                        "users": []
                    }
                }
            }
        }
    response = hb.api.put(hb.config_url + snmp_payload)
    if response.status_code != 200:
        print(response.text)
    response.raise_for_status()
    hb.commit()

    # Adding snmp port with usm in Snmp Notification
    snmp_payload = \
        {
            "snmp-notification": {
                "port": 2029,                                       # Replace your port here
                "v3": {
                    "usm": {
                        "users": [                                  # Replace values accordingly
                            {
                                "authentication-none": [
                                    "None"
                                ],
                                "privacy-none": [
                                    "None"
                                ],
                                "username": "root"
                            },
                            {
                                "authentication": {
                                    "passphrase": "12345678",
                                    "protocol": "MD5"
                                },
                                "privacy": {
                                    "passphrase": "12345678",
                                    "protocol": "DES1"
                                },
                                "username": "root1"
                            }
                        ]
                    }
                }
            }
        }
    response = hb.api.put(hb.config_url + snmp_payload)
    if response.status_code != 200:
        print(response.text)
    response.raise_for_status()
    hb.commit()

    # Getting the value set for Snmp Notification
    response = hb.api.get(snmp_url)
    response_json = response.json()
    print(response_json)
