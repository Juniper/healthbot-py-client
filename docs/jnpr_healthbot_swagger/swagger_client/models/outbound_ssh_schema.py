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


class OutboundSshSchema(object):
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
        'outbound_ssh': 'OutboundsshSchemaOutboundssh'
    }

    attribute_map = {
        'outbound_ssh': 'outbound-ssh'
    }

    def __init__(self, outbound_ssh=None):  # noqa: E501
        """OutboundSshSchema - a model defined in Swagger"""  # noqa: E501

        self._outbound_ssh = None
        self.discriminator = None

        if outbound_ssh is not None:
            self.outbound_ssh = outbound_ssh

    @property
    def outbound_ssh(self):
        """Gets the outbound_ssh of this OutboundSshSchema.  # noqa: E501


        :return: The outbound_ssh of this OutboundSshSchema.  # noqa: E501
        :rtype: OutboundsshSchemaOutboundssh
        """
        return self._outbound_ssh

    @outbound_ssh.setter
    def outbound_ssh(self, outbound_ssh):
        """Sets the outbound_ssh of this OutboundSshSchema.


        :param outbound_ssh: The outbound_ssh of this OutboundSshSchema.  # noqa: E501
        :type: OutboundsshSchemaOutboundssh
        """

        self._outbound_ssh = outbound_ssh

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
        if issubclass(OutboundSshSchema, dict):
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
        if not isinstance(other, OutboundSshSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
