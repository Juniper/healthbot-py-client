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


class HbGraphs(object):
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
        'graph_name': 'str',
        'graph_description': 'str',
        'graph_type': 'str',
        'time_range': 'str',
        'query': 'HbGraphsQuery',
        'y_label': 'str',
        'y_max': 'str',
        'y_min': 'str',
        'unit_type': 'str',
        'decimals': 'str'
    }

    attribute_map = {
        'graph_name': 'graph_name',
        'graph_description': 'graph_description',
        'graph_type': 'graph_type',
        'time_range': 'time_range',
        'query': 'query',
        'y_label': 'y_label',
        'y_max': 'y_max',
        'y_min': 'y_min',
        'unit_type': 'unit_type',
        'decimals': 'decimals'
    }

    def __init__(self, graph_name=None, graph_description=None, graph_type=None, time_range=None, query=None, y_label=None, y_max=None, y_min=None, unit_type=None, decimals=None):  # noqa: E501
        """HbGraphs - a model defined in Swagger"""  # noqa: E501

        self._graph_name = None
        self._graph_description = None
        self._graph_type = None
        self._time_range = None
        self._query = None
        self._y_label = None
        self._y_max = None
        self._y_min = None
        self._unit_type = None
        self._decimals = None
        self.discriminator = None

        if graph_name is not None:
            self.graph_name = graph_name
        if graph_description is not None:
            self.graph_description = graph_description
        if graph_type is not None:
            self.graph_type = graph_type
        if time_range is not None:
            self.time_range = time_range
        if query is not None:
            self.query = query
        if y_label is not None:
            self.y_label = y_label
        if y_max is not None:
            self.y_max = y_max
        if y_min is not None:
            self.y_min = y_min
        if unit_type is not None:
            self.unit_type = unit_type
        if decimals is not None:
            self.decimals = decimals

    @property
    def graph_name(self):
        """Gets the graph_name of this HbGraphs.  # noqa: E501

        Graph name  # noqa: E501

        :return: The graph_name of this HbGraphs.  # noqa: E501
        :rtype: str
        """
        return self._graph_name

    @graph_name.setter
    def graph_name(self, graph_name):
        """Sets the graph_name of this HbGraphs.

        Graph name  # noqa: E501

        :param graph_name: The graph_name of this HbGraphs.  # noqa: E501
        :type: str
        """

        self._graph_name = graph_name

    @property
    def graph_description(self):
        """Gets the graph_description of this HbGraphs.  # noqa: E501

        Graph description  # noqa: E501

        :return: The graph_description of this HbGraphs.  # noqa: E501
        :rtype: str
        """
        return self._graph_description

    @graph_description.setter
    def graph_description(self, graph_description):
        """Sets the graph_description of this HbGraphs.

        Graph description  # noqa: E501

        :param graph_description: The graph_description of this HbGraphs.  # noqa: E501
        :type: str
        """

        self._graph_description = graph_description

    @property
    def graph_type(self):
        """Gets the graph_type of this HbGraphs.  # noqa: E501

        Graph type: Time Series or Histogram or Heatmap  # noqa: E501

        :return: The graph_type of this HbGraphs.  # noqa: E501
        :rtype: str
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type):
        """Sets the graph_type of this HbGraphs.

        Graph type: Time Series or Histogram or Heatmap  # noqa: E501

        :param graph_type: The graph_type of this HbGraphs.  # noqa: E501
        :type: str
        """
        allowed_values = ["Time Series", "Histogram", "Heatmap"]  # noqa: E501
        if graph_type not in allowed_values:
            raise ValueError(
                "Invalid value for `graph_type` ({0}), must be one of {1}"  # noqa: E501
                .format(graph_type, allowed_values)
            )

        self._graph_type = graph_type

    @property
    def time_range(self):
        """Gets the time_range of this HbGraphs.  # noqa: E501

        Time range for the graph  # noqa: E501

        :return: The time_range of this HbGraphs.  # noqa: E501
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this HbGraphs.

        Time range for the graph  # noqa: E501

        :param time_range: The time_range of this HbGraphs.  # noqa: E501
        :type: str
        """
        allowed_values = ["1h", "3h", "6h", "12h", "1d", "2d", "3d", "4d", "5d", "6d", "7d"]  # noqa: E501
        if time_range not in allowed_values:
            raise ValueError(
                "Invalid value for `time_range` ({0}), must be one of {1}"  # noqa: E501
                .format(time_range, allowed_values)
            )

        self._time_range = time_range

    @property
    def query(self):
        """Gets the query of this HbGraphs.  # noqa: E501


        :return: The query of this HbGraphs.  # noqa: E501
        :rtype: HbGraphsQuery
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this HbGraphs.


        :param query: The query of this HbGraphs.  # noqa: E501
        :type: HbGraphsQuery
        """

        self._query = query

    @property
    def y_label(self):
        """Gets the y_label of this HbGraphs.  # noqa: E501

        Y Label value in visualization  # noqa: E501

        :return: The y_label of this HbGraphs.  # noqa: E501
        :rtype: str
        """
        return self._y_label

    @y_label.setter
    def y_label(self, y_label):
        """Sets the y_label of this HbGraphs.

        Y Label value in visualization  # noqa: E501

        :param y_label: The y_label of this HbGraphs.  # noqa: E501
        :type: str
        """

        self._y_label = y_label

    @property
    def y_max(self):
        """Gets the y_max of this HbGraphs.  # noqa: E501

        Y max value in visualization  # noqa: E501

        :return: The y_max of this HbGraphs.  # noqa: E501
        :rtype: str
        """
        return self._y_max

    @y_max.setter
    def y_max(self, y_max):
        """Sets the y_max of this HbGraphs.

        Y max value in visualization  # noqa: E501

        :param y_max: The y_max of this HbGraphs.  # noqa: E501
        :type: str
        """

        self._y_max = y_max

    @property
    def y_min(self):
        """Gets the y_min of this HbGraphs.  # noqa: E501

        Y min value in visualization  # noqa: E501

        :return: The y_min of this HbGraphs.  # noqa: E501
        :rtype: str
        """
        return self._y_min

    @y_min.setter
    def y_min(self, y_min):
        """Sets the y_min of this HbGraphs.

        Y min value in visualization  # noqa: E501

        :param y_min: The y_min of this HbGraphs.  # noqa: E501
        :type: str
        """

        self._y_min = y_min

    @property
    def unit_type(self):
        """Gets the unit_type of this HbGraphs.  # noqa: E501

        unit type value in visualization  # noqa: E501

        :return: The unit_type of this HbGraphs.  # noqa: E501
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """Sets the unit_type of this HbGraphs.

        unit type value in visualization  # noqa: E501

        :param unit_type: The unit_type of this HbGraphs.  # noqa: E501
        :type: str
        """
        allowed_values = ["Short", "Percentage(0-100)", "Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Parts per million(ppm)", "Parts per billion(ppb)"]  # noqa: E501
        if unit_type not in allowed_values:
            raise ValueError(
                "Invalid value for `unit_type` ({0}), must be one of {1}"  # noqa: E501
                .format(unit_type, allowed_values)
            )

        self._unit_type = unit_type

    @property
    def decimals(self):
        """Gets the decimals of this HbGraphs.  # noqa: E501

        Decimals value in visualization  # noqa: E501

        :return: The decimals of this HbGraphs.  # noqa: E501
        :rtype: str
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """Sets the decimals of this HbGraphs.

        Decimals value in visualization  # noqa: E501

        :param decimals: The decimals of this HbGraphs.  # noqa: E501
        :type: str
        """

        self._decimals = decimals

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
        if issubclass(HbGraphs, dict):
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
        if not isinstance(other, HbGraphs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
