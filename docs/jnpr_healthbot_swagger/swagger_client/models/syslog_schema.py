# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SyslogSchema(object):
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
        'syslog': 'SyslogSchemaSyslog'
    }

    attribute_map = {
        'syslog': 'syslog'
    }

    def __init__(self, syslog=None):  # noqa: E501
        """SyslogSchema - a model defined in Swagger"""  # noqa: E501

        self._syslog = None
        self.discriminator = None

        if syslog is not None:
            self.syslog = syslog

    @property
    def syslog(self):
        """Gets the syslog of this SyslogSchema.  # noqa: E501


        :return: The syslog of this SyslogSchema.  # noqa: E501
        :rtype: SyslogSchemaSyslog
        """
        return self._syslog

    @syslog.setter
    def syslog(self, syslog):
        """Sets the syslog of this SyslogSchema.


        :param syslog: The syslog of this SyslogSchema.  # noqa: E501
        :type: SyslogSchemaSyslog
        """

        self._syslog = syslog

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
        if issubclass(SyslogSchema, dict):
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
        if not isinstance(other, SyslogSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
