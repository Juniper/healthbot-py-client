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


class PatternSchema(object):
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
        'constant': 'list[PatternSchemaConstant]',
        'description': 'str',
        'event_id': 'str',
        'field': 'list[PatternSchemaField]',
        'filter': 'str',
        'filter_type': 'str',
        'key_fields': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'constant': 'constant',
        'description': 'description',
        'event_id': 'event-id',
        'field': 'field',
        'filter': 'filter',
        'filter_type': 'filter-type',
        'key_fields': 'key-fields',
        'name': 'name'
    }

    def __init__(self, constant=None, description=None, event_id=None, field=None, filter=None, filter_type=None, key_fields=None, name=None):  # noqa: E501
        """PatternSchema - a model defined in Swagger"""  # noqa: E501

        self._constant = None
        self._description = None
        self._event_id = None
        self._field = None
        self._filter = None
        self._filter_type = None
        self._key_fields = None
        self._name = None
        self.discriminator = None

        if constant is not None:
            self.constant = constant
        if description is not None:
            self.description = description
        self.event_id = event_id
        if field is not None:
            self.field = field
        if filter is not None:
            self.filter = filter
        if filter_type is not None:
            self.filter_type = filter_type
        if key_fields is not None:
            self.key_fields = key_fields
        self.name = name

    @property
    def constant(self):
        """Gets the constant of this PatternSchema.  # noqa: E501

        Constant details  # noqa: E501

        :return: The constant of this PatternSchema.  # noqa: E501
        :rtype: list[PatternSchemaConstant]
        """
        return self._constant

    @constant.setter
    def constant(self, constant):
        """Sets the constant of this PatternSchema.

        Constant details  # noqa: E501

        :param constant: The constant of this PatternSchema.  # noqa: E501
        :type: list[PatternSchemaConstant]
        """

        self._constant = constant

    @property
    def description(self):
        """Gets the description of this PatternSchema.  # noqa: E501

        Pattern description  # noqa: E501

        :return: The description of this PatternSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PatternSchema.

        Pattern description  # noqa: E501

        :param description: The description of this PatternSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def event_id(self):
        """Gets the event_id of this PatternSchema.  # noqa: E501

        Event id that identifies a log uniquely. Field names also can be part of event-id. Example my-event+$field1  # noqa: E501

        :return: The event_id of this PatternSchema.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this PatternSchema.

        Event id that identifies a log uniquely. Field names also can be part of event-id. Example my-event+$field1  # noqa: E501

        :param event_id: The event_id of this PatternSchema.  # noqa: E501
        :type: str
        """
        if event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id

    @property
    def field(self):
        """Gets the field of this PatternSchema.  # noqa: E501

        Field details  # noqa: E501

        :return: The field of this PatternSchema.  # noqa: E501
        :rtype: list[PatternSchemaField]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this PatternSchema.

        Field details  # noqa: E501

        :param field: The field of this PatternSchema.  # noqa: E501
        :type: list[PatternSchemaField]
        """

        self._field = field

    @property
    def filter(self):
        """Gets the filter of this PatternSchema.  # noqa: E501

        Filter to match a log line  # noqa: E501

        :return: The filter of this PatternSchema.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this PatternSchema.

        Filter to match a log line  # noqa: E501

        :param filter: The filter of this PatternSchema.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def filter_type(self):
        """Gets the filter_type of this PatternSchema.  # noqa: E501

        Filter type, default is grok  # noqa: E501

        :return: The filter_type of this PatternSchema.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this PatternSchema.

        Filter type, default is grok  # noqa: E501

        :param filter_type: The filter_type of this PatternSchema.  # noqa: E501
        :type: str
        """
        allowed_values = ["grok"]  # noqa: E501
        if filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `filter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(filter_type, allowed_values)
            )

        self._filter_type = filter_type

    @property
    def key_fields(self):
        """Gets the key_fields of this PatternSchema.  # noqa: E501


        :return: The key_fields of this PatternSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._key_fields

    @key_fields.setter
    def key_fields(self, key_fields):
        """Sets the key_fields of this PatternSchema.


        :param key_fields: The key_fields of this PatternSchema.  # noqa: E501
        :type: list[str]
        """

        self._key_fields = key_fields

    @property
    def name(self):
        """Gets the name of this PatternSchema.  # noqa: E501

        Name of a pattern. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The name of this PatternSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatternSchema.

        Name of a pattern. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param name: The name of this PatternSchema.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._name = name

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
        if issubclass(PatternSchema, dict):
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
        if not isinstance(other, PatternSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
