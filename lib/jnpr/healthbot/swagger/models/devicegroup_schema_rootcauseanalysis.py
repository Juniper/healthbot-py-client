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


class DevicegroupSchemaRootcauseanalysis(object):
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
        'no_rca': 'list[object]',
        'dynamic_resources': 'list[str]',
        'exclude_resources': 'list[str]'
    }

    attribute_map = {
        'no_rca': 'no-rca',
        'dynamic_resources': 'dynamic-resources',
        'exclude_resources': 'exclude-resources'
    }

    def __init__(self, no_rca=None, dynamic_resources=None, exclude_resources=None):  # noqa: E501
        """DevicegroupSchemaRootcauseanalysis - a model defined in Swagger"""  # noqa: E501

        self._no_rca = None
        self._dynamic_resources = None
        self._exclude_resources = None
        self.discriminator = None

        if no_rca is not None:
            self.no_rca = no_rca
        if dynamic_resources is not None:
            self.dynamic_resources = dynamic_resources
        if exclude_resources is not None:
            self.exclude_resources = exclude_resources

    @property
    def no_rca(self):
        """Gets the no_rca of this DevicegroupSchemaRootcauseanalysis.  # noqa: E501

        Disable Root Cause analysis  # noqa: E501

        :return: The no_rca of this DevicegroupSchemaRootcauseanalysis.  # noqa: E501
        :rtype: list[object]
        """
        return self._no_rca

    @no_rca.setter
    def no_rca(self, no_rca):
        """Sets the no_rca of this DevicegroupSchemaRootcauseanalysis.

        Disable Root Cause analysis  # noqa: E501

        :param no_rca: The no_rca of this DevicegroupSchemaRootcauseanalysis.  # noqa: E501
        :type: list[object]
        """

        self._no_rca = no_rca

    @property
    def dynamic_resources(self):
        """Gets the dynamic_resources of this DevicegroupSchemaRootcauseanalysis.  # noqa: E501


        :return: The dynamic_resources of this DevicegroupSchemaRootcauseanalysis.  # noqa: E501
        :rtype: list[str]
        """
        return self._dynamic_resources

    @dynamic_resources.setter
    def dynamic_resources(self, dynamic_resources):
        """Sets the dynamic_resources of this DevicegroupSchemaRootcauseanalysis.


        :param dynamic_resources: The dynamic_resources of this DevicegroupSchemaRootcauseanalysis.  # noqa: E501
        :type: list[str]
        """

        self._dynamic_resources = dynamic_resources

    @property
    def exclude_resources(self):
        """Gets the exclude_resources of this DevicegroupSchemaRootcauseanalysis.  # noqa: E501


        :return: The exclude_resources of this DevicegroupSchemaRootcauseanalysis.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_resources

    @exclude_resources.setter
    def exclude_resources(self, exclude_resources):
        """Sets the exclude_resources of this DevicegroupSchemaRootcauseanalysis.


        :param exclude_resources: The exclude_resources of this DevicegroupSchemaRootcauseanalysis.  # noqa: E501
        :type: list[str]
        """

        self._exclude_resources = exclude_resources

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
        if issubclass(DevicegroupSchemaRootcauseanalysis, dict):
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
        if not isinstance(other, DevicegroupSchemaRootcauseanalysis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other