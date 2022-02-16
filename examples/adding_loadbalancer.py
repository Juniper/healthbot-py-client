# Settings --> Deployment --> Loadbalancer
# Equivalant to GUI: https://<IP>:8080/deployment-management/deploy

from jnpr.healthbot import HealthBotClient

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'

with HealthBotClient(ip, gui_username, gui_password, port=8080) as hb:
    # Adding a loadbalancer IP
    hb.settings.deployment.add(ip="1.1.1.1")
    hb.commit()

    # Updating the loadbalancer IP
    hb.settings.deployment.update(ip="1.1.1.2")
    hb.commit()

    # Getting the configured loadbalancer IP
    print(hb.settings.deployment.get())

    # Deleting the configured IP
    hb.settings.deployment.delete()
    hb.commit()
