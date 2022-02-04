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


class ReportSchema(object):
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
        'capture_fields': 'list[str]',
        'destination': 'list[str]',
        'format': 'str',
        'graph_canvas': 'list[ReportSchemaGraphcanvas]',
        'name': 'str',
        'schedule': 'list[str]'
    }

    attribute_map = {
        'capture_fields': 'capture-fields',
        'destination': 'destination',
        'format': 'format',
        'graph_canvas': 'graph-canvas',
        'name': 'name',
        'schedule': 'schedule'
    }

    def __init__(self, capture_fields=None, destination=None, format=None, graph_canvas=None, name=None, schedule=None):  # noqa: E501
        """ReportSchema - a model defined in Swagger"""  # noqa: E501

        self._capture_fields = None
        self._destination = None
        self._format = None
        self._graph_canvas = None
        self._name = None
        self._schedule = None
        self.discriminator = None

        if capture_fields is not None:
            self.capture_fields = capture_fields
        self.destination = destination
        self.format = format
        if graph_canvas is not None:
            self.graph_canvas = graph_canvas
        self.name = name
        self.schedule = schedule

    @property
    def capture_fields(self):
        """Gets the capture_fields of this ReportSchema.  # noqa: E501


        :return: The capture_fields of this ReportSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._capture_fields

    @capture_fields.setter
    def capture_fields(self, capture_fields):
        """Sets the capture_fields of this ReportSchema.


        :param capture_fields: The capture_fields of this ReportSchema.  # noqa: E501
        :type: list[str]
        """

        self._capture_fields = capture_fields

    @property
    def destination(self):
        """Gets the destination of this ReportSchema.  # noqa: E501


        :return: The destination of this ReportSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ReportSchema.


        :param destination: The destination of this ReportSchema.  # noqa: E501
        :type: list[str]
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def format(self):
        """Gets the format of this ReportSchema.  # noqa: E501

        Generated report format  # noqa: E501

        :return: The format of this ReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ReportSchema.

        Generated report format  # noqa: E501

        :param format: The format of this ReportSchema.  # noqa: E501
        :type: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        allowed_values = ["json", "html", "pdf"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def graph_canvas(self):
        """Gets the graph_canvas of this ReportSchema.  # noqa: E501

        Canvas name  # noqa: E501

        :return: The graph_canvas of this ReportSchema.  # noqa: E501
        :rtype: list[ReportSchemaGraphcanvas]
        """
        return self._graph_canvas

    @graph_canvas.setter
    def graph_canvas(self, graph_canvas):
        """Sets the graph_canvas of this ReportSchema.

        Canvas name  # noqa: E501

        :param graph_canvas: The graph_canvas of this ReportSchema.  # noqa: E501
        :type: list[ReportSchemaGraphcanvas]
        """

        self._graph_canvas = graph_canvas

    @property
    def name(self):
        """Gets the name of this ReportSchema.  # noqa: E501

        Name of the report  # noqa: E501

        :return: The name of this ReportSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportSchema.

        Name of the report  # noqa: E501

        :param name: The name of this ReportSchema.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def schedule(self):
        """Gets the schedule of this ReportSchema.  # noqa: E501


        :return: The schedule of this ReportSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ReportSchema.


        :param schedule: The schedule of this ReportSchema.  # noqa: E501
        :type: list[str]
        """
        if schedule is None:
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501

        self._schedule = schedule

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
        if issubclass(ReportSchema, dict):
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
        if not isinstance(other, ReportSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
