import unittest
from nose.plugins.attrib import attr

from mock import patch, PropertyMock

from jnpr.healthbot import HealthBotClient
from jnpr.healthbot import NotificationSchema
from jnpr.healthbot import NotificationSchemaSlack
from jnpr.healthbot import SchedulerSchema
from jnpr.healthbot import DestinationSchema
from jnpr.healthbot import ReportSchema
from jnpr.healthbot import RetentionPolicySchema

from requests.models import Response
from . import _mock_user_login


@attr('unit')
class TestSettings(unittest.TestCase):

    @patch('jnpr.healthbot.healthbot.requests.Session')
    @patch('jnpr.healthbot.swagger.api.authentication_api.AuthenticationApi.user_login')
    def setUp(self, mock_user_login, mock_request):
        self.mock_user_login = _mock_user_login
        self.mock_request = mock_request
        self.mock_request().get.side_effect = self._mock_manager
        with patch('jnpr.healthbot.healthbot.HealthBotClient.version',
                   new_callable=PropertyMock) as mock_ver:
            with patch('jnpr.healthbot.healthbot.HealthBotClient.config_url',
                       new_callable=PropertyMock) as mock_cnf:
                mock_ver.return_value = '2.1.0'
                mock_cnf.return_value = "https://1.1.1.1:8080/api/v1"
                self.conn = HealthBotClient(
                    server='1.1.1.1',
                    user='test',
                    password='password123').open()
        self.conn.api_client.call_api = self._mock_manager

    def tearDown(self) -> None:
        self.conn.close()

    def test_add_notification(self):
        ns = NotificationSchema(notification_name='HbEZ-notification')
        ns.description = "example of adding notification via API"
        nss = NotificationSchemaSlack(channel="HbEZ", url='https://testing')
        ns.slack = nss
        self.assertTrue(self.conn.settings.notification.add(ns))
        self.assertEqual(self.mock_request().mock_calls[2][0], 'post')
        self.assertEqual(
            self.mock_request().mock_calls[2][1][0],
            'https://1.1.1.1:8080/api/v1/notification/HbEZ-notification')
        # add without schema
        self.assertTrue(
            self.conn.settings.notification.add(
                notification_name='HbEZ-notification',
                description="example of adding notification via API"))
        self.assertEqual(self.mock_request().mock_calls[2][0], 'post')
        self.assertEqual(
            self.mock_request().mock_calls[2][1][0],
            'https://1.1.1.1:8080/api/v1/notification/HbEZ-notification')

    def test_add_scheduler(self):
        sc = SchedulerSchema(
            name='HbEZ-schedule',
            repeat={
                'every': 'week'},
            start_time="2019-07-22T05:32:23Z")
        self.assertTrue(self.conn.settings.scheduler.add(sc))
        self.assertEqual(self.mock_request().mock_calls[2][0], 'post')
        self.assertEqual(
            self.mock_request().mock_calls[2][1][0],
            'https://1.1.1.1:8080/api/v1/system-settings/scheduler/HbEZ-schedule')
        # add without schema
        self.assertTrue(
            self.conn.settings.scheduler.add(
                name='HbEZ-schedule',
                repeat={
                    'every': 'week'},
                start_time="2019-07-22T05:32:23Z"))
        self.assertEqual(self.mock_request().mock_calls[2][0], 'post')
        self.assertEqual(
            self.mock_request().mock_calls[2][1][0],
            'https://1.1.1.1:8080/api/v1/system-settings/scheduler/HbEZ-schedule')

    def test_add_destinaton(self):
        ds = DestinationSchema(
            name='HbEZ-destination',
            email={
                'id': 'xyz@abc.com'})
        self.assertTrue(self.conn.settings.destination.add(ds))
        self.assertEqual(self.mock_request().mock_calls[2][0], 'post')
        self.assertEqual(
            self.mock_request().mock_calls[2][1][0],
            'https://1.1.1.1:8080/api/v1/system-settings/report-generation/destination/HbEZ-destination')
        # add without schema
        self.assertTrue(self.conn.settings.destination.add(
            name='HbEZ-destination', email={'id': 'xyz@abc.com'}))
        self.assertEqual(self.mock_request().mock_calls[2][0], 'post')
        self.assertEqual(
            self.mock_request().mock_calls[2][1][0],
            'https://1.1.1.1:8080/api/v1/system-settings/report-generation/destination/HbEZ-destination')

    def test_add_report(self):
        rs = ReportSchema(
            name="HbEZ-report",
            destination=['HbEZ-destination'],
            format="html",
            schedule=["HbEZ-schedule"])
        self.assertTrue(self.conn.settings.report.add(rs))
        self.assertEqual(self.mock_request().mock_calls[2][0], 'post')
        self.assertEqual(
            self.mock_request().mock_calls[2][1][0],
            'https://1.1.1.1:8080/api/v1/system-settings/report-generation/report/HbEZ-report')
        # add without schema
        self.assertTrue(
            self.conn.settings.report.add(
                name="HbEZ-report",
                destination=['HbEZ-destination'],
                format="html",
                schedule=["HbEZ-schedule"]))
        self.assertEqual(self.mock_request().mock_calls[2][0], 'post')
        self.assertEqual(
            self.mock_request().mock_calls[2][1][0],
            'https://1.1.1.1:8080/api/v1/system-settings/report-generation/report/HbEZ-report')

    def test_add_retention_policy(self):
        rps = RetentionPolicySchema(retention_policy_name='HbEZ-testing')
        self.assertTrue(
            self.conn.settings.retention_policy.add(rps))
        self.assertEqual(self.mock_request().mock_calls[2][0], 'post')
        self.assertEqual(
            self.mock_request().mock_calls[2][1][0],
            'https://1.1.1.1:8080/api/v1/retention-policy/HbEZ-testing')
        # without creating schema
        self.assertTrue(
            self.conn.settings.retention_policy.add(
                retention_policy_name='HbEZ-testing'))
        self.assertEqual(self.mock_request().mock_calls[2][0], 'post')
        self.assertEqual(
            self.mock_request().mock_calls[2][1][0],
            'https://1.1.1.1:8080/api/v1/retention-policy/HbEZ-testing')

    def test_get_notification(self):
        ns = self.conn.settings.notification.get(
            notification_name='HbEZ-notification')
        self.assertEqual(
            ns.description,
            "example of adding notification via API")
        self.assertEqual(ns.notification_name, "HbEZ-notification")

    def test_get_notification_error(self):
        self.assertRaises(
            ValueError,
            self.conn.settings.notification.get,
            notification_name='error')

    def test_get_scheduler(self):
        sc = self.conn.settings.scheduler.get(name='HbEZ-schedule')
        self.assertEqual(sc.repeat, {
            "every": "week"
        })

    def test_get_destination(self):
        ds = self.conn.settings.destination.get(
            name='HbEZ-destination')
        self.assertEqual(ds.email, {'id': 'xyz@abc.com'})

    def test_get_report(self):
        rs = self.conn.settings.report.get(name="HbEZ-report")
        self.assertEqual(rs.format, 'html')

    def test_get_retention_policy(self):
        rp = self.conn.settings.retention_policy.get(
            'HbEZ-testing')
        self.assertEqual(rp.retention_policy_name, "HbEZ-testing")

    def test_get_reports(self):
        rs = self.conn.settings.report.get()
        self.assertGreater(len(rs), 0)

    def test_get_notifications(self):
        ns = self.conn.settings.notification.get()
        self.assertGreater(len(ns), 0)

    def test_get_schedulers(self):
        sc = self.conn.settings.scheduler.get()
        self.assertGreater(len(sc), 0)

    def test_get_destinations(self):
        des = self.conn.settings.destination.get()
        self.assertGreater(len(des), 0)

    def test_get_reports(self):
        rep = self.conn.settings.report.get()
        self.assertGreater(len(rep), 0)

    def test_get_retention_policies(self):
        rp = self.conn.settings.retention_policy.get()
        self.assertGreater(len(rp), 0)

    def test_delete_notification(self):
        ret = self.conn.settings.notification.delete(
            notification_name='HbEZ-notification')
        self.assertTrue(ret)
        self.assertEqual(self.mock_request().mock_calls[2][0],
                         'delete')

    def test_delete_scheduler(self):
        ret = self.conn.settings.scheduler.delete(
            name='HbEZ-schedule')
        self.assertTrue(ret)
        self.assertEqual(self.mock_request().mock_calls[2][0],
                         'delete')

    def test_delete_destinaton(self):
        ret = self.conn.settings.destination.delete(
            name='HbEZ-destination')
        self.assertTrue(ret)
        self.assertEqual(self.mock_request().mock_calls[2][0],
                         'delete')

    def test_delete_report(self):
        ret = self.conn.settings.report.delete(name="HbEZ-report")
        self.assertTrue(ret)
        self.assertEqual(self.mock_request().mock_calls[2][0],
                         'delete')

    def test_delete_retention_policy(self):
        ret = self.conn.settings.retention_policy.delete(
            "HbEZ-testing")
        self.assertTrue(ret)
        self.assertEqual(self.mock_request().mock_calls[2][0],
                         'delete')

    def test_update_notification(self):
        ns = self.conn.settings.notification.get(
            notification_name='HbEZ-notification')
        from jnpr.healthbot import NotificationSchemaHttppost
        ns.http_post = NotificationSchemaHttppost(url='https://juniper.net')
        self.conn.settings.notification.update(ns)
        self.assertEqual(
            self.mock_request().mock_calls[3][2]['json']['http-post']['url'],
            'https://juniper.net')

    def test_update_scheduler(self):
        sc = self.conn.settings.scheduler.get(name='HbEZ-schedule')
        sc.repeat = {'every': 'daily'}
        self.conn.settings.scheduler.update(sc)
        self.assertEqual(
            self.mock_request().mock_calls[3][2]['json']['repeat']['every'],
            'daily')

    def test_update_destination(self):
        ds = self.conn.settings.destination.get(
            name='HbEZ-destination')
        ds.email = {'id': 'pqr@abc.com'}
        self.conn.settings.destination.update(ds)
        self.assertEqual(
            self.mock_request().mock_calls[3][2]['json']['email']['id'],
            'pqr@abc.com')

    def test_update_report(self):
        rs = self.conn.settings.report.get(name="HbEZ-report")
        rs.format = 'json'
        self.conn.settings.report.update(rs)
        self.assertEqual(
            self.mock_request().mock_calls[3][2]['json']['format'],
            'json')

    def test_update_retention_policy(self):
        rp = self.conn.settings.retention_policy.get(
            'HbEZ-testing')
        rp.duration = '10h'
        self.conn.settings.retention_policy.update(rp)
        self.assertEqual(
            self.mock_request().mock_calls[3][2]['json']['duration'],
            '10h')

    def test_license_get(self):
        ret = self.conn.settings.license.get(
            'xxx-xx-xxx')
        self.assertEqual(ret["customer-id"], "xxxx")

    def test_license_get_ids(self):
        ret = self.conn.settings.license.get_ids()
        self.assertEqual(ret, ['xxx-xx-xxx', 'yyy-yy-yyy'])

    def test_license_get_features(self):
        ret = self.conn.settings.license.get_features()
        self.assertEqual(ret.feature_description, "Max G8")

    def test_license_get_all(self):
        ret = self.conn.settings.license.get()
        self.assertEqual(ret[0].validity_type, "countdown")

    def test_license_delete(self):
        self.assertTrue(self.conn.settings.license.delete("xxx-xx-xxx"))

    def _mock_manager(self, *args, **kwargs):
        class MockResponse(Response):
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            @property
            def text(self):
                return 'did you just hit an error'

            def json(self):
                return self.json_data

            def to_dict(self):
                return self.json_data

            def raise_for_status(self):
                return None

        if args[0] == 'https://1.1.1.1:8080/api/v1/notification/HbEZ-notification/?working=true':
            return MockResponse({
                "description": "example of adding notification via API",
                "notification-name": "HbEZ-notification",
                "slack": {
                    "channel": "HbEZ",
                    "url": "http://testing"
                }
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/system-settings/scheduler/HbEZ-schedule/?working=true':
            return MockResponse({
                "name": "HbEZ-schedule",
                "repeat": {
                    "every": "week"
                },
                "start-time": "2019-07-22T05:32:23Z"
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/system-settings/report-generation/destination/HbEZ-destination/?working=true':
            return MockResponse({
                "email": {
                    "id": "xyz@abc.com"
                },
                "name": "HbEZ-destination"
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/system-settings/report-generation/report/HbEZ-report/?working=true':
            return MockResponse({
                "destination": [
                    "HbEZ-destination"
                ],
                "format": "html",
                "name": "HbEZ-report",
                "schedule": [
                    "HbEZ-schedule"
                ]
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/system-settings/report-generation/reports/?working=true':
            return MockResponse({
                "report": [
                    {
                        "destination": [
                            "HbEZ-destination"
                        ],
                        "format": "html",
                        "name": "HbEZ-report",
                        "schedule": [
                            "HbEZ-schedule"
                        ]
                    }
                ]
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/notifications/?working=true':
            return MockResponse({
                "notification": [
                    {
                        "description": "example of adding notification via API",
                        "notification-name": "HbEZ-notification",
                        "slack": {
                            "channel": "HbEZ",
                            "url": "http://testing"
                        }
                    }
                ]
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/system-settings/schedulers/?working=true':
            return MockResponse({
                "scheduler": [
                    {
                        "name": "HbEZ-schedule",
                        "repeat": {
                            "every": "week"
                        },
                        "start-time": "2019-07-22T05:32:23Z"
                    }
                ]
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/system-settings/report-generation/destinations/?working=true':
            return MockResponse({
                "destination": [
                    {
                        "email": {
                            "id": "xyz@abc.com"
                        },
                        "name": "HbEZ-destination"
                    }
                ]
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/retention-policy/HbEZ-testing/?working=true':
            return MockResponse({
                "retention-policy-name": "HbEZ-testing"
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/retention-policies/?working=true':
            return MockResponse({
                "retention-policy": [
                    {
                        "retention-policy-name": "HbEZ-testing"
                    }
                ]
            }, 200)
        elif args[0] == 'https://1.1.1.1:8080/api/v1/notification/error/?working=true':
            obj = MockResponse(None, 404)

            def fn():
                raise ValueError
            obj.raise_for_status = fn
            return obj
        elif args[0] == '/license/key/{license_id}/contents/' and \
                args[2] == {'license_id': 'xxx-xx-xxx'}:
            return {"customer-id": "xxxx",
                    "end-date": "2106-02-0xxx",
                    "features": [{"capacity-flag": False,
                                  "capacity-value": 1,
                                  "feature-description": "Allow a..",
                                  "feature-id": 10001,
                                  "feature-name": "xxxx"},
                                 ],
                    "license-id": "xxx-xx-xxx",
                    "mode": "standalone",
                    "order-type": "commercial",
                    "sku-name": "HBxxx",
                    "start-date": "20xxx",
                    "sw-serial-id": "07xxx",
                    "validity-type": "xxx",
                    "version": 1}
        elif args[0] == '/license/keys/contents/':
            from jnpr.healthbot import LicenseKeySchema
            from jnpr.healthbot import LicenseKeysSchema
            return LicenseKeysSchema([LicenseKeySchema(**{"customer_id": "xxxx",
                    "end_date": "2106-02-0xxx",
                    "features": [{"capacity_flag": False,
                                  "capacity_value": 1,
                                  "feature_description": "Allow a..",
                                  "feature_id": 10001,
                                  "feature_name": "xxxx"},
                                 ],
                    "license_id": "xxx-xx-xxx",
                    "mode": "standalone",
                    "order_type": "commercial",
                    "sku_name": "HBxxx",
                    "start_date": "20xxx",
                    "sw_serial_id": "07xxx",
                    "validity_type": "countdown",
                    "version": 1})])
        elif args[0] == '/license/keys/':
            return ["xxx-xx-xxx", "yyy-yy-yyy"]
        elif args[0] == '/license/status/':
            from jnpr.healthbot import LicenseFeaturesSchema
            from jnpr.healthbot import LicenseFeatureSchema
            return LicenseFeaturesSchema(license_feature= LicenseFeatureSchema(**{'compliance': True,
                     'end_date': 111,
                     'feature_description': 'Max G8',
                     'feature_id': 111,
                     'feature_name': 'xxxx',
                     'license_remaining': 1,
                     'license_requested': 1,
                     'license_total': 1,
                     'license_usage': 1,
                     'max_remaining_days': 1,
                     'mode': 'standalone',
                     'valid_until': 'xxxx',
                     'validity_type': 'countdown'}))
        elif args[0] == '/license/key/{license_id}/' and args[1] == 'DELETE' and\
                args[2] == {'license_id': 'xxx-xx-xxx'}:
            return None
        return MockResponse(None, 404)
