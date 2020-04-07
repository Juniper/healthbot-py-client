# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IngestsettingsSchemaIngestsettingsSyslogConstant(object):
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
        'description': 'str',
        'name': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, description=None, name=None, type=None, value=None):  # noqa: E501
        """IngestsettingsSchemaIngestsettingsSyslogConstant - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._name = None
        self._type = None
        self._value = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name
        if type is not None:
            self.type = type
        self.value = value

    @property
    def description(self):
        """Gets the description of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501

        Constant description  # noqa: E501

        :return: The description of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IngestsettingsSchemaIngestsettingsSyslogConstant.

        Constant description  # noqa: E501

        :param description: The description of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501

        Constant field name  # noqa: E501

        :return: The name of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IngestsettingsSchemaIngestsettingsSyslogConstant.

        Constant field name  # noqa: E501

        :param name: The name of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501


        :return: The type of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IngestsettingsSchemaIngestsettingsSyslogConstant.


        :param type: The type of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501
        :type: str
        """
        allowed_values = ["integer", "float", "string"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501

        Value of the constant  # noqa: E501

        :return: The value of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IngestsettingsSchemaIngestsettingsSyslogConstant.

        Value of the constant  # noqa: E501

        :param value: The value of this IngestsettingsSchemaIngestsettingsSyslogConstant.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IngestsettingsSchemaIngestsettingsSyslogConstant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other