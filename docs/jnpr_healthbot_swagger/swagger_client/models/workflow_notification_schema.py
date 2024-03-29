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


class WorkflowNotificationSchema(object):
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
        'tag': 'str',
        'payload': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'payload': 'payload'
    }

    def __init__(self, tag=None, payload=None):  # noqa: E501
        """WorkflowNotificationSchema - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._payload = None
        self.discriminator = None

        self.tag = tag
        if payload is not None:
            self.payload = payload

    @property
    def tag(self):
        """Gets the tag of this WorkflowNotificationSchema.  # noqa: E501

        Notification key tag  # noqa: E501

        :return: The tag of this WorkflowNotificationSchema.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this WorkflowNotificationSchema.

        Notification key tag  # noqa: E501

        :param tag: The tag of this WorkflowNotificationSchema.  # noqa: E501
        :type: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def payload(self):
        """Gets the payload of this WorkflowNotificationSchema.  # noqa: E501

        Payload of the notification  # noqa: E501

        :return: The payload of this WorkflowNotificationSchema.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this WorkflowNotificationSchema.

        Payload of the notification  # noqa: E501

        :param payload: The payload of this WorkflowNotificationSchema.  # noqa: E501
        :type: str
        """

        self._payload = payload

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
        if issubclass(WorkflowNotificationSchema, dict):
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
        if not isinstance(other, WorkflowNotificationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
