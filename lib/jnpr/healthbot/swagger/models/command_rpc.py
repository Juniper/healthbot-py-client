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


class CommandRpc(object):
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
        'args': 'dict(str, str)',
        'filename': 'str',
        'host': 'str',
        'password': 'str',
        'tablename': 'str',
        'target': 'str',
        'username': 'str'
    }

    attribute_map = {
        'args': 'args',
        'filename': 'filename',
        'host': 'host',
        'password': 'password',
        'tablename': 'tablename',
        'target': 'target',
        'username': 'username'
    }

    def __init__(self, args=None, filename=None, host=None, password=None, tablename=None, target=None, username=None):  # noqa: E501
        """CommandRpc - a model defined in Swagger"""  # noqa: E501

        self._args = None
        self._filename = None
        self._host = None
        self._password = None
        self._tablename = None
        self._target = None
        self._username = None
        self.discriminator = None

        if args is not None:
            self.args = args
        self.filename = filename
        self.host = host
        self.password = password
        self.tablename = tablename
        if target is not None:
            self.target = target
        self.username = username

    @property
    def args(self):
        """Gets the args of this CommandRpc.  # noqa: E501

        Optional key/value pair arguments to table  # noqa: E501

        :return: The args of this CommandRpc.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this CommandRpc.

        Optional key/value pair arguments to table  # noqa: E501

        :param args: The args of this CommandRpc.  # noqa: E501
        :type: dict(str, str)
        """

        self._args = args

    @property
    def filename(self):
        """Gets the filename of this CommandRpc.  # noqa: E501

        Command-rpc table filename in which the table is defined  # noqa: E501

        :return: The filename of this CommandRpc.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this CommandRpc.

        Command-rpc table filename in which the table is defined  # noqa: E501

        :param filename: The filename of this CommandRpc.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def host(self):
        """Gets the host of this CommandRpc.  # noqa: E501

        Host name or ip-address of the device in which command will be inspected  # noqa: E501

        :return: The host of this CommandRpc.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CommandRpc.

        Host name or ip-address of the device in which command will be inspected  # noqa: E501

        :param host: The host of this CommandRpc.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def password(self):
        """Gets the password of this CommandRpc.  # noqa: E501

        Password to connect to device  # noqa: E501

        :return: The password of this CommandRpc.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CommandRpc.

        Password to connect to device  # noqa: E501

        :param password: The password of this CommandRpc.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def tablename(self):
        """Gets the tablename of this CommandRpc.  # noqa: E501

        Command-rpc table name  # noqa: E501

        :return: The tablename of this CommandRpc.  # noqa: E501
        :rtype: str
        """
        return self._tablename

    @tablename.setter
    def tablename(self, tablename):
        """Sets the tablename of this CommandRpc.

        Command-rpc table name  # noqa: E501

        :param tablename: The tablename of this CommandRpc.  # noqa: E501
        :type: str
        """
        if tablename is None:
            raise ValueError("Invalid value for `tablename`, must not be `None`")  # noqa: E501

        self._tablename = tablename

    @property
    def target(self):
        """Gets the target of this CommandRpc.  # noqa: E501

        To run command on FPC, specifiy FPC target  # noqa: E501

        :return: The target of this CommandRpc.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this CommandRpc.

        To run command on FPC, specifiy FPC target  # noqa: E501

        :param target: The target of this CommandRpc.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def username(self):
        """Gets the username of this CommandRpc.  # noqa: E501

        Username to connect to device  # noqa: E501

        :return: The username of this CommandRpc.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CommandRpc.

        Username to connect to device  # noqa: E501

        :param username: The username of this CommandRpc.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if issubclass(CommandRpc, dict):
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
        if not isinstance(other, CommandRpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
