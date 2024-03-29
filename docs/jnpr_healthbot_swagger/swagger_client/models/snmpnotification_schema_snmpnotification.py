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


class SnmpnotificationSchemaSnmpnotification(object):
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
        'engine_id': 'str',
        'port': 'int',
        'v3': 'SnmpnotificationSchemaSnmpnotificationV3'
    }

    attribute_map = {
        'engine_id': 'engine-id',
        'port': 'port',
        'v3': 'v3'
    }

    def __init__(self, engine_id=None, port=None, v3=None):  # noqa: E501
        """SnmpnotificationSchemaSnmpnotification - a model defined in Swagger"""  # noqa: E501

        self._engine_id = None
        self._port = None
        self._v3 = None
        self.discriminator = None

        if engine_id is not None:
            self.engine_id = engine_id
        if port is not None:
            self.port = port
        if v3 is not None:
            self.v3 = v3

    @property
    def engine_id(self):
        """Gets the engine_id of this SnmpnotificationSchemaSnmpnotification.  # noqa: E501

        Autogenerated Engine-id for Healthbot in Hex Format Eg: '80001f8880bd5b8d052eb40d6000000000'  # noqa: E501

        :return: The engine_id of this SnmpnotificationSchemaSnmpnotification.  # noqa: E501
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """Sets the engine_id of this SnmpnotificationSchemaSnmpnotification.

        Autogenerated Engine-id for Healthbot in Hex Format Eg: '80001f8880bd5b8d052eb40d6000000000'  # noqa: E501

        :param engine_id: The engine_id of this SnmpnotificationSchemaSnmpnotification.  # noqa: E501
        :type: str
        """
        if engine_id is not None and len(engine_id) > 64:
            raise ValueError("Invalid value for `engine_id`, length must be less than or equal to `64`")  # noqa: E501
        if engine_id is not None and len(engine_id) < 5:
            raise ValueError("Invalid value for `engine_id`, length must be greater than or equal to `5`")  # noqa: E501

        self._engine_id = engine_id

    @property
    def port(self):
        """Gets the port of this SnmpnotificationSchemaSnmpnotification.  # noqa: E501

        Port to listen for SNMP Notification(Traps/Informs) messages  # noqa: E501

        :return: The port of this SnmpnotificationSchemaSnmpnotification.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SnmpnotificationSchemaSnmpnotification.

        Port to listen for SNMP Notification(Traps/Informs) messages  # noqa: E501

        :param port: The port of this SnmpnotificationSchemaSnmpnotification.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def v3(self):
        """Gets the v3 of this SnmpnotificationSchemaSnmpnotification.  # noqa: E501


        :return: The v3 of this SnmpnotificationSchemaSnmpnotification.  # noqa: E501
        :rtype: SnmpnotificationSchemaSnmpnotificationV3
        """
        return self._v3

    @v3.setter
    def v3(self, v3):
        """Sets the v3 of this SnmpnotificationSchemaSnmpnotification.


        :param v3: The v3 of this SnmpnotificationSchemaSnmpnotification.  # noqa: E501
        :type: SnmpnotificationSchemaSnmpnotificationV3
        """

        self._v3 = v3

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
        if issubclass(SnmpnotificationSchemaSnmpnotification, dict):
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
        if not isinstance(other, SnmpnotificationSchemaSnmpnotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
