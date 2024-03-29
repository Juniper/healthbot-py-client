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


class RuleSchemaRulepropertiesSupporteddevicesJuniper(object):
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
        'operating_system': 'list[RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem]',
        'sensors': 'list[str]'
    }

    attribute_map = {
        'operating_system': 'operating-system',
        'sensors': 'sensors'
    }

    def __init__(self, operating_system=None, sensors=None):  # noqa: E501
        """RuleSchemaRulepropertiesSupporteddevicesJuniper - a model defined in Swagger"""  # noqa: E501

        self._operating_system = None
        self._sensors = None
        self.discriminator = None

        if operating_system is not None:
            self.operating_system = operating_system
        if sensors is not None:
            self.sensors = sensors

    @property
    def operating_system(self):
        """Gets the operating_system of this RuleSchemaRulepropertiesSupporteddevicesJuniper.  # noqa: E501

        Operating system of the device  # noqa: E501

        :return: The operating_system of this RuleSchemaRulepropertiesSupporteddevicesJuniper.  # noqa: E501
        :rtype: list[RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem]
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this RuleSchemaRulepropertiesSupporteddevicesJuniper.

        Operating system of the device  # noqa: E501

        :param operating_system: The operating_system of this RuleSchemaRulepropertiesSupporteddevicesJuniper.  # noqa: E501
        :type: list[RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem]
        """

        self._operating_system = operating_system

    @property
    def sensors(self):
        """Gets the sensors of this RuleSchemaRulepropertiesSupporteddevicesJuniper.  # noqa: E501


        :return: The sensors of this RuleSchemaRulepropertiesSupporteddevicesJuniper.  # noqa: E501
        :rtype: list[str]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this RuleSchemaRulepropertiesSupporteddevicesJuniper.


        :param sensors: The sensors of this RuleSchemaRulepropertiesSupporteddevicesJuniper.  # noqa: E501
        :type: list[str]
        """

        self._sensors = sensors

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
        if issubclass(RuleSchemaRulepropertiesSupporteddevicesJuniper, dict):
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
        if not isinstance(other, RuleSchemaRulepropertiesSupporteddevicesJuniper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
