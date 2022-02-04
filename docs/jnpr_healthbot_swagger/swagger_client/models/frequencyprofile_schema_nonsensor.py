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


class FrequencyprofileSchemaNonsensor(object):
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
        'frequency': 'str',
        'rule_name': 'str'
    }

    attribute_map = {
        'frequency': 'frequency',
        'rule_name': 'rule-name'
    }

    def __init__(self, frequency=None, rule_name=None):  # noqa: E501
        """FrequencyprofileSchemaNonsensor - a model defined in Swagger"""  # noqa: E501

        self._frequency = None
        self._rule_name = None
        self.discriminator = None

        self.frequency = frequency
        self.rule_name = rule_name

    @property
    def frequency(self):
        """Gets the frequency of this FrequencyprofileSchemaNonsensor.  # noqa: E501

        Sensor subscription duration. Specify integer >= 0 followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s. A frequency of zero should be used only in case of events subscription  # noqa: E501

        :return: The frequency of this FrequencyprofileSchemaNonsensor.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this FrequencyprofileSchemaNonsensor.

        Sensor subscription duration. Specify integer >= 0 followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s. A frequency of zero should be used only in case of events subscription  # noqa: E501

        :param frequency: The frequency of this FrequencyprofileSchemaNonsensor.  # noqa: E501
        :type: str
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501
        if frequency is not None and not re.search(r'^[0-9]+(seconds|minutes|hours|days|weeks|years)$', frequency):  # noqa: E501
            raise ValueError("Invalid value for `frequency`, must be a follow pattern or equal to `/^[0-9]+(seconds|minutes|hours|days|weeks|years)$/`")  # noqa: E501

        self._frequency = frequency

    @property
    def rule_name(self):
        """Gets the rule_name of this FrequencyprofileSchemaNonsensor.  # noqa: E501

        Name of non-sensor or network rule i.e topic-name/rule-name  # noqa: E501

        :return: The rule_name of this FrequencyprofileSchemaNonsensor.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this FrequencyprofileSchemaNonsensor.

        Name of non-sensor or network rule i.e topic-name/rule-name  # noqa: E501

        :param rule_name: The rule_name of this FrequencyprofileSchemaNonsensor.  # noqa: E501
        :type: str
        """
        if rule_name is None:
            raise ValueError("Invalid value for `rule_name`, must not be `None`")  # noqa: E501

        self._rule_name = rule_name

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
        if issubclass(FrequencyprofileSchemaNonsensor, dict):
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
        if not isinstance(other, FrequencyprofileSchemaNonsensor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
