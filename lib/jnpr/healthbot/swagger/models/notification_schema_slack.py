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


class NotificationSchemaSlack(object):
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
        'channel': 'str',
        'url': 'str'
    }

    attribute_map = {
        'channel': 'channel',
        'url': 'url'
    }

    def __init__(self, channel=None, url=None):  # noqa: E501
        """NotificationSchemaSlack - a model defined in Swagger"""  # noqa: E501

        self._channel = None
        self._url = None
        self.discriminator = None

        self.channel = channel
        self.url = url

    @property
    def channel(self):
        """Gets the channel of this NotificationSchemaSlack.  # noqa: E501

        Channel on which notification should be posted  # noqa: E501

        :return: The channel of this NotificationSchemaSlack.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this NotificationSchemaSlack.

        Channel on which notification should be posted  # noqa: E501

        :param channel: The channel of this NotificationSchemaSlack.  # noqa: E501
        :type: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def url(self):
        """Gets the url of this NotificationSchemaSlack.  # noqa: E501

        URL on which slack notification needs to be posted  # noqa: E501

        :return: The url of this NotificationSchemaSlack.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NotificationSchemaSlack.

        URL on which slack notification needs to be posted  # noqa: E501

        :param url: The url of this NotificationSchemaSlack.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if url is not None and not re.search('^(https):\/\/[^\\s\/$.?#].[^\\s]*$', url):  # noqa: E501
            raise ValueError(r"Invalid value for `url`, must be a follow pattern or equal to `/^(https):\/\/[^\\s\/$.?#].[^\\s]*$/`")  # noqa: E501

        self._url = url

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
        if issubclass(NotificationSchemaSlack, dict):
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
        if not isinstance(other, NotificationSchemaSlack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
