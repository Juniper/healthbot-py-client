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


class PinGraphsQueryGroupByTagKeys(object):
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
        'tag_key': 'str',
        'tag_key_datatype': 'str'
    }

    attribute_map = {
        'tag_key': 'tag_key',
        'tag_key_datatype': 'tag_key_datatype'
    }

    def __init__(self, tag_key=None, tag_key_datatype=None):  # noqa: E501
        """PinGraphsQueryGroupByTagKeys - a model defined in Swagger"""  # noqa: E501

        self._tag_key = None
        self._tag_key_datatype = None
        self.discriminator = None

        if tag_key is not None:
            self.tag_key = tag_key
        if tag_key_datatype is not None:
            self.tag_key_datatype = tag_key_datatype

    @property
    def tag_key(self):
        """Gets the tag_key of this PinGraphsQueryGroupByTagKeys.  # noqa: E501

        Tag key value  # noqa: E501

        :return: The tag_key of this PinGraphsQueryGroupByTagKeys.  # noqa: E501
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        """Sets the tag_key of this PinGraphsQueryGroupByTagKeys.

        Tag key value  # noqa: E501

        :param tag_key: The tag_key of this PinGraphsQueryGroupByTagKeys.  # noqa: E501
        :type: str
        """

        self._tag_key = tag_key

    @property
    def tag_key_datatype(self):
        """Gets the tag_key_datatype of this PinGraphsQueryGroupByTagKeys.  # noqa: E501

        Tag key's datatype  # noqa: E501

        :return: The tag_key_datatype of this PinGraphsQueryGroupByTagKeys.  # noqa: E501
        :rtype: str
        """
        return self._tag_key_datatype

    @tag_key_datatype.setter
    def tag_key_datatype(self, tag_key_datatype):
        """Sets the tag_key_datatype of this PinGraphsQueryGroupByTagKeys.

        Tag key's datatype  # noqa: E501

        :param tag_key_datatype: The tag_key_datatype of this PinGraphsQueryGroupByTagKeys.  # noqa: E501
        :type: str
        """

        self._tag_key_datatype = tag_key_datatype

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
        if issubclass(PinGraphsQueryGroupByTagKeys, dict):
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
        if not isinstance(other, PinGraphsQueryGroupByTagKeys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other