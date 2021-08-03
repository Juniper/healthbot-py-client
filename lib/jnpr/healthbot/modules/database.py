from jnpr.healthbot.swagger.models.table_schema import TableSchema
from influxdb import InfluxDBClient
import logging
logger = logging.getLogger(__file__)


class Database(InfluxDBClient):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance

        Example:
        ::
            hb.tsdb.query("show databases")
            hb.tsdb.query('select * from "protocol-eventd-host/check-host-traffic/packet-loss" limit 10',
                              database='Core:vmx')
        """
        self.hbot = hbot
        self.url = hbot.url
        InfluxDBClient.__init__(self, hbot.server, 8086)

    @property
    def api(self):
        return self.hbot.hbot_session

    def get_table(self):
        """
        Get list of tables

        :return: list of `TableSchema <jnpr_healthbot_swagger/TableSchema.html>`_
        """
        get_tabel_url = self.hbot.urlfor.table()
        response = self.api.get(get_tabel_url)

        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return self.hbot._create_schema(response, TableSchema)
