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


class TsdbResultsResults(object):
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
        'statement_id': 'int',
        'database': 'str',
        'series': 'list[TsdbResultsSeries]'
    }

    attribute_map = {
        'statement_id': 'statement_id',
        'database': 'database',
        'series': 'series'
    }

    def __init__(self, statement_id=None, database=None, series=None):  # noqa: E501
        """TsdbResultsResults - a model defined in Swagger"""  # noqa: E501

        self._statement_id = None
        self._database = None
        self._series = None
        self.discriminator = None

        if statement_id is not None:
            self.statement_id = statement_id
        if database is not None:
            self.database = database
        if series is not None:
            self.series = series

    @property
    def statement_id(self):
        """Gets the statement_id of this TsdbResultsResults.  # noqa: E501


        :return: The statement_id of this TsdbResultsResults.  # noqa: E501
        :rtype: int
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        """Sets the statement_id of this TsdbResultsResults.


        :param statement_id: The statement_id of this TsdbResultsResults.  # noqa: E501
        :type: int
        """

        self._statement_id = statement_id

    @property
    def database(self):
        """Gets the database of this TsdbResultsResults.  # noqa: E501


        :return: The database of this TsdbResultsResults.  # noqa: E501
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this TsdbResultsResults.


        :param database: The database of this TsdbResultsResults.  # noqa: E501
        :type: str
        """

        self._database = database

    @property
    def series(self):
        """Gets the series of this TsdbResultsResults.  # noqa: E501


        :return: The series of this TsdbResultsResults.  # noqa: E501
        :rtype: list[TsdbResultsSeries]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this TsdbResultsResults.


        :param series: The series of this TsdbResultsResults.  # noqa: E501
        :type: list[TsdbResultsSeries]
        """

        self._series = series

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
        if issubclass(TsdbResultsResults, dict):
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
        if not isinstance(other, TsdbResultsResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
