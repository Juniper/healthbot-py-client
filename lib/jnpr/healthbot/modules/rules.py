from jnpr.healthbot.swagger.models.rule_schema import RuleSchema
from jnpr.healthbot.swagger.models.topic_schema import TopicSchema
from jnpr.healthbot.exception import SchemaError, NotFoundError

from jnpr.healthbot.modules import BaseModule
import logging
logger = logging.getLogger(__file__)


class Rule(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def add(self, topic_name: str, schema: RuleSchema = None, **kwargs):
        """
        Create Rule under given topic

        :param str topic_name: Rules to be created under this given topic name
        :param object schema: `RuleSchema <jnpr.healthbot.swagger.models.html#ruleschema>`_
        :param object kwargs: key values, which can be used to create
            RuleSchema
            Check `RuleSchema <jnpr.healthbot.swagger.models.html#ruleschema>`_
            for details about which all keys can be used

        Example:
        ::
            from jnpr.healthbot import HealthBotClient
            from jnpr.healthbot import RuleSchema

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                rs = RuleSchema(rule_name="hbez-fpc-heap-utilization")

                rs.description = "HealthBot EZ example"
                rs.synopsis = "Using python client for demo"


                rs.sensor = [{'description': 'Monitors FPC buffer, heap and cpu utilization',
                              'iAgent': {'file': 'fpc-utilization.yml',
                                         'frequency': '30s',
                                         'table': 'FPCCPUHEAPutilizationTable'},
                              'sensor-name': 'fpccpuheaputilization'}]

                from jnpr.healthbot.swagger.models.rule_schema_field import RuleSchemaField
                from jnpr.healthbot.swagger.models.rule_schema_constant import RuleSchemaConstant

                rs.field = [RuleSchemaField(constant=RuleSchemaConstant(value='{{fpc-buffer-usage-threshold}}'),
                                            description='This field is for buffer usage threshold',
                                            field_name='linecard-buffer-usage-threshold'),
                            RuleSchemaField(constant=RuleSchemaConstant(value='{{fpc-cpu-usage-threshold}}'),
                                            description='This field is for linecard cpu usage threshold',
                                            field_name='linecard-cpu-usage-threshold'),
                            RuleSchemaField(constant=RuleSchemaConstant(value='{{fpc-heap-usage-threshold}}'),
                                            description='This field is for linecard heap usage threshold',
                                            field_name='linecard-heap-usage-threshold')]

                rs.keys = ['slot']

                rs.variable = [{'description': 'Linecard Buffer Memory usage threshold value',
                                'name': 'fpc-buffer-usage-threshold',
                                'type': 'int',
                                'value': '80'},
                               {'description': 'Linecard CPU usage threshold value',
                                'name': 'fpc-cpu-usage-threshold',
                                'type': 'int',
                                'value': '80'},
                               {'description': 'Linecard Heap Memory usage threshold value',
                                'name': 'fpc-heap-usage-threshold',
                                'type': 'int',
                                'value': '80'}]

                rs.trigger = [{'description': 'Sets health based on linecard buffer memory',
                               'frequency': '60s',
                               'synopsis': 'Linecard buffer memory kpi',
                               'term': [{'term-name': 'is-buffer-memory-utilization-greater-than-threshold',
                                         'then': {'status': {'color': 'red',
                                                             'message': 'FPC buffer memory '
                                                                        'utilization '
                                                                        '($memory-buffer-utilization) '
                                                                        'is over threshold '
                                                                        '($linecard-buffer-usage-threshold)'}},
                                         'when': {'greater-than': [{'left-operand': '$memory-buffer-utilization',
                                                                    'right-operand': '$linecard-buffer-usage-threshold'}]}},
                                        {'term-name': 'buffer-utilization-less-than-threshold',
                                         'then': {'status': {'color': 'green'}}}],
                               'trigger-name': 'fpc-buffer-memory-utilization'},
                              {'description': 'Sets health based on linecard cpu utilization',
                               'frequency': '60s',
                               'synopsis': 'Linecard cpu utilization kpi',
                               'term': [{'term-name': 'is-cpu-utilization-greater-than-80',
                                         'then': {'status': {'color': 'red',
                                                             'message': 'FPC CPU utilization '
                                                                        '($cpu-total) is over '
                                                                        'threshold '
                                                                        '($linecard-cpu-usage-threshold)'}},
                                         'when': {'greater-than': [{'left-operand': '$cpu-total',
                                                                    'right-operand': '$linecard-cpu-usage-threshold',
                                                                    'time-range': '180s'}]}},
                                        {'term-name': 'cpu-utilization-less-than-threshold',
                                         'then': {'status': {'color': 'green'}}}],
                               'trigger-name': 'fpc-cpu-utilization'},
                              {'description': 'Sets health based on linecard heap memory '
                                              'utilization',
                               'frequency': '60s',
                               'synopsis': 'Linecard heap memory kpi',
                               'term': [{'term-name': 'is-heap-memory-utilization-greater-than-threshold',
                                         'then': {'status': {'color': 'red',
                                                             'message': 'FPC heap memory '
                                                                        'utilization '
                                                                        '($memory-heap-utilization) '
                                                                        'is over threshold '
                                                                        '($linecard-heap-usage-threshold)'}},
                                         'when': {'greater-than': [{'left-operand': '$memory-heap-utilization',
                                                                    'right-operand': '$linecard-heap-usage-threshold'}]}},
                                        {'term-name': 'heap-memory-utilization-less-than-threshold',
                                         'then': {'status': {'color': 'green'}}}],
                               'trigger-name': 'fpc-heap-memory-utilization'}]
                hb.rule.add('hbez', schema=rs)

        Returns:
            True if action successful

        """
        if schema is None:
            schema = RuleSchema(**kwargs)
        else:
            if not isinstance(schema, RuleSchema):
                raise SchemaError(RuleSchema)

        # check for topic presence, if not do all that first
        topic_url = self.hbot.urlfor.topic(topic_name)
        resp = self.api.get(topic_url + self.hbot.apiopt_candidate)
        if not resp.ok:
            logger.debug(
                "Adding topic '{}' first as its not present".format(topic_name))
            response = self.api.post(topic_url, json={"topic-name":
                                                      topic_name})
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()

        payload = self.hbot._create_payload(schema)
        rule_url = self.hbot.urlfor.rule(topic_name, payload['rule-name'])
        resp = self.api.get(rule_url + self.hbot.apiopt_candidate)
        if resp.ok:
            logger.info("Rule already exists")
            return True
        response = self.api.post(rule_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()

        return True

    def delete(self, topic_name: str, rule_name: str):
        """
        Delete rule under given topic

        :param str topic_name: The name of the topic under which rule need to deleted
        :param str rule_name: The name of the rule to be deleted

        Example:
        ::
            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                hb.rule.delete('linecard.ospf', 'check-ddos-statistics')

        """

        payload = {'rule-name': rule_name}
        rule_url = self.hbot.urlfor.rule(topic_name, rule_name)
        response = self.api.delete(rule_url, json=payload)
        if response.status_code != 204:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def get(
            self,
            topic_name: str,
            rule_name: str = None,
            uncommitted: bool = True):
        """
        get rule(s) details under given topic

        :param str topic_name: The name of the topic under which rule need to be fetched
        :param str rule_name: The name of the rule under given topic
                If none return list for all Rule
        :param bool uncommitted: True includes fetches uncommitted changes,
                False restricts data set to only committed changes

        Example:
        ::
            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                print(hb.rule.get('linecard.ospf', 'check-ddos-statistics')

                print(hb.rule.get('linecard.ospf')

        """
        if rule_name is not None:
            rule_url = self.hbot.urlfor.rule(topic_name, rule_name)
            if uncommitted:
                rule_url += self.hbot.apiopt_candidate
            response = self.api.get(rule_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(response, RuleSchema)
        else:
            response = self.hbot.topic.get(topic_name)
            response_json = response.to_dict()
            rule_list = []
            existing_rules = response_json['rule']
            for rule in existing_rules:
                obj = self.hbot._create_schema(rule, RuleSchema)
                rule_list.append(obj)
            return rule_list

    def update(self, topic_name: str, schema: RuleSchema = None, **kwargs):
        """
        Update `RuleSchema <jnpr.healthbot.swagger.models.html#ruleschema>`_ for
        given rule schema object

        Passing Schema invoke `put` and kwargs `post`

        :param str topic_name: The name of the topic under which rule need to be updated
        :param obj schema: `RuleSchema <jnpr.healthbot.swagger.models.html#ruleschema>`_
        :param object kwargs: key values, which can be used to create
            RuleSchema

        Example:
        ::

            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                schemaObj = hb.rule.get(topic_name='hbez', rule_name="hbez-fpc-heap-utilization")
                schemaObj.description = "HbEZ example"
                hb.rule.update(topic_name='hbez', schemaObj)

        :returns: True when OK

        """
        if schema is None:
            schema = RuleSchema(**kwargs)
            call = self.api.post
        else:
            if not isinstance(schema, RuleSchema):
                raise SchemaError(RuleSchema)
            call = self.api.put
        payload = self.hbot._create_payload(schema)
        rule_url = self.hbot.urlfor.rule(topic_name, payload['rule-name'])
        response = call(rule_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def upload_rule_file(self, filename):
        """

        :param filename: File to be loaded
        :return: return True of OK
        """
        return self.hbot.upload_helper_file(filename)


class Topic(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def get(self, topic_name: str = None, uncommitted: bool = True):
        """
        Get `TopicSchema(s) <jnpr.healthbot.swagger.models.html#topicschema>`_
         for given topic name or all topics in HealthBot system

        Example:
        ::

            from jnpr.healthbot import HealthBotClient

            with HealthBotClient('xx.xxx.x.xx', 'xxxx', 'xxxx') as hb:
                print(hb.topic.get('linecard.ospf'))
                topics = hb.topic.get()
                for topic in topics:
                    print(topic)

        :return: Single/list of `TopicSchema <jnpr.healthbot.swagger.models.html#topicchema>`_
        """
        if topic_name is not None:
            topic_url = self.hbot.urlfor.topic(topic_name)
            if uncommitted:
                topic_url += self.hbot.apiopt_candidate
            response = self.api.get(topic_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            return self.hbot._create_schema(response, TopicSchema)
        else:
            topic_list = []

            topic_list_url = self.hbot.urlfor.topics()
            resp = self.api.get(topic_list_url)

            if resp.status_code == 404:
                return False

            existing_topics = resp.json()['topic']
            for topic in existing_topics:
                obj = self.hbot._create_schema(topic, TopicSchema)
                topic_list.append(obj)

            return topic_list
