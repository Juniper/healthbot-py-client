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


class RuleSchemaSflow(object):
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
        'sensor_name': 'str'
    }

    attribute_map = {
        'sensor_name': 'sensor-name'
    }

    def __init__(self, sensor_name=None):  # noqa: E501
        """RuleSchemaSflow - a model defined in Swagger"""  # noqa: E501

        self._sensor_name = None
        self.discriminator = None

        self.sensor_name = sensor_name

    @property
    def sensor_name(self):
        """Gets the sensor_name of this RuleSchemaSflow.  # noqa: E501

        Sensor to subscribe  # noqa: E501

        :return: The sensor_name of this RuleSchemaSflow.  # noqa: E501
        :rtype: str
        """
        return self._sensor_name

    @sensor_name.setter
    def sensor_name(self, sensor_name):
        """Sets the sensor_name of this RuleSchemaSflow.

        Sensor to subscribe  # noqa: E501

        :param sensor_name: The sensor_name of this RuleSchemaSflow.  # noqa: E501
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
        if issubclass(RuleSchemaSflow, dict):
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
        if not isinstance(other, RuleSchemaSflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
