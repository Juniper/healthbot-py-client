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


class IngestMappingSchema(object):
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
        'i_agent': 'IngestmappingSchemaIAgent',
        'name': 'str',
        'native_gpb': 'IngestmappingSchemaNativegpb',
        'netflow': 'IngestmappingSchemaNetflow',
        'open_config': 'IngestmappingSchemaOpenconfig',
        'snmp': 'IngestmappingSchemaSnmp',
        'syslog': 'IngestmappingSchemaSyslog'
    }

    attribute_map = {
        'i_agent': 'iAgent',
        'name': 'name',
        'native_gpb': 'native-gpb',
        'netflow': 'netflow',
        'open_config': 'open-config',
        'snmp': 'snmp',
        'syslog': 'syslog'
    }

    def __init__(self, i_agent=None, name=None, native_gpb=None, netflow=None, open_config=None, snmp=None, syslog=None):  # noqa: E501
        """IngestMappingSchema - a model defined in Swagger"""  # noqa: E501

        self._i_agent = None
        self._name = None
        self._native_gpb = None
        self._netflow = None
        self._open_config = None
        self._snmp = None
        self._syslog = None
        self.discriminator = None

        if i_agent is not None:
            self.i_agent = i_agent
        self.name = name
        if native_gpb is not None:
            self.native_gpb = native_gpb
        if netflow is not None:
            self.netflow = netflow
        if open_config is not None:
            self.open_config = open_config
        if snmp is not None:
            self.snmp = snmp
        if syslog is not None:
            self.syslog = syslog

    @property
    def i_agent(self):
        """Gets the i_agent of this IngestMappingSchema.  # noqa: E501


        :return: The i_agent of this IngestMappingSchema.  # noqa: E501
        :rtype: IngestmappingSchemaIAgent
        """
        return self._i_agent

    @i_agent.setter
    def i_agent(self, i_agent):
        """Sets the i_agent of this IngestMappingSchema.


        :param i_agent: The i_agent of this IngestMappingSchema.  # noqa: E501
        :type: IngestmappingSchemaIAgent
        """

        self._i_agent = i_agent

    @property
    def name(self):
        """Gets the name of this IngestMappingSchema.  # noqa: E501

        Name of the mapping  # noqa: E501

        :return: The name of this IngestMappingSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IngestMappingSchema.

        Name of the mapping  # noqa: E501

        :param name: The name of this IngestMappingSchema.  # noqa: E501
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
    def native_gpb(self):
        """Gets the native_gpb of this IngestMappingSchema.  # noqa: E501


        :return: The native_gpb of this IngestMappingSchema.  # noqa: E501
        :rtype: IngestmappingSchemaNativegpb
        """
        return self._native_gpb

    @native_gpb.setter
    def native_gpb(self, native_gpb):
        """Sets the native_gpb of this IngestMappingSchema.


        :param native_gpb: The native_gpb of this IngestMappingSchema.  # noqa: E501
        :type: IngestmappingSchemaNativegpb
        """

        self._native_gpb = native_gpb

    @property
    def netflow(self):
        """Gets the netflow of this IngestMappingSchema.  # noqa: E501


        :return: The netflow of this IngestMappingSchema.  # noqa: E501
        :rtype: IngestmappingSchemaNetflow
        """
        return self._netflow

    @netflow.setter
    def netflow(self, netflow):
        """Sets the netflow of this IngestMappingSchema.


        :param netflow: The netflow of this IngestMappingSchema.  # noqa: E501
        :type: IngestmappingSchemaNetflow
        """

        self._netflow = netflow

    @property
    def open_config(self):
        """Gets the open_config of this IngestMappingSchema.  # noqa: E501


        :return: The open_config of this IngestMappingSchema.  # noqa: E501
        :rtype: IngestmappingSchemaOpenconfig
        """
        return self._open_config

    @open_config.setter
    def open_config(self, open_config):
        """Sets the open_config of this IngestMappingSchema.


        :param open_config: The open_config of this IngestMappingSchema.  # noqa: E501
        :type: IngestmappingSchemaOpenconfig
        """

        self._open_config = open_config

    @property
    def snmp(self):
        """Gets the snmp of this IngestMappingSchema.  # noqa: E501


        :return: The snmp of this IngestMappingSchema.  # noqa: E501
        :rtype: IngestmappingSchemaSnmp
        """
        return self._snmp

    @snmp.setter
    def snmp(self, snmp):
        """Sets the snmp of this IngestMappingSchema.


        :param snmp: The snmp of this IngestMappingSchema.  # noqa: E501
        :type: IngestmappingSchemaSnmp
        """

        self._snmp = snmp

    @property
    def syslog(self):
        """Gets the syslog of this IngestMappingSchema.  # noqa: E501


        :return: The syslog of this IngestMappingSchema.  # noqa: E501
        :rtype: IngestmappingSchemaSyslog
        """
        return self._syslog

    @syslog.setter
    def syslog(self, syslog):
        """Sets the syslog of this IngestMappingSchema.


        :param syslog: The syslog of this IngestMappingSchema.  # noqa: E501
        :type: IngestmappingSchemaSyslog
        """

        self._syslog = syslog

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
        if issubclass(IngestMappingSchema, dict):
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
        if not isinstance(other, IngestMappingSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
