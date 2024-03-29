# coding: utf-8

"""
    Paragon Insights APIs

    API interface for PI application  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DevicegroupSchemaScheduler(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'instance_id': 'str',
        'playbook': 'str',
        'rule': 'str',
        'schedule': 'str'
    }

    attribute_map = {
        'instance_id': 'instance-id',
        'playbook': 'playbook',
        'rule': 'rule',
        'schedule': 'schedule'
    }

    def __init__(self, instance_id=None, playbook=None, rule=None, schedule=None):  # noqa: E501
        """DevicegroupSchemaScheduler - a model defined in Swagger"""  # noqa: E501

        self._instance_id = None
        self._playbook = None
        self._rule = None
        self._schedule = None
        self.discriminator = None

        self.instance_id = instance_id
        self.playbook = playbook
        self.rule = rule
        self.schedule = schedule

    @property
    def instance_id(self):
        """Gets the instance_id of this DevicegroupSchemaScheduler.  # noqa: E501

        Unique ID of the variable instance. This should be unique per playbook and rule combination. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The instance_id of this DevicegroupSchemaScheduler.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DevicegroupSchemaScheduler.

        Unique ID of the variable instance. This should be unique per playbook and rule combination. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param instance_id: The instance_id of this DevicegroupSchemaScheduler.  # noqa: E501
        :type: str
        """
        if instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501
        if instance_id is not None and len(instance_id) > 64:
            raise ValueError("Invalid value for `instance_id`, length must be less than or equal to `64`")  # noqa: E501
        if instance_id is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', instance_id):  # noqa: E501
            raise ValueError(r"Invalid value for `instance_id`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def playbook(self):
        """Gets the playbook of this DevicegroupSchemaScheduler.  # noqa: E501

        Name of the playbook in which the variable instance needs to be used  # noqa: E501

        :return: The playbook of this DevicegroupSchemaScheduler.  # noqa: E501
        :rtype: str
        """
        return self._playbook

    @playbook.setter
    def playbook(self, playbook):
        """Sets the playbook of this DevicegroupSchemaScheduler.

        Name of the playbook in which the variable instance needs to be used  # noqa: E501

        :param playbook: The playbook of this DevicegroupSchemaScheduler.  # noqa: E501
        :type: str
        """
        if playbook is None:
            raise ValueError("Invalid value for `playbook`, must not be `None`")  # noqa: E501
        if playbook is not None and len(playbook) > 64:
            raise ValueError("Invalid value for `playbook`, length must be less than or equal to `64`")  # noqa: E501
        if playbook is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', playbook):  # noqa: E501
            raise ValueError(r"Invalid value for `playbook`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._playbook = playbook

    @property
    def rule(self):
        """Gets the rule of this DevicegroupSchemaScheduler.  # noqa: E501

        Name of the rule. This should be of the format <topic-name>/<rule-name>  # noqa: E501

        :return: The rule of this DevicegroupSchemaScheduler.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this DevicegroupSchemaScheduler.

        Name of the rule. This should be of the format <topic-name>/<rule-name>  # noqa: E501

        :param rule: The rule of this DevicegroupSchemaScheduler.  # noqa: E501
        :type: str
        """
        if rule is None:
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501
        if rule is not None and len(rule) > 129:
            raise ValueError("Invalid value for `rule`, length must be less than or equal to `129`")  # noqa: E501
        if rule is not None and not re.search(r'^[a-z][a-z-]*(\\.{1}[a-z0-9-]+)*\/[a-z][a-z0-9_-]*$', rule):  # noqa: E501
            raise ValueError(r"Invalid value for `rule`, must be a follow pattern or equal to `/^[a-z][a-z-]*(\\.{1}[a-z0-9-]+)*\/[a-z][a-z0-9_-]*$/`")  # noqa: E501

        self._rule = rule

    @property
    def schedule(self):
        """Gets the schedule of this DevicegroupSchemaScheduler.  # noqa: E501

        Name of the schedule that play/pauses the playbook instance automatically  # noqa: E501

        :return: The schedule of this DevicegroupSchemaScheduler.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this DevicegroupSchemaScheduler.

        Name of the schedule that play/pauses the playbook instance automatically  # noqa: E501

        :param schedule: The schedule of this DevicegroupSchemaScheduler.  # noqa: E501
        :type: str
        """
        if schedule is None:
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501
        if schedule is not None and len(schedule) > 64:
            raise ValueError("Invalid value for `schedule`, length must be less than or equal to `64`")  # noqa: E501
        if schedule is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', schedule):  # noqa: E501
            raise ValueError(r"Invalid value for `schedule`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._schedule = schedule

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DevicegroupSchemaScheduler, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DevicegroupSchemaScheduler):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
