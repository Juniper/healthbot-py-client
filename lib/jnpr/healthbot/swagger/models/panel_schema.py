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


class PanelSchema(object):
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
        'db': 'str',
        'decimals': 'str',
        'panel_data': 'list[PanelDataSchema]',
        'panel_name': 'str',
        'panel_query': 'PanelSchemaPanelQuery',
        'panel_type': 'PanelSchemaPanelType',
        'panel_uid': 'str',
        'time_range': 'PanelSchemaTimeRange',
        'unit_type': 'PanelSchemaUnitType',
        'y_label': 'str',
        'y_max': 'str',
        'y_min': 'str'
    }

    attribute_map = {
        'db': 'db',
        'decimals': 'decimals',
        'panel_data': 'panelData',
        'panel_name': 'panelName',
        'panel_query': 'panelQuery',
        'panel_type': 'panelType',
        'panel_uid': 'panelUid',
        'time_range': 'timeRange',
        'unit_type': 'unitType',
        'y_label': 'yLabel',
        'y_max': 'yMax',
        'y_min': 'yMin'
    }

    def __init__(self, db=None, decimals=None, panel_data=None, panel_name=None, panel_query=None, panel_type=None, panel_uid=None, time_range=None, unit_type=None, y_label=None, y_max=None, y_min=None):  # noqa: E501
        """PanelSchema - a model defined in Swagger"""  # noqa: E501

        self._db = None
        self._decimals = None
        self._panel_data = None
        self._panel_name = None
        self._panel_query = None
        self._panel_type = None
        self._panel_uid = None
        self._time_range = None
        self._unit_type = None
        self._y_label = None
        self._y_max = None
        self._y_min = None
        self.discriminator = None

        if db is not None:
            self.db = db
        if decimals is not None:
            self.decimals = decimals
        if panel_data is not None:
            self.panel_data = panel_data
        if panel_name is not None:
            self.panel_name = panel_name
        if panel_query is not None:
            self.panel_query = panel_query
        if panel_type is not None:
            self.panel_type = panel_type
        if panel_uid is not None:
            self.panel_uid = panel_uid
        if time_range is not None:
            self.time_range = time_range
        if unit_type is not None:
            self.unit_type = unit_type
        if y_label is not None:
            self.y_label = y_label
        if y_max is not None:
            self.y_max = y_max
        if y_min is not None:
            self.y_min = y_min

    @property
    def db(self):
        """Gets the db of this PanelSchema.  # noqa: E501

        database name  # noqa: E501

        :return: The db of this PanelSchema.  # noqa: E501
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        """Sets the db of this PanelSchema.

        database name  # noqa: E501

        :param db: The db of this PanelSchema.  # noqa: E501
        :type: str
        """

        self._db = db

    @property
    def decimals(self):
        """Gets the decimals of this PanelSchema.  # noqa: E501

        decimal value  # noqa: E501

        :return: The decimals of this PanelSchema.  # noqa: E501
        :rtype: str
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """Sets the decimals of this PanelSchema.

        decimal value  # noqa: E501

        :param decimals: The decimals of this PanelSchema.  # noqa: E501
        :type: str
        """

        self._decimals = decimals

    @property
    def panel_data(self):
        """Gets the panel_data of this PanelSchema.  # noqa: E501

        Panel data  # noqa: E501

        :return: The panel_data of this PanelSchema.  # noqa: E501
        :rtype: list[PanelDataSchema]
        """
        return self._panel_data

    @panel_data.setter
    def panel_data(self, panel_data):
        """Sets the panel_data of this PanelSchema.

        Panel data  # noqa: E501

        :param panel_data: The panel_data of this PanelSchema.  # noqa: E501
        :type: list[PanelDataSchema]
        """

        self._panel_data = panel_data

    @property
    def panel_name(self):
        """Gets the panel_name of this PanelSchema.  # noqa: E501

        Name of the panel  # noqa: E501

        :return: The panel_name of this PanelSchema.  # noqa: E501
        :rtype: str
        """
        return self._panel_name

    @panel_name.setter
    def panel_name(self, panel_name):
        """Sets the panel_name of this PanelSchema.

        Name of the panel  # noqa: E501

        :param panel_name: The panel_name of this PanelSchema.  # noqa: E501
        :type: str
        """

        self._panel_name = panel_name

    @property
    def panel_query(self):
        """Gets the panel_query of this PanelSchema.  # noqa: E501


        :return: The panel_query of this PanelSchema.  # noqa: E501
        :rtype: PanelSchemaPanelQuery
        """
        return self._panel_query

    @panel_query.setter
    def panel_query(self, panel_query):
        """Sets the panel_query of this PanelSchema.


        :param panel_query: The panel_query of this PanelSchema.  # noqa: E501
        :type: PanelSchemaPanelQuery
        """

        self._panel_query = panel_query

    @property
    def panel_type(self):
        """Gets the panel_type of this PanelSchema.  # noqa: E501


        :return: The panel_type of this PanelSchema.  # noqa: E501
        :rtype: PanelSchemaPanelType
        """
        return self._panel_type

    @panel_type.setter
    def panel_type(self, panel_type):
        """Sets the panel_type of this PanelSchema.


        :param panel_type: The panel_type of this PanelSchema.  # noqa: E501
        :type: PanelSchemaPanelType
        """

        self._panel_type = panel_type

    @property
    def panel_uid(self):
        """Gets the panel_uid of this PanelSchema.  # noqa: E501

        Unique identifier for panel  # noqa: E501

        :return: The panel_uid of this PanelSchema.  # noqa: E501
        :rtype: str
        """
        return self._panel_uid

    @panel_uid.setter
    def panel_uid(self, panel_uid):
        """Sets the panel_uid of this PanelSchema.

        Unique identifier for panel  # noqa: E501

        :param panel_uid: The panel_uid of this PanelSchema.  # noqa: E501
        :type: str
        """

        self._panel_uid = panel_uid

    @property
    def time_range(self):
        """Gets the time_range of this PanelSchema.  # noqa: E501


        :return: The time_range of this PanelSchema.  # noqa: E501
        :rtype: PanelSchemaTimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this PanelSchema.


        :param time_range: The time_range of this PanelSchema.  # noqa: E501
        :type: PanelSchemaTimeRange
        """

        self._time_range = time_range

    @property
    def unit_type(self):
        """Gets the unit_type of this PanelSchema.  # noqa: E501


        :return: The unit_type of this PanelSchema.  # noqa: E501
        :rtype: PanelSchemaUnitType
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """Sets the unit_type of this PanelSchema.


        :param unit_type: The unit_type of this PanelSchema.  # noqa: E501
        :type: PanelSchemaUnitType
        """

        self._unit_type = unit_type

    @property
    def y_label(self):
        """Gets the y_label of this PanelSchema.  # noqa: E501

        yLabel values  # noqa: E501

        :return: The y_label of this PanelSchema.  # noqa: E501
        :rtype: str
        """
        return self._y_label

    @y_label.setter
    def y_label(self, y_label):
        """Sets the y_label of this PanelSchema.

        yLabel values  # noqa: E501

        :param y_label: The y_label of this PanelSchema.  # noqa: E501
        :type: str
        """

        self._y_label = y_label

    @property
    def y_max(self):
        """Gets the y_max of this PanelSchema.  # noqa: E501

        yMax value  # noqa: E501

        :return: The y_max of this PanelSchema.  # noqa: E501
        :rtype: str
        """
        return self._y_max

    @y_max.setter
    def y_max(self, y_max):
        """Sets the y_max of this PanelSchema.

        yMax value  # noqa: E501

        :param y_max: The y_max of this PanelSchema.  # noqa: E501
        :type: str
        """

        self._y_max = y_max

    @property
    def y_min(self):
        """Gets the y_min of this PanelSchema.  # noqa: E501

        yMin value  # noqa: E501

        :return: The y_min of this PanelSchema.  # noqa: E501
        :rtype: str
        """
        return self._y_min

    @y_min.setter
    def y_min(self, y_min):
        """Sets the y_min of this PanelSchema.

        yMin value  # noqa: E501

        :param y_min: The y_min of this PanelSchema.  # noqa: E501
        :type: str
        """

        self._y_min = y_min

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
        if issubclass(PanelSchema, dict):
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
        if not isinstance(other, PanelSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
