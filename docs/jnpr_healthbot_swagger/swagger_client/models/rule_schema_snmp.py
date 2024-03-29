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


class RuleSchemaSnmp(object):
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
        'frequency': 'str',
        'scalars': 'list[str]',
        'table': 'str'
    }

    attribute_map = {
        'frequency': 'frequency',
        'scalars': 'scalars',
        'table': 'table'
    }

    def __init__(self, frequency=None, scalars=None, table=None):  # noqa: E501
        """RuleSchemaSnmp - a model defined in Swagger"""  # noqa: E501

        self._frequency = None
        self._scalars = None
        self._table = None
        self.discriminator = None

        self.frequency = frequency
        if scalars is not None:
            self.scalars = scalars
        if table is not None:
            self.table = table

    @property
    def frequency(self):
        """Gets the frequency of this RuleSchemaSnmp.  # noqa: E501

        Frequency at which data needs to be extracted from given SNMP table. Specify positive integer followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s  # noqa: E501

        :return: The frequency of this RuleSchemaSnmp.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this RuleSchemaSnmp.

        Frequency at which data needs to be extracted from given SNMP table. Specify positive integer followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s  # noqa: E501

        :param frequency: The frequency of this RuleSchemaSnmp.  # noqa: E501
        :type: str
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501
        if frequency is not None and not re.search(r'^[1-9][0-9]*[smhdwy]$', frequency):  # noqa: E501
            raise ValueError(r"Invalid value for `frequency`, must be a follow pattern or equal to `/^[1-9][0-9]*[smhdwy]$/`")  # noqa: E501

        self._frequency = frequency

    @property
    def scalars(self):
        """Gets the scalars of this RuleSchemaSnmp.  # noqa: E501


        :return: The scalars of this RuleSchemaSnmp.  # noqa: E501
        :rtype: list[str]
        """
        return self._scalars

    @scalars.setter
    def scalars(self, scalars):
        """Sets the scalars of this RuleSchemaSnmp.


        :param scalars: The scalars of this RuleSchemaSnmp.  # noqa: E501
        :type: list[str]
        """

        self._scalars = scalars

    @property
    def table(self):
        """Gets the table of this RuleSchemaSnmp.  # noqa: E501

        OID of an SNMP table  # noqa: E501

        :return: The table of this RuleSchemaSnmp.  # noqa: E501
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this RuleSchemaSnmp.

        OID of an SNMP table  # noqa: E501

        :param table: The table of this RuleSchemaSnmp.  # noqa: E501
        :type: str
        """

        self._table = table

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
        if issubclass(RuleSchemaSnmp, dict):
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
        if not isinstance(other, RuleSchemaSnmp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
