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


class InlineResponse2002(object):
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
        'access_token': 'str',
        'refresh_token': 'str',
        'refresh_token_expires': 'str',
        'token_expires': 'str'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'refresh_token': 'refreshToken',
        'refresh_token_expires': 'refreshTokenExpires',
        'token_expires': 'tokenExpires'
    }

    def __init__(self, access_token=None, refresh_token=None, refresh_token_expires=None, token_expires=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501

        self._access_token = None
        self._refresh_token = None
        self._refresh_token_expires = None
        self._token_expires = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if refresh_token_expires is not None:
            self.refresh_token_expires = refresh_token_expires
        if token_expires is not None:
            self.token_expires = token_expires

    @property
    def access_token(self):
        """Gets the access_token of this InlineResponse2002.  # noqa: E501

        Access token generated by system  # noqa: E501

        :return: The access_token of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this InlineResponse2002.

        Access token generated by system  # noqa: E501

        :param access_token: The access_token of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def refresh_token(self):
        """Gets the refresh_token of this InlineResponse2002.  # noqa: E501

        Refresh token generated by system  # noqa: E501

        :return: The refresh_token of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this InlineResponse2002.

        Refresh token generated by system  # noqa: E501

        :param refresh_token: The refresh_token of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def refresh_token_expires(self):
        """Gets the refresh_token_expires of this InlineResponse2002.  # noqa: E501

        Refresh token validity duration  # noqa: E501

        :return: The refresh_token_expires of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token_expires

    @refresh_token_expires.setter
    def refresh_token_expires(self, refresh_token_expires):
        """Sets the refresh_token_expires of this InlineResponse2002.

        Refresh token validity duration  # noqa: E501

        :param refresh_token_expires: The refresh_token_expires of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._refresh_token_expires = refresh_token_expires

    @property
    def token_expires(self):
        """Gets the token_expires of this InlineResponse2002.  # noqa: E501

        Access token validity duration  # noqa: E501

        :return: The token_expires of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._token_expires

    @token_expires.setter
    def token_expires(self, token_expires):
        """Sets the token_expires of this InlineResponse2002.

        Access token validity duration  # noqa: E501

        :param token_expires: The token_expires of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._token_expires = token_expires

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
        if issubclass(InlineResponse2002, dict):
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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
