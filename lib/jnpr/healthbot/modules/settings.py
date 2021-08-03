from jnpr.healthbot.modules.profiles import Security

from jnpr.healthbot.swagger.models.notification_schema import NotificationSchema
from jnpr.healthbot.swagger.models.retention_policy_schema import RetentionPolicySchema
from jnpr.healthbot.swagger.models.scheduler_schema import SchedulerSchema
from jnpr.healthbot.swagger.models.report_schema import ReportSchema
from jnpr.healthbot.swagger.models.destination_schema import DestinationSchema
from jnpr.healthbot.swagger.api.license_api import LicenseApi
from jnpr.healthbot.exception import SchemaError, NotFoundError

from jnpr.healthbot.modules import BaseModule
# from jnpr.healthbot import AutoGenClass

import logging
logger = logging.getLogger(__file__)


class Settings(object):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """

        self._hbot = hbot
        self.notification = Notification(hbot)
        self.retention_policy = RetentionPolicy(hbot)
        self.scheduler = Scheduler(hbot)
        self.report = Report(hbot)
        self.destination = Destination(hbot)
        self.security = Security(hbot)
        self.license = LicenseKeyManagement(hbot)


class Notification(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def get(self, notification_name: str = None, uncommitted: bool = True):
        """
        Get `NotificationSchema(s) <jnpr.healthbot.swagger.models.html#notificationschema>`_ for
        given notification name or list for all

        :param notification_name: ID of notification-name
        :param bool uncommitted: True includes fetches uncommitted changes,
            False restricts data set to only committed changes

        Example:
        ::

                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.settings.notification.get('xyz')

        :return: `NotificationSchema(s) <jnpr.healthbot.swagger.models.html#notificationschema>`_
        """
        if notification_name is not None:
            notification_url = self.hbot.urlfor.notification(notification_name)
            if uncommitted:
                notification_url += self.hbot.apiopt_candidate
            response = self.api.get(notification_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(response, NotificationSchema)
        else:
            notifications_url = self.hbot.urlfor.notifications()
            if uncommitted:
                notifications_url += self.hbot.apiopt_candidate
            response = self.api.get(notifications_url)
            response_json = response.json()
            if response.status_code != 200:
                logger.error(response.text)
                raise NotFoundError(response_json)
            existing_notifications = response_json['notification']
            notification_list = []
            for notification in existing_notifications:
                obj = self.hbot._create_schema(
                    notification, NotificationSchema)
                notification_list.append(obj)

            return notification_list

    def add(self, schema: NotificationSchema = None, **kwargs):
        """
        Add notification to HealthBot

        :param object schema: `NotificationSchema <jnpr.healthbot.swagger.models.html#notificationschema>`_
        :param object kwargs: key values, which can be used to create
            NotificationSchema
            Check `NotificationSchema <jnpr.healthbot.swagger.models.html#notificationschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import NotificationSchema, NotificationSchemaSlack

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                ns = NotificationSchema(notification_name='HbEZ-notification')
                ns.description = "example of adding notification via API"
                ns.slack = NotificationSchemaSlack(channel="HbEZ", url='http://testing')
                hb.settings.notification.add(ns)

        :returns: True when OK

        """
        if schema is None:
            schema = NotificationSchema(**kwargs)
        payload = self.hbot._create_payload(schema)
        notification_url = self.hbot.urlfor.notification(
            payload['notification-name'])
        response = self.api.post(notification_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def delete(self, notification_name: str):
        """
        Remove notification from settings

        :param str notification_name: The name of the notification to be deleted

        Example:
        ::
            hb.settings.notification.delete('xyz')
            hb.commit()

        :returns: True when OK
        """

        notification_url = self.hbot.urlfor.notification(notification_name)
        response = self.api.delete(notification_url)
        if response.status_code != 204:
            logger.error(response.text)
        response.raise_for_status()

        return True

    def update(self, schema: NotificationSchema = None, **kwargs):
        """
        Update `NotificationSchema <jnpr.healthbot.swagger.models.html#notificationschema>`_ for
        given NotificationSchema schema

        Passing Schema invoke `put` and kwargs `post`

        :param obj schema: `NotificationSchema <jnpr.healthbot.swagger.models.html#notificationschema>`_
        :param object kwargs: key values, which can be used to create
            RetentionPolicySchema
            Check `NotificationSchema <jnpr.healthbot.swagger.models.html#notificationschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schemaObj = hb.settings.notification.get('xyz')
                schemaObj.description = 'changed description'
                hb.settings.notification.update(schemaObj)

        :returns: True when OK
        """
        if schema is None:
            schema = NotificationSchema(**kwargs)
            call = self.api.post
        else:
            if not isinstance(schema, NotificationSchema):
                raise SchemaError(NotificationSchema)
            call = self.api.put
        payload = self.hbot._create_payload(schema)
        name = schema.notification_name
        notification_url = self.hbot.urlfor.notification(name)
        response = call(notification_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True


class RetentionPolicy(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def get(
            self,
            retention_policy_name: str = None,
            uncommitted=True):
        """
        Get `RetentionPolicySchema(s) <jnpr.healthbot.swagger.models.html#retentionpolicyschema>`_ for
        given retention policy name or list for all

        :param retention_policy_name: ID of retention-policy-name
        :param bool uncommitted: True includes fetches uncommitted changes,
            False restricts data set to only committed changes

        Example:
        ::
                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.settings.retention_policy.get('xyz')

                    # for all
                    print(hb.settings.retention_policy.get()

        :return: `RetentionPolicySchema(s) <jnpr.healthbot.swagger.models.html#retentionpolicyschema>`_
        """
        if retention_policy_name is not None:
            retention_policy_url = self.hbot.urlfor.retention_policy(
                retention_policy_name)
            if uncommitted:
                retention_policy_url += self.hbot.apiopt_candidate
            response = self.api.get(retention_policy_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(response, RetentionPolicySchema)
        else:
            notifications_url = self.hbot.urlfor.retention_policies()
            if uncommitted:
                notifications_url += self.hbot.apiopt_candidate
            response = self.api.get(notifications_url)
            response_json = response.json()
            if response.status_code != 200:
                logger.error(response.text)
                raise NotFoundError(response_json)
            existing_retention_policies = response_json['retention-policy']
            existing_retention_policies_list = []
            for retention_policy in existing_retention_policies:
                obj = self.hbot._create_schema(
                    retention_policy, RetentionPolicySchema)
                existing_retention_policies_list.append(obj)

            return existing_retention_policies_list

    def add(
            self,
            schema: RetentionPolicySchema = None,
            **kwargs):
        """
        Add notification to HealthBot

        :param object schema: `RetentionPolicySchema <jnpr.healthbot.swagger.models.html#retentionpolicyschema>`_
        :param object kwargs: key values, which can be used to create
            RetentionPolicySchema
            Check `RetentionPolicySchema <jnpr.healthbot.swagger.models.html#retentionpolicyschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import RetentionPolicySchema

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                rps = RetentionPolicySchema(retention_policy_name='HbEZ-rentention-policy')
                hb.settings.retention_policy.add(rps)

        :returns: True when OK

        """
        if schema is None:
            schema = RetentionPolicySchema(**kwargs)
        payload = self.hbot._create_payload(schema)
        retention_policy_url = self.hbot.urlfor.retention_policy(
            payload['retention-policy-name'])
        response = self.api.post(retention_policy_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def delete(self, retention_policy_name: str):
        """
        Remove notification from settings

        :param str retention_policy_name: The name of the retention policy to be deleted

        Example:
        ::
            hb.settings.retention_policy.delete('xyz')
            hb.commit()

        :returns: True when OK
        """

        retention_policy_url = self.hbot.urlfor.retention_policy(
            retention_policy_name)
        response = self.api.delete(retention_policy_url)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()

        return True

    def update(self, schema: RetentionPolicySchema = None, **kwargs):
        """
        Update `RetentionPolicySchema <jnpr.healthbot.swagger.models.html#retentionpolicyschema>`_ for
        given RetentionPolicySchema schema

        Passing Schema invoke `put` and kwargs `post`

        :param obj schema: `RetentionPolicySchema <jnpr.healthbot.swagger.models.html#retentionpolicyschema>`_
        :param object kwargs: key values, which can be used to create
            RetentionPolicySchema
            Check `RetentionPolicySchema <jnpr.healthbot.swagger.models.html#retentionpolicyschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schemaObj = hb.settings.retention_policy.get('xyz')
                schemaObj.description = 'changed description'
                hb.settings.retention_policy.update(schemaObj)

        :returns: True when OK
        """
        if schema is None:
            schema = RetentionPolicySchema(**kwargs)
            call = self.api.post
        else:
            if not isinstance(schema, RetentionPolicySchema):
                raise SchemaError(RetentionPolicySchema)
            call = self.api.put
        payload = self.hbot._create_payload(schema)
        name = schema.retention_policy_name
        retention_policy_url = self.hbot.urlfor.retention_policy(name)
        response = call(retention_policy_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True


class Scheduler(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def get(self, name: str = None, uncommitted: bool = True):
        """
        Get `SchedulerSchema(s) <jnpr.healthbot.swagger.models.html#schedulerschema>`_ for
        given scheduler name or list for all

        :param name: scheduler name
        :param bool uncommitted: True includes fetches uncommitted changes,
            False restricts data set to only committed changes

        Example:
        ::
                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.settings.scheduler.get('xyz')

                    # for all
                    print(hb.settings.scheduler.get()

        :return: `SchedulerSchema(s) <jnpr.healthbot.swagger.models.html#schedulerschema>`_
        """
        if name is not None:
            scheduler_url = self.hbot.urlfor.scheduler(name)
            if uncommitted:
                scheduler_url += self.hbot.apiopt_candidate
            response = self.api.get(scheduler_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(response, SchedulerSchema)
        else:
            schedulers_url = self.hbot.urlfor.schedulers()
            if uncommitted:
                schedulers_url += self.hbot.apiopt_candidate
            response = self.api.get(schedulers_url)
            response_json = response.json()
            if response.status_code != 200:
                logger.error(response.text)
                raise NotFoundError(response_json)
            existing_schedulers = response_json['scheduler']
            existing_schedulers_list = []
            for scheduler in existing_schedulers:
                obj = self.hbot._create_schema(scheduler, SchedulerSchema)
                existing_schedulers_list.append(obj)

            return existing_schedulers_list

    def add(self, schema: SchedulerSchema = None, **kwargs):
        """
        Add scheduler to HealthBot

        :param object schema: `SchedulerSchema <jnpr.healthbot.swagger.models.html#schedulerschema>`_
        :param object kwargs: key values, which can be used to create
            SchedulerSchema
            Check `SchedulerSchema <jnpr.healthbot.swagger.models.html#schedulerschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import SchedulerSchema

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                sc = SchedulerSchema(name='HbEZ', repeat={'every': 'week'},
                        start_time="2019-07-22T05:32:23Z")
                hb.settings.scheduler.add(sc)

        :returns: True when OK

        """
        if schema is None:
            schema = SchedulerSchema(**kwargs)
        payload = self.hbot._create_payload(schema)
        scheduler_url = self.hbot.urlfor.scheduler(payload['name'])
        response = self.api.post(scheduler_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def delete(self, name: str):
        """
        Remove notification from settings

        :param str name: The name of the scheduler to be deleted

        Example:
        ::
            hb.settings.scheduler.delete('xyz')
            hb.commit()

        :returns: True when OK
        """

        scheduler_url = self.hbot.urlfor.scheduler(name)
        response = self.api.delete(scheduler_url)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()

        return True

    def update(self, schema: SchedulerSchema = None, **kwargs):
        """
        Update `SchedulerSchema <jnpr.healthbot.swagger.models.html#schedulerschema>`_ for
        given scheduler schema

        Passing Schema invoke `put` and kwargs `post`

        :param obj schema: `SchedulerSchema <jnpr.healthbot.swagger.models.html#schedulerschema>`_
        :param object kwargs: key values, which can be used to create
            SchedulerSchema
            Check `SchedulerSchema <jnpr.healthbot.swagger.models.html#schedulerschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schemaObj = hb.settings.scheduler.get('xyz')
                schemaObj.description = 'changed description'
                hb.settings.scheduler.update(schemaObj)

        :returns: True when OK
        """
        if schema is None:
            schema = SchedulerSchema(**kwargs)
            call = self.api.post
        else:
            if not isinstance(schema, SchedulerSchema):
                raise SchemaError(SchedulerSchema)
            call = self.api.put
        payload = self.hbot._create_payload(schema)
        name = schema.name
        scheduler_url = self.hbot.urlfor.scheduler(name)
        response = call(scheduler_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True


class Destination(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def get(self, name: str = None, uncommitted: bool = True):
        """
        Get `DestinationSchema(s) <jnpr.healthbot.swagger.models.html#destinationschema>`_ for
        given destination name or list for all

        :param name: destination ID
        :param bool uncommitted: True includes fetches uncommitted changes,
            False restricts data set to only committed changes

        Example:
        ::

                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.settings.destination.get('xyz')

                    # for all
                    print(hb.settings.destination.get()

        :return: `DestinationSchema(s) <jnpr.healthbot.swagger.models.html#destinationschema>`_
        """
        if name is not None:
            destination_url = self.hbot.urlfor.destination(name)
            if uncommitted:
                destination_url += self.hbot.apiopt_candidate
            response = self.api.get(destination_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(response, DestinationSchema)
        else:
            destination_url = self.hbot.urlfor.destinations()
            if uncommitted:
                destination_url += self.hbot.apiopt_candidate
            response = self.api.get(destination_url)
            response_json = response.json()
            if response.status_code != 200:
                logger.error(response.text)
                raise NotFoundError(response_json)
            existing_destinations = response_json['destination']
            destinations_list = []
            for destination in existing_destinations:
                obj = self.hbot._create_schema(
                    destination, DestinationSchema)
                destinations_list.append(obj)

            return destinations_list

    def add(self, schema: DestinationSchema = None, **kwargs):
        """
        Add destination to HealthBot

        :param object schema: `DestinationSchema <jnpr.healthbot.swagger.models.html#destinationschema>`_
        :param object kwargs: key values, which can be used to create
            DestinationSchema
            Check `DestinationSchema <jnpr.healthbot.swagger.models.html#destinationschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import DestinationSchema

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                ds = DestinationSchema(name='HbEZ-destination')
                hb.settings.destination.add(ds)

        :returns: True when OK

        """
        if schema is None:
            schema = DestinationSchema(**kwargs)
        payload = self.hbot._create_payload(schema)
        destination_url = self.hbot.urlfor.destination(payload['name'])
        response = self.api.post(destination_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def delete(self, name: str):
        """
        Remove destination from settings

        :param str name: The ID name of the destination to be deleted

        Example:
        ::
            hb.settings.destination.delete('xyz')
            hb.commit()

        :returns: True when OK
        """

        destinations_url = self.hbot.urlfor.destination(name)
        response = self.api.delete(destinations_url)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()

        return True

    def update(self, schema: DestinationSchema = None, **kwargs):
        """
        Update `DestinationSchema <jnpr.healthbot.swagger.models.html#destinationschema>`_ for
        given destination schema

        Passing Schema invoke `put` and kwargs `post`

        :param obj schema: `DestinationSchema <jnpr.healthbot.swagger.models.html#destinationschema>`_
        :param object kwargs: key values, which can be used to create
            DestinationSchema
            Check `DestinationSchema <jnpr.healthbot.swagger.models.html#destinationschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schemaObj = hb.settings.destination.get('xyz')
                schemaObj.description = 'changed description'
                hb.settings.destination.update(schemaObj)

        :returns: True when OK
        """
        if schema is None:
            schema = DestinationSchema(**kwargs)
            call = self.api.post
        else:
            if not isinstance(schema, DestinationSchema):
                raise SchemaError(DestinationSchema)
            call = self.api.put
        payload = self.hbot._create_payload(schema)
        name = schema.name
        destination_url = self.hbot.urlfor.destination(name)
        response = call(destination_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True


class Report(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def get(self, name: str = None, uncommitted: bool = True):
        """
        Get `ReportSchema(s) <jnpr.healthbot.swagger.models.html#reportschema>`_ for
        given report name or list for all

        :param name: report ID
        :param bool uncommitted: True includes fetches uncommitted changes,
            False restricts data set to only committed changes

        Example:
        ::

                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.settings.report.get('xyz')

                    # for all
                    print(hb.settings.report.get()

        :return: `ReportSchema(s) <jnpr.healthbot.swagger.models.html#reportschema>`_
        """
        if name is not None:
            report_url = self.hbot.urlfor.report(name)
            if uncommitted:
                report_url += self.hbot.apiopt_candidate
            response = self.api.get(report_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(
                response, ReportSchema)
        else:
            reports_url = self.hbot.urlfor.reports()
            if uncommitted:
                reports_url += self.hbot.apiopt_candidate
            response = self.api.get(reports_url)
            response_json = response.json()
            if response.status_code != 200:
                logger.error(response.text)
                raise NotFoundError(response_json)
            existing_reports = response_json['report']
            reports_list = []
            for report in existing_reports:
                obj = self.hbot._create_schema(report, ReportSchema)
                reports_list.append(obj)

            return reports_list

    def add(self, schema: ReportSchema = None, **kwargs):
        """
        Add report to HealthBot

        :param object schema: `ReportSchema <jnpr.healthbot.swagger.models.html#reportschema>`_
        :param object kwargs: key values, which can be used to create
            ReportSchema
            Check `ReportSchema <jnpr.healthbot.swagger.models.html#reportschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import ReportSchema

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:

                from jnpr.healthbot import SchedulerSchema
                sc = SchedulerSchema(name='HbEZ-schedule', repeat={'every': 'week'},
                                start_time="2019-07-22T05:32:23Z")
                hb.settings.scheduler.add(sc)

                from jnpr.healthbot import DestinationSchema
                ds = DestinationSchema(name='HbEZ-destination',
                                email={'id': 'nitinkr@juniper.net'})
                hb.settings.destination.add(ds)

                from jnpr.healthbot import ReportSchema
                rs = ReportSchema(name="HbEZ-report", destination=['HbEZ-destination'],
                                format="html", schedule=["HbEZ-schedule"])
                hb.settings.report.add(rs)

        :returns: True when OK

        """
        if schema is None:
            schema = ReportSchema(**kwargs)
        payload = self.hbot._create_payload(schema)
        report_url = self.hbot.urlfor.report(payload['name'])
        response = self.api.post(report_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def delete(self, name: str):
        """
        Remove report from settings

        :param str name: The name of the report to be deleted

        Example:
        ::

            hb.settings.report.delete('xyz')
            hb.commit()

        :returns: True when OK
        """

        report_url = self.hbot.urlfor.report(name)
        response = self.api.delete(report_url)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()

        return True

    def update(self, schema: ReportSchema = None, **kwargs):
        """
        Update `ReportSchema <jnpr.healthbot.swagger.models.html#reportschema>`_ for
        given report schema

        Passing Schema invoke `put` and kwargs `post`

        :param obj schema: `ReportSchema <jnpr.healthbot.swagger.models.html#reportschema>`_
        :param object kwargs: key values, which can be used to create
            ReportSchema
            Check `ReportSchema <jnpr.healthbot.swagger.models.html#reportschema>`_
            for details about which all keys can be used

        Example:
        ::

            from jnpr.healthbot import HealthBotClient
            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schemaObj = hb.settings.report.get('xyz')
                schemaObj.description = 'changed description'
                hb.settings.report.update(schemaObj)

        :returns: True when OK
        """
        if schema is None:
            schema = ReportSchema(**kwargs)
            call = self.api.post
        else:
            if not isinstance(schema, ReportSchema):
                raise SchemaError(ReportSchema)
            call = self.api.put
        payload = self.hbot._create_payload(schema)
        name = schema.name
        report_url = self.hbot.urlfor.report(name)
        response = call(report_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True


class LicenseKeyManagement(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)
        self._license_api = LicenseApi(hbot.api_client)

    def get_features(self):
        """
        Get `LicenseFeatureSchema(s) <jnpr.healthbot.swagger.models.html#licensefeatureschema>`_ for
        given license id or for all licence id

        :param license_id: License ID

        Example:
        ::

                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.settings.license.get_features()

        :return: `LicenseFeatureSchema(s) <jnpr.healthbot.swagger.models.html#licensefeatureschema>`_

        """
        response = self._license_api.retrieve_iceberg_license_features_info(
            x_iam_token=self.authorization)
        return response.license_feature

    def get_ids(self):
        """
        List of all licence id

        Example:
        ::

                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    # print all existing licence ids
                    print(hb.settings.license.get()
        :return: `List of license ids`

        """
        return self._license_api.retrieve_iceberg_get_all_license_id(
            x_iam_token=self.authorization)

    def get(self, license_id: str = None):
        """
        Get `LicenseKeySchema(s) <jnpr.healthbot.swagger.models.html#licensekeyschema>`_ for
        given license id or for all licence id

        :param license_id: License ID

        Example:
        ::

                from jnpr.healthbot import HealthBotClient

                with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                    print(hb.settings.license.get()

                    # for given licence id
                    print(hb.settings.report.get('xxxxx')

        :return: `LicenseKeySchema(s) <jnpr.healthbot.swagger.models.html#licensekeyschema>`_
        """
        if license_id is not None:
            return self._license_api.retrieve_iceberg_license_key_contents_by_id(
                    license_id, x_iam_token=self.authorization)
        else:
            response = self._license_api.retrieve_iceberg_license_key_contents(
                x_iam_token=self.authorization)
            return response.license_key

    def add(self, license_file):
        """
        Add report to HealthBot

        :param path license_file: license file path

        Example:
        ::

            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                hb.settings.license.add(license_file='/var/tmp/xyz')

        :returns: license_id if OK

        """
        response = self._license_api.create_iceberg_add_license_from_file(
            license_file, x_iam_token=self.authorization)
        return response.license_id

    def delete(self, license_id: str):
        """
        Remove report from settings

        :param str license_id: The license id be deleted

        Example:
        ::

            hb.settings.license.delete('xx-xxx-xxx-xxx-xx')

        :returns: True when OK
        """

        self._license_api.delete_iceberg_delete_license_by_id(
            license_id, x_iam_token=self.authorization)

        return True
