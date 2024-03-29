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


class NetworkgroupSchemaNotification(object):
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
        'enable': 'list[object]',
        'major': 'list[str]',
        'minor': 'list[str]',
        'normal': 'list[str]'
    }

    attribute_map = {
        'enable': 'enable',
        'major': 'major',
        'minor': 'minor',
        'normal': 'normal'
    }

    def __init__(self, enable=None, major=None, minor=None, normal=None):  # noqa: E501
        """NetworkgroupSchemaNotification - a model defined in Swagger"""  # noqa: E501

        self._enable = None
        self._major = None
        self._minor = None
        self._normal = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if major is not None:
            self.major = major
        if minor is not None:
            self.minor = minor
        if normal is not None:
            self.normal = normal

    @property
    def enable(self):
        """Gets the enable of this NetworkgroupSchemaNotification.  # noqa: E501

        Turn on notifications  # noqa: E501

        :return: The enable of this NetworkgroupSchemaNotification.  # noqa: E501
        :rtype: list[object]
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this NetworkgroupSchemaNotification.

        Turn on notifications  # noqa: E501

        :param enable: The enable of this NetworkgroupSchemaNotification.  # noqa: E501
        :type: list[object]
        """

        self._enable = enable

    @property
    def major(self):
        """Gets the major of this NetworkgroupSchemaNotification.  # noqa: E501


        :return: The major of this NetworkgroupSchemaNotification.  # noqa: E501
        :rtype: list[str]
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this NetworkgroupSchemaNotification.


        :param major: The major of this NetworkgroupSchemaNotification.  # noqa: E501
        :type: list[str]
        """

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this NetworkgroupSchemaNotification.  # noqa: E501


        :return: The minor of this NetworkgroupSchemaNotification.  # noqa: E501
        :rtype: list[str]
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this NetworkgroupSchemaNotification.


        :param minor: The minor of this NetworkgroupSchemaNotification.  # noqa: E501
        :type: list[str]
        """

        self._minor = minor

    @property
    def normal(self):
        """Gets the normal of this NetworkgroupSchemaNotification.  # noqa: E501


        :return: The normal of this NetworkgroupSchemaNotification.  # noqa: E501
        :rtype: list[str]
        """
        return self._normal

    @normal.setter
    def normal(self, normal):
        """Sets the normal of this NetworkgroupSchemaNotification.


        :param normal: The normal of this NetworkgroupSchemaNotification.  # noqa: E501
        :type: list[str]
        """

        self._normal = normal

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
        if issubclass(NetworkgroupSchemaNotification, dict):
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
        if not isinstance(other, NetworkgroupSchemaNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
