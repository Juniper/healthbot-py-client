# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RuleSchemaFormulaOutlierdetection(object):
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
        'algorithm': 'RuleSchemaFormulaOutlierdetectionAlgorithm',
        'dataset': 'str'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'dataset': 'dataset'
    }

    def __init__(self, algorithm=None, dataset=None):  # noqa: E501
        """RuleSchemaFormulaOutlierdetection - a model defined in Swagger"""  # noqa: E501

        self._algorithm = None
        self._dataset = None
        self.discriminator = None

        if algorithm is not None:
            self.algorithm = algorithm
        self.dataset = dataset

    @property
    def algorithm(self):
        """Gets the algorithm of this RuleSchemaFormulaOutlierdetection.  # noqa: E501


        :return: The algorithm of this RuleSchemaFormulaOutlierdetection.  # noqa: E501
        :rtype: RuleSchemaFormulaOutlierdetectionAlgorithm
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this RuleSchemaFormulaOutlierdetection.


        :param algorithm: The algorithm of this RuleSchemaFormulaOutlierdetection.  # noqa: E501
        :type: RuleSchemaFormulaOutlierdetectionAlgorithm
        """

        self._algorithm = algorithm

    @property
    def dataset(self):
        """Gets the dataset of this RuleSchemaFormulaOutlierdetection.  # noqa: E501

        Variable containing the list of XPATHs to the data  # noqa: E501

        :return: The dataset of this RuleSchemaFormulaOutlierdetection.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this RuleSchemaFormulaOutlierdetection.

        Variable containing the list of XPATHs to the data  # noqa: E501

        :param dataset: The dataset of this RuleSchemaFormulaOutlierdetection.  # noqa: E501
        :type: str
        """
        if dataset is None:
            raise ValueError("Invalid value for `dataset`, must not be `None`")  # noqa: E501

        self._dataset = dataset

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
        if issubclass(RuleSchemaFormulaOutlierdetection, dict):
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
        if not isinstance(other, RuleSchemaFormulaOutlierdetection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
