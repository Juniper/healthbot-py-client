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


class RuleSchemaOpenconfig(object):
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
        'sensor_name': 'str'
    }

    attribute_map = {
        'frequency': 'frequency',
        'sensor_name': 'sensor-name'
    }

    def __init__(self, frequency=None, sensor_name=None):  # noqa: E501
        """RuleSchemaOpenconfig - a model defined in Swagger"""  # noqa: E501

        self._frequency = None
        self._sensor_name = None
        self.discriminator = None

        self.frequency = frequency
        self.sensor_name = sensor_name

    @property
    def frequency(self):
        """Gets the frequency of this RuleSchemaOpenconfig.  # noqa: E501

        Sensor subscription duration. Specify integer >= 0 followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s. A frequency of zero should be used only in case of events subscription  # noqa: E501

        :return: The frequency of this RuleSchemaOpenconfig.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this RuleSchemaOpenconfig.

        Sensor subscription duration. Specify integer >= 0 followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s. A frequency of zero should be used only in case of events subscription  # noqa: E501

        :param frequency: The frequency of this RuleSchemaOpenconfig.  # noqa: E501
        :type: str
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501
        if frequency is not None and not re.search(r'^[0-9]+[smhdwy]$', frequency):  # noqa: E501
            raise ValueError(r"Invalid value for `frequency`, must be a follow pattern or equal to `/^[0-9]+[smhdwy]$/`")  # noqa: E501

        self._frequency = frequency

    @property
    def sensor_name(self):
        """Gets the sensor_name of this RuleSchemaOpenconfig.  # noqa: E501

        Sensor to subscribe  # noqa: E501

        :return: The sensor_name of this RuleSchemaOpenconfig.  # noqa: E501
        :rtype: str
        """
        return self._sensor_name

    @sensor_name.setter
    def sensor_name(self, sensor_name):
        """Sets the sensor_name of this RuleSchemaOpenconfig.

        Sensor to subscribe  # noqa: E501

        :param sensor_name: The sensor_name of this RuleSchemaOpenconfig.  # noqa: E501
        :type: str
        """
        if sensor_name is None:
            raise ValueError("Invalid value for `sensor_name`, must not be `None`")  # noqa: E501
        if sensor_name is not None and not re.search(r'^\\S+$', sensor_name):  # noqa: E501
            raise ValueError(r"Invalid value for `sensor_name`, must be a follow pattern or equal to `/^\\S+$/`")  # noqa: E501

        self._sensor_name = sensor_name

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
        if issubclass(RuleSchemaOpenconfig, dict):
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
        if not isinstance(other, RuleSchemaOpenconfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
