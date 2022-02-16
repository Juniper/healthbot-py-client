class UrlFor(object):
    def __init__(self, hbot):
        self.hbot = hbot
        self.url = hbot.url
        self.config_url = hbot.config_url
        self.grafana_url = hbot.grafana_url

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

    def device_group_list(self):
        return "{api}/device-group".format(api=self.config_url)

    def network_group(self, group):
        return "{api}/network-group/{group}".format(api=self.config_url, group=group)

    def network_groups(self):
        return "{api}/network-groups".format(api=self.config_url)

    def network_group_list(self):
        return "{api}/network-group".format(api=self.config_url)

    def topic(self, topic_name):
        return "{api}/topic/{topic_name}".format(api=self.config_url,
                                                 topic_name=topic_name)

    def rule(self, topic_name, rule_name):
        return "{api}/topic/{topic_name}/rule/{rule_name}".format(
            api=self.config_url, topic_name=topic_name, rule_name=rule_name)

    def topics(self):
        return "{api}/topics".format(api=self.config_url)

    def dg_measurements_list(self, device_id, device_group):
        return "{api}/data/database/table/?device_id={device_id}&device_group_name={dg_name}"\
            .format(api=self.url, device_id=device_id, dg_name=device_group)

    def dg_measurement_fields(self, device_id, device_group, table_name):
        return "{api}/data/database/table/column/?device_id={device_id}&device_group_name={dg_name}" \
               "&table_name={table_name}".format(api=self.url, device_id=device_id,
                                                 dg_name=device_group, table_name=table_name)

    def dg_measurement_tags(self, device_id, device_group, table_name):
        return "{api}/data/database/table/tags/?device_id={device_id}&device_group_name={dg_name}" \
               "&table_name={table_name}".format(api=self.url, device_id=device_id,
                                                 dg_name=device_group, table_name=table_name)

    def ng_measurements_list(self, network_group):
        return "{api}/data/database/table/?network_group_name={network_group}"\
            .format(api=self.url, network_group=network_group)

    def ng_measurement_fields(self, network_group, table_name):
        return "{api}/data/database/table/column/?network_group_name={network_group}&table_name={table_name}"\
            .format(api=self.url, network_group=network_group, table_name=table_name)

    def ng_measurement_tags(self, network_group, table_name):
        return "{api}/data/database/table/tags/?network_group_name={network_group}&table_name={table_name}"\
            .format(api=self.url, network_group=network_group, table_name=table_name)

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
            api=self.config_url, name=name)

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

    def data_store_schema(self, canvas_name, group_name="grafana"):
        "/graph-management/canvas?name=a1"
        return "{api}/data-store/grafana/?key={canvas_name}"\
            .format(api=self.config_url, group_name=group_name, canvas_name=canvas_name)

    def grafana_get_dashboard(self, dashboard_uid):
        return "{grafana_url}/dashboards/uid/{dashboard_uid}"\
            .format(grafana_url=self.grafana_url, dashboard_uid=dashboard_uid)

    def grafana_update_dashboard(self):
        return "{grafana_url}/dashboards/db".format(grafana_url=self.grafana_url)

    def grafana_delete_dashboard(self,dashboard_uid):
        return "{grafana_url}/dashboards/uid/{dashboard_uid}".\
            format(grafana_url=self.grafana_url, dashboard_uid=dashboard_uid)

    def grafana_home_dashboard(self):
        return "{grafana_url}/dashboards/home".format(grafana_url=self.grafana_url)

    def deployment(self):
        return "{api}/deployment".format(api=self.config_url)

    def snmp_notifications(self):
        return "{api}/ingest/snmp-notification".format(api=self.config_url)

