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


class SshKeyProfileSchema(object):
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
        'name': 'str',
        'ssh_private_key_file': 'str',
        'ssh_private_key_passphrase': 'str'
    }

    attribute_map = {
        'name': 'name',
        'ssh_private_key_file': 'ssh-private-key-file',
        'ssh_private_key_passphrase': 'ssh-private-key-passphrase'
    }

    def __init__(self, name=None, ssh_private_key_file=None, ssh_private_key_passphrase=None):  # noqa: E501
        """SshKeyProfileSchema - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._ssh_private_key_file = None
        self._ssh_private_key_passphrase = None
        self.discriminator = None

        self.name = name
        self.ssh_private_key_file = ssh_private_key_file
        self.ssh_private_key_passphrase = ssh_private_key_passphrase

    @property
    def name(self):
        """Gets the name of this SshKeyProfileSchema.  # noqa: E501

        SSH Key profile name. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The name of this SshKeyProfileSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SshKeyProfileSchema.

        SSH Key profile name. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param name: The name of this SshKeyProfileSchema.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def ssh_private_key_file(self):
        """Gets the ssh_private_key_file of this SshKeyProfileSchema.  # noqa: E501

        SSH private key file name  # noqa: E501

        :return: The ssh_private_key_file of this SshKeyProfileSchema.  # noqa: E501
        :rtype: str
        """
        return self._ssh_private_key_file

    @ssh_private_key_file.setter
    def ssh_private_key_file(self, ssh_private_key_file):
        """Sets the ssh_private_key_file of this SshKeyProfileSchema.

        SSH private key file name  # noqa: E501

        :param ssh_private_key_file: The ssh_private_key_file of this SshKeyProfileSchema.  # noqa: E501
        :type: str
        """
        if ssh_private_key_file is None:
            raise ValueError("Invalid value for `ssh_private_key_file`, must not be `None`")  # noqa: E501

        self._ssh_private_key_file = ssh_private_key_file

    @property
    def ssh_private_key_passphrase(self):
        """Gets the ssh_private_key_passphrase of this SshKeyProfileSchema.  # noqa: E501

        SSH private key passphrase  # noqa: E501

        :return: The ssh_private_key_passphrase of this SshKeyProfileSchema.  # noqa: E501
        :rtype: str
        """
        return self._ssh_private_key_passphrase

    @ssh_private_key_passphrase.setter
    def ssh_private_key_passphrase(self, ssh_private_key_passphrase):
        """Sets the ssh_private_key_passphrase of this SshKeyProfileSchema.

        SSH private key passphrase  # noqa: E501

        :param ssh_private_key_passphrase: The ssh_private_key_passphrase of this SshKeyProfileSchema.  # noqa: E501
        :type: str
        """
        if ssh_private_key_passphrase is None:
            raise ValueError("Invalid value for `ssh_private_key_passphrase`, must not be `None`")  # noqa: E501

        self._ssh_private_key_passphrase = ssh_private_key_passphrase

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
        if issubclass(SshKeyProfileSchema, dict):
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
        if not isinstance(other, SshKeyProfileSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
