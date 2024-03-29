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


class TopicSchemaWhereArgument(object):
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
        'argument_name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'argument_name': 'argument-name',
        'value': 'value'
    }

    def __init__(self, argument_name=None, value=None):  # noqa: E501
        """TopicSchemaWhereArgument - a model defined in Swagger"""  # noqa: E501

        self._argument_name = None
        self._value = None
        self.discriminator = None

        self.argument_name = argument_name
        self.value = value

    @property
    def argument_name(self):
        """Gets the argument_name of this TopicSchemaWhereArgument.  # noqa: E501

        Name of the argument. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The argument_name of this TopicSchemaWhereArgument.  # noqa: E501
        :rtype: str
        """
        return self._argument_name

    @argument_name.setter
    def argument_name(self, argument_name):
        """Sets the argument_name of this TopicSchemaWhereArgument.

        Name of the argument. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param argument_name: The argument_name of this TopicSchemaWhereArgument.  # noqa: E501
        :type: str
        """
        if argument_name is None:
            raise ValueError("Invalid value for `argument_name`, must not be `None`")  # noqa: E501
        if argument_name is not None and len(argument_name) > 64:
            raise ValueError("Invalid value for `argument_name`, length must be less than or equal to `64`")  # noqa: E501
        if argument_name is not None and len(argument_name) < 1:
            raise ValueError("Invalid value for `argument_name`, length must be greater than or equal to `1`")  # noqa: E501
        if argument_name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', argument_name):  # noqa: E501
            raise ValueError("Invalid value for `argument_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._argument_name = argument_name

    @property
    def value(self):
        """Gets the value of this TopicSchemaWhereArgument.  # noqa: E501

        Argument value  # noqa: E501

        :return: The value of this TopicSchemaWhereArgument.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TopicSchemaWhereArgument.

        Argument value  # noqa: E501

        :param value: The value of this TopicSchemaWhereArgument.  # noqa: E501
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
        if issubclass(TopicSchemaWhereArgument, dict):
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
        if not isinstance(other, TopicSchemaWhereArgument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
