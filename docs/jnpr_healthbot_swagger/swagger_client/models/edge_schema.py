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


class EdgeSchema(object):
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
        'description': 'str',
        'edge_id': 'str',
        'edge_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'edge_id': 'edge-id',
        'edge_name': 'edge-name'
    }

    def __init__(self, description=None, edge_id=None, edge_name=None):  # noqa: E501
        """EdgeSchema - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._edge_id = None
        self._edge_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.edge_id = edge_id
        self.edge_name = edge_name

    @property
    def description(self):
        """Gets the description of this EdgeSchema.  # noqa: E501

        Description about the edge  # noqa: E501

        :return: The description of this EdgeSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EdgeSchema.

        Description about the edge  # noqa: E501

        :param description: The description of this EdgeSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def edge_id(self):
        """Gets the edge_id of this EdgeSchema.  # noqa: E501

        uuid of the edge in string  # noqa: E501

        :return: The edge_id of this EdgeSchema.  # noqa: E501
        :rtype: str
        """
        return self._edge_id

    @edge_id.setter
    def edge_id(self, edge_id):
        """Sets the edge_id of this EdgeSchema.

        uuid of the edge in string  # noqa: E501

        :param edge_id: The edge_id of this EdgeSchema.  # noqa: E501
        :type: str
        """
        if edge_id is None:
            raise ValueError("Invalid value for `edge_id`, must not be `None`")  # noqa: E501

        self._edge_id = edge_id

    @property
    def edge_name(self):
        """Gets the edge_name of this EdgeSchema.  # noqa: E501

        Name of the edge. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The edge_name of this EdgeSchema.  # noqa: E501
        :rtype: str
        """
        return self._edge_name

    @edge_name.setter
    def edge_name(self, edge_name):
        """Sets the edge_name of this EdgeSchema.

        Name of the edge. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param edge_name: The edge_name of this EdgeSchema.  # noqa: E501
        :type: str
        """
        if edge_name is None:
            raise ValueError("Invalid value for `edge_name`, must not be `None`")  # noqa: E501
        if edge_name is not None and len(edge_name) > 64:
            raise ValueError("Invalid value for `edge_name`, length must be less than or equal to `64`")  # noqa: E501
        if edge_name is not None and len(edge_name) < 1:
            raise ValueError("Invalid value for `edge_name`, length must be greater than or equal to `1`")  # noqa: E501
        if edge_name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', edge_name):  # noqa: E501
            raise ValueError(r"Invalid value for `edge_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._edge_name = edge_name

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
        if issubclass(EdgeSchema, dict):
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
        if not isinstance(other, EdgeSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
