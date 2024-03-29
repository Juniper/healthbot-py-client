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


class FlowRecordSchema(object):
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
        'enterprise': 'int',
        'field': 'list[SflowSchemaSflowField]',
        'format': 'int',
        'record_name': 'str'
    }

    attribute_map = {
        'enterprise': 'enterprise',
        'field': 'field',
        'format': 'format',
        'record_name': 'record-name'
    }

    def __init__(self, enterprise=None, field=None, format=None, record_name=None):  # noqa: E501
        """FlowRecordSchema - a model defined in Swagger"""  # noqa: E501

        self._enterprise = None
        self._field = None
        self._format = None
        self._record_name = None
        self.discriminator = None

        self.enterprise = enterprise
        self.field = field
        self.format = format
        self.record_name = record_name

    @property
    def enterprise(self):
        """Gets the enterprise of this FlowRecordSchema.  # noqa: E501

        Enterprise to which record belongs  # noqa: E501

        :return: The enterprise of this FlowRecordSchema.  # noqa: E501
        :rtype: int
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this FlowRecordSchema.

        Enterprise to which record belongs  # noqa: E501

        :param enterprise: The enterprise of this FlowRecordSchema.  # noqa: E501
        :type: int
        """
        if enterprise is None:
            raise ValueError("Invalid value for `enterprise`, must not be `None`")  # noqa: E501

        self._enterprise = enterprise

    @property
    def field(self):
        """Gets the field of this FlowRecordSchema.  # noqa: E501

        List of fields  # noqa: E501

        :return: The field of this FlowRecordSchema.  # noqa: E501
        :rtype: list[SflowSchemaSflowField]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this FlowRecordSchema.

        List of fields  # noqa: E501

        :param field: The field of this FlowRecordSchema.  # noqa: E501
        :type: list[SflowSchemaSflowField]
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def format(self):
        """Gets the format of this FlowRecordSchema.  # noqa: E501

        Format of record  # noqa: E501

        :return: The format of this FlowRecordSchema.  # noqa: E501
        :rtype: int
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this FlowRecordSchema.

        Format of record  # noqa: E501

        :param format: The format of this FlowRecordSchema.  # noqa: E501
        :type: int
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501

        self._format = format

    @property
    def record_name(self):
        """Gets the record_name of this FlowRecordSchema.  # noqa: E501

        Name of record  # noqa: E501

        :return: The record_name of this FlowRecordSchema.  # noqa: E501
        :rtype: str
        """
        return self._record_name

    @record_name.setter
    def record_name(self, record_name):
        """Sets the record_name of this FlowRecordSchema.

        Name of record  # noqa: E501

        :param record_name: The record_name of this FlowRecordSchema.  # noqa: E501
        :type: str
        """
        if record_name is None:
            raise ValueError("Invalid value for `record_name`, must not be `None`")  # noqa: E501

        self._record_name = record_name

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
        if issubclass(FlowRecordSchema, dict):
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
        if not isinstance(other, FlowRecordSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
