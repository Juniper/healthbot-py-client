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


class SflowSchemaSflowField(object):
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
        'export_as': 'str',
        'field_name': 'str',
        'next_header': 'list[ERRORUNKNOWN]',
        'size_based_on_field': 'SflowSchemaSflowSizebasedonfield',
        'size_in_bits': 'int',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'export_as': 'export-as',
        'field_name': 'field-name',
        'next_header': 'next-header',
        'size_based_on_field': 'size-based-on-field',
        'size_in_bits': 'size-in-bits',
        'type': 'type'
    }

    def __init__(self, description=None, export_as=None, field_name=None, next_header=None, size_based_on_field=None, size_in_bits=None, type=None):  # noqa: E501
        """SflowSchemaSflowField - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._export_as = None
        self._field_name = None
        self._next_header = None
        self._size_based_on_field = None
        self._size_in_bits = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if export_as is not None:
            self.export_as = export_as
        self.field_name = field_name
        if next_header is not None:
            self.next_header = next_header
        if size_based_on_field is not None:
            self.size_based_on_field = size_based_on_field
        if size_in_bits is not None:
            self.size_in_bits = size_in_bits
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this SflowSchemaSflowField.  # noqa: E501

        Description of field  # noqa: E501

        :return: The description of this SflowSchemaSflowField.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SflowSchemaSflowField.

        Description of field  # noqa: E501

        :param description: The description of this SflowSchemaSflowField.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def export_as(self):
        """Gets the export_as of this SflowSchemaSflowField.  # noqa: E501

        Export field as tag/field  # noqa: E501

        :return: The export_as of this SflowSchemaSflowField.  # noqa: E501
        :rtype: str
        """
        return self._export_as

    @export_as.setter
    def export_as(self, export_as):
        """Sets the export_as of this SflowSchemaSflowField.

        Export field as tag/field  # noqa: E501

        :param export_as: The export_as of this SflowSchemaSflowField.  # noqa: E501
        :type: str
        """
        allowed_values = ["tag", "field"]  # noqa: E501
        if export_as not in allowed_values:
            raise ValueError(
                "Invalid value for `export_as` ({0}), must be one of {1}"  # noqa: E501
                .format(export_as, allowed_values)
            )

        self._export_as = export_as

    @property
    def field_name(self):
        """Gets the field_name of this SflowSchemaSflowField.  # noqa: E501

        Field name that needs to be exported  # noqa: E501

        :return: The field_name of this SflowSchemaSflowField.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this SflowSchemaSflowField.

        Field name that needs to be exported  # noqa: E501

        :param field_name: The field_name of this SflowSchemaSflowField.  # noqa: E501
        :type: str
        """
        if field_name is None:
            raise ValueError("Invalid value for `field_name`, must not be `None`")  # noqa: E501

        self._field_name = field_name

    @property
    def next_header(self):
        """Gets the next_header of this SflowSchemaSflowField.  # noqa: E501

        Flag to indicate current field points to next header format  # noqa: E501

        :return: The next_header of this SflowSchemaSflowField.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._next_header

    @next_header.setter
    def next_header(self, next_header):
        """Sets the next_header of this SflowSchemaSflowField.

        Flag to indicate current field points to next header format  # noqa: E501

        :param next_header: The next_header of this SflowSchemaSflowField.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._next_header = next_header

    @property
    def size_based_on_field(self):
        """Gets the size_based_on_field of this SflowSchemaSflowField.  # noqa: E501


        :return: The size_based_on_field of this SflowSchemaSflowField.  # noqa: E501
        :rtype: SflowSchemaSflowSizebasedonfield
        """
        return self._size_based_on_field

    @size_based_on_field.setter
    def size_based_on_field(self, size_based_on_field):
        """Sets the size_based_on_field of this SflowSchemaSflowField.


        :param size_based_on_field: The size_based_on_field of this SflowSchemaSflowField.  # noqa: E501
        :type: SflowSchemaSflowSizebasedonfield
        """

        self._size_based_on_field = size_based_on_field

    @property
    def size_in_bits(self):
        """Gets the size_in_bits of this SflowSchemaSflowField.  # noqa: E501

        Field size in bits  # noqa: E501

        :return: The size_in_bits of this SflowSchemaSflowField.  # noqa: E501
        :rtype: int
        """
        return self._size_in_bits

    @size_in_bits.setter
    def size_in_bits(self, size_in_bits):
        """Sets the size_in_bits of this SflowSchemaSflowField.

        Field size in bits  # noqa: E501

        :param size_in_bits: The size_in_bits of this SflowSchemaSflowField.  # noqa: E501
        :type: int
        """

        self._size_in_bits = size_in_bits

    @property
    def type(self):
        """Gets the type of this SflowSchemaSflowField.  # noqa: E501

        Data type of field  # noqa: E501

        :return: The type of this SflowSchemaSflowField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SflowSchemaSflowField.

        Data type of field  # noqa: E501

        :param type: The type of this SflowSchemaSflowField.  # noqa: E501
        :type: str
        """
        allowed_values = ["number", "string", "IpAddress", "hardwareAddr", "numbers", "ASPath"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(SflowSchemaSflowField, dict):
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
        if not isinstance(other, SflowSchemaSflowField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
