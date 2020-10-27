class UrlFor(object):
    def __init__(self, hbot):
        self.hbot = hbot
        self.url = hbot.url
        self.config_url = hbot.config_url

    def system_details(self):
        return "{api}/system-details".format(api=self.url)

    def device(self, device_id=None):
        if device_id is not None:
            return "{api}/device/{device_id}".format(
                api=self.config_url, device_id=device_id)
        else:
            return "{api}/device/".format(
                api=self.config_url)

    def device_facts(self, device_id):
        return "{api}/device/{device_id}/facts".format(
            api=self.config_url, device_id=device_id)

    def devices(self):
        return "{api}/devices".format(api=self.config_url)

    def devices_facts(self):
        return "{api}/devices/facts".format(api=self.config_url)

    def device_group(self, group):
        return "{api}/device-group/{group}".format(api=self.config_url, group=group)

    def device_groups(self):
        return "{api}/device-groups".format(api=self.config_url)

    def network_group(self, group):
        return "{api}/network-group/{group}".format(api=self.config_url, group=group)

    def network_groups(self):
        return "{api}/network-groups".format(api=self.config_url)

    def topic(self, topic_name):
        return "{api}/topic/{topic_name}".format(api=self.config_url,
                                                 topic_name=topic_name)

    def rule(self, topic_name, rule_name):
        return "{api}/topic/{topic_name}/rule/{rule_name}".format(
            api=self.config_url, topic_name=topic_name, rule_name=rule_name)

    def topic(self, topic_name):
        return "{api}/topic/{topic_name}".format(
            api=self.config_url, topic_name=topic_name)

    def topics(self):
        return "{api}/topics".format(api=self.config_url)

    def playbook(self, playbook_name):
        return "{api}/playbook/{playbook_name}".format(
            api=self.config_url, playbook_name=playbook_name)

    def playbooks(self):
        return "{api}/playbooks".format(api=self.config_url)

    def health(self):
        return "{api}/health".format(api=self.url)

    def device_health(self, device_id):
        return "{api}/health-tree/{device_id}".format(
            api=self.url, device_id=device_id)

    def device_group_health(self, device_group_name):
        return "{api}/health-tree/device-group/{device_group_name}".format(
            api=self.url, device_group_name=device_group_name)

    def network_group_health(self, network_group_name):
        return "{api}/health-tree/network-group/{network_group_name}".format(
            api=self.url, network_group_name=network_group_name)

    def table(self):
        return "{api}/data/database/table".format(api=self.url)

    def notification(self, notification_name):
        return "{api}/notification/{notification_name}".format(
            api=self.config_url, notification_name=notification_name)

    def notifications(self):
        return "{api}/notifications".format(api=self.config_url)

    def retention_policy(self, retention_policy_name):
        return "{api}/retention-policy/{retention_policy_name}".format(
            api=self.config_url, retention_policy_name=retention_policy_name)

    def retention_policies(self):
        return "{api}/retention-policies".format(api=self.config_url)

    def scheduler(self, name):
        return "{api}/system-settings/scheduler/{name}".format(
            api=self.config_url, name=name)

    def schedulers(self):
        return "{api}/system-settings/schedulers".format(api=self.config_url)

    def destination(self, name):
        return "{api}/system-settings/report-generation/destination/{name}".format(
            api=self.config_url, name=name)

    def destinations(self):
        return "{api}/system-settings/report-generation/destinations".format(
            api=self.config_url)

    def report(self, name):
        return "{api}/system-settings/report-generation/report/{name}".format(
            api=self.config_url, name=name)

    def reports(self):
        return "{api}/system-settings/report-generation/reports".format(
            api=self.config_url)

    def services_device_group(self, device_group_name=None):
        if device_group_name is None:
            return "{api}/services/device-group/".format(api=self.config_url)
        else:
            return "{api}/services/device-group/{device_group_name}".format(
                api=self.config_url, device_group_name=device_group_name)

    def helper_files(self, name):
        return "{api}/files/helper-files/{name}".format(
            api=self.url, name=name)

    def ca_profile(self, name):
        return "{api}/profile/security/ca-profile/{name}".format(
            api=self.config_url, name=name)

    def ca_profiles(self):
        return "{api}/profile/security/ca-profiles".format(api=self.config_url)

    def local_certificate(self, name):
        return "{api}/profile/security/local-certificate/{name}".format(
            api=self.config_url, name=name)

    def local_certificates(self):
        return "{api}/profile/security/local-certificates".format(api=self.config_url)

    def ssh_key_profile(self, name):
        return "{api}/profile/security/ssh-key-profile/{name}".format(
            api=self.config_url, name=name)

    def ssh_key_profiles(self):
        return "{api}/profile/security/ssh-key-profiles".format(api=self.config_url)
