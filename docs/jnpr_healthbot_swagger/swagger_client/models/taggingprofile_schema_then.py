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


class TaggingprofileSchemaThen(object):
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
        'add_field': 'list[TaggingprofileSchemaThenAddfield]',
        'add_key': 'list[TaggingprofileSchemaThenAddkey]',
        'next': 'list[object]'
    }

    attribute_map = {
        'add_field': 'add-field',
        'add_key': 'add-key',
        'next': 'next'
    }

    def __init__(self, add_field=None, add_key=None, next=None):  # noqa: E501
        """TaggingprofileSchemaThen - a model defined in Swagger"""  # noqa: E501

        self._add_field = None
        self._add_key = None
        self._next = None
        self.discriminator = None

        if add_field is not None:
            self.add_field = add_field
        if add_key is not None:
            self.add_key = add_key
        if next is not None:
            self.next = next

    @property
    def add_field(self):
        """Gets the add_field of this TaggingprofileSchemaThen.  # noqa: E501


        :return: The add_field of this TaggingprofileSchemaThen.  # noqa: E501
        :rtype: list[TaggingprofileSchemaThenAddfield]
        """
        return self._add_field

    @add_field.setter
    def add_field(self, add_field):
        """Sets the add_field of this TaggingprofileSchemaThen.


        :param add_field: The add_field of this TaggingprofileSchemaThen.  # noqa: E501
        :type: list[TaggingprofileSchemaThenAddfield]
        """

        self._add_field = add_field

    @property
    def add_key(self):
        """Gets the add_key of this TaggingprofileSchemaThen.  # noqa: E501


        :return: The add_key of this TaggingprofileSchemaThen.  # noqa: E501
        :rtype: list[TaggingprofileSchemaThenAddkey]
        """
        return self._add_key

    @add_key.setter
    def add_key(self, add_key):
        """Sets the add_key of this TaggingprofileSchemaThen.


        :param add_key: The add_key of this TaggingprofileSchemaThen.  # noqa: E501
        :type: list[TaggingprofileSchemaThenAddkey]
        """

        self._add_key = add_key

    @property
    def next(self):
        """Gets the next of this TaggingprofileSchemaThen.  # noqa: E501

        Continue evaluating next term in the policy  # noqa: E501

        :return: The next of this TaggingprofileSchemaThen.  # noqa: E501
        :rtype: list[object]
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this TaggingprofileSchemaThen.

        Continue evaluating next term in the policy  # noqa: E501

        :param next: The next of this TaggingprofileSchemaThen.  # noqa: E501
        :type: list[object]
        """

        self._next = next

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
        if issubclass(TaggingprofileSchemaThen, dict):
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
        if not isinstance(other, TaggingprofileSchemaThen):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
