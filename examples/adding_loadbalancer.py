# Settings --> Deployment --> Loadbalancer
# Equivalant to GUI: https://<IP>:8080/deployment-management/deploy

from jnpr.healthbot import HealthBotClient

DEPLOYMENT_ENDPOINT = "/deployment"

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'

with HealthBotClient(ip, gui_username, gui_password, port=8080) as hb:
    deployment_url = hb.config_url + DEPLOYMENT_ENDPOINT

    # Setting loadbalancer IP
    load_balancer_payload = \
        {
            "deployment": {
                "kubernetes": {
                    "loadbalancer": {
                        "snmp-proxy": {
                            "virtual-ip-address": "1.1.1.1"          # Replace your IP here
                        }
                    }
                }
            }
        }

    response = hb.api.put(deployment_url,
                          json=load_balancer_payload)
    if response.status_code != 200:
        print(response.text)
    response.raise_for_status()
    hb.commit()

    # Getting the value set for loadbalancer
    response = hb.api.get(deployment_url)
    response_json = response.json()
    print(response_json)
