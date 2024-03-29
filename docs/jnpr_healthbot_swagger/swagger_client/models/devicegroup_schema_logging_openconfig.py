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


class DevicegroupSchemaLoggingOpenconfig(object):
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
        'daemons': 'list[str]',
        'log_level': 'str'
    }

    attribute_map = {
        'daemons': 'daemons',
        'log_level': 'log-level'
    }

    def __init__(self, daemons=None, log_level=None):  # noqa: E501
        """DevicegroupSchemaLoggingOpenconfig - a model defined in Swagger"""  # noqa: E501

        self._daemons = None
        self._log_level = None
        self.discriminator = None

        if daemons is not None:
            self.daemons = daemons
        self.log_level = log_level

    @property
    def daemons(self):
        """Gets the daemons of this DevicegroupSchemaLoggingOpenconfig.  # noqa: E501


        :return: The daemons of this DevicegroupSchemaLoggingOpenconfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._daemons

    @daemons.setter
    def daemons(self, daemons):
        """Sets the daemons of this DevicegroupSchemaLoggingOpenconfig.


        :param daemons: The daemons of this DevicegroupSchemaLoggingOpenconfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ingest", "tand", "publishd"]  # noqa: E501
        if not set(daemons).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `daemons` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(daemons) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._daemons = daemons

    @property
    def log_level(self):
        """Gets the log_level of this DevicegroupSchemaLoggingOpenconfig.  # noqa: E501

        Set the logging level  # noqa: E501

        :return: The log_level of this DevicegroupSchemaLoggingOpenconfig.  # noqa: E501
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this DevicegroupSchemaLoggingOpenconfig.

        Set the logging level  # noqa: E501

        :param log_level: The log_level of this DevicegroupSchemaLoggingOpenconfig.  # noqa: E501
        :type: str
        """
        if log_level is None:
            raise ValueError("Invalid value for `log_level`, must not be `None`")  # noqa: E501
        allowed_values = ["error", "debug", "warn", "info"]  # noqa: E501
        if log_level not in allowed_values:
            raise ValueError(
                "Invalid value for `log_level` ({0}), must be one of {1}"  # noqa: E501
                .format(log_level, allowed_values)
            )

        self._log_level = log_level

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
        if issubclass(DevicegroupSchemaLoggingOpenconfig, dict):
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
        if not isinstance(other, DevicegroupSchemaLoggingOpenconfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
