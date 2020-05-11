# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TsdbSchema(object):
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
        'dedicate': 'bool',
        'nodes': 'list[str]',
        'replication_factor': 'int'
    }

    attribute_map = {
        'dedicate': 'dedicate',
        'nodes': 'nodes',
        'replication_factor': 'replication-factor'
    }

    def __init__(self, dedicate=None, nodes=None, replication_factor=None):  # noqa: E501
        """TsdbSchema - a model defined in Swagger"""  # noqa: E501

        self._dedicate = None
        self._nodes = None
        self._replication_factor = None
        self.discriminator = None

        if dedicate is not None:
            self.dedicate = dedicate
        if nodes is not None:
            self.nodes = nodes
        if replication_factor is not None:
            self.replication_factor = replication_factor

    @property
    def dedicate(self):
        """Gets the dedicate of this TsdbSchema.  # noqa: E501

        Dedicate given nodes only for tsdb instances. No other services will be spawned on tsdb nodes when set to true  # noqa: E501

        :return: The dedicate of this TsdbSchema.  # noqa: E501
        :rtype: bool
        """
        return self._dedicate

    @dedicate.setter
    def dedicate(self, dedicate):
        """Sets the dedicate of this TsdbSchema.

        Dedicate given nodes only for tsdb instances. No other services will be spawned on tsdb nodes when set to true  # noqa: E501

        :param dedicate: The dedicate of this TsdbSchema.  # noqa: E501
        :type: bool
        """

        self._dedicate = dedicate

    @property
    def nodes(self):
        """Gets the nodes of this TsdbSchema.  # noqa: E501


        :return: The nodes of this TsdbSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this TsdbSchema.


        :param nodes: The nodes of this TsdbSchema.  # noqa: E501
        :type: list[str]
        """

        self._nodes = nodes

    @property
    def replication_factor(self):
        """Gets the replication_factor of this TsdbSchema.  # noqa: E501

        High availability. Number of copies of data to be stored  # noqa: E501

        :return: The replication_factor of this TsdbSchema.  # noqa: E501
        :rtype: int
        """
        return self._replication_factor

    @replication_factor.setter
    def replication_factor(self, replication_factor):
        """Sets the replication_factor of this TsdbSchema.

        High availability. Number of copies of data to be stored  # noqa: E501

        :param replication_factor: The replication_factor of this TsdbSchema.  # noqa: E501
        :type: int
        """

        self._replication_factor = replication_factor

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
        if issubclass(TsdbSchema, dict):
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
        if not isinstance(other, TsdbSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other