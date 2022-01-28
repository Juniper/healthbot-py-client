from jnpr.healthbot import HealthBotClient

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'


with HealthBotClient(ip, gui_username, gui_password, port=8080) as hb:
    # We can upload rules/playbooks/udf python files (any kind of helper file) 
    file = "/<path>/myrule.rule"
    hb.rule.upload_rule_file(file)
    hb.commit()
