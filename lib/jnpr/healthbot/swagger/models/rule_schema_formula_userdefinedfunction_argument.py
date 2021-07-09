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


class RuleSchemaFormulaUserdefinedfunctionArgument(object):
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
        'argument': 'str',
        'value': 'str'
    }

    attribute_map = {
        'argument': 'argument',
        'value': 'value'
    }

    def __init__(self, argument=None, value=None):  # noqa: E501
        """RuleSchemaFormulaUserdefinedfunctionArgument - a model defined in Swagger"""  # noqa: E501

        self._argument = None
        self._value = None
        self.discriminator = None

        self.argument = argument
        self.value = value

    @property
    def argument(self):
        """Gets the argument of this RuleSchemaFormulaUserdefinedfunctionArgument.  # noqa: E501

        Argument name  # noqa: E501

        :return: The argument of this RuleSchemaFormulaUserdefinedfunctionArgument.  # noqa: E501
        :rtype: str
        """
        return self._argument

    @argument.setter
    def argument(self, argument):
        """Sets the argument of this RuleSchemaFormulaUserdefinedfunctionArgument.

        Argument name  # noqa: E501

        :param argument: The argument of this RuleSchemaFormulaUserdefinedfunctionArgument.  # noqa: E501
        :type: str
        """
        if argument is None:
            raise ValueError("Invalid value for `argument`, must not be `None`")  # noqa: E501
        if argument is not None and len(argument) > 64:
            raise ValueError("Invalid value for `argument`, length must be less than or equal to `64`")  # noqa: E501
        if argument is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', argument):  # noqa: E501
            raise ValueError(r"Invalid value for `argument`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._argument = argument

    @property
    def value(self):
        """Gets the value of this RuleSchemaFormulaUserdefinedfunctionArgument.  # noqa: E501

        Argument value  # noqa: E501

        :return: The value of this RuleSchemaFormulaUserdefinedfunctionArgument.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RuleSchemaFormulaUserdefinedfunctionArgument.

        Argument value  # noqa: E501

        :param value: The value of this RuleSchemaFormulaUserdefinedfunctionArgument.  # noqa: E501
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
        if issubclass(RuleSchemaFormulaUserdefinedfunctionArgument, dict):
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
        if not isinstance(other, RuleSchemaFormulaUserdefinedfunctionArgument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
