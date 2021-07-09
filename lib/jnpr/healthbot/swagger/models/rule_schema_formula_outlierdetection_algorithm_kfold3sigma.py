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


class RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma(object):
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
        'learning_period': 'str',
        'sensitivity': 'RuleSchemaFormulaOutlierdetectionAlgorithmDbscanSensitivity',
        'sigma_coefficient': 'float'
    }

    attribute_map = {
        'learning_period': 'learning-period',
        'sensitivity': 'sensitivity',
        'sigma_coefficient': 'sigma-coefficient'
    }

    def __init__(self, learning_period=None, sensitivity=None, sigma_coefficient=None):  # noqa: E501
        """RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma - a model defined in Swagger"""  # noqa: E501

        self._learning_period = None
        self._sensitivity = None
        self._sigma_coefficient = None
        self.discriminator = None

        self.learning_period = learning_period
        if sensitivity is not None:
            self.sensitivity = sensitivity
        if sigma_coefficient is not None:
            self.sigma_coefficient = sigma_coefficient

    @property
    def learning_period(self):
        """Gets the learning_period of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.  # noqa: E501

        Time period on which to detect outliers  # noqa: E501

        :return: The learning_period of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.  # noqa: E501
        :rtype: str
        """
        return self._learning_period

    @learning_period.setter
    def learning_period(self, learning_period):
        """Sets the learning_period of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.

        Time period on which to detect outliers  # noqa: E501

        :param learning_period: The learning_period of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.  # noqa: E501
        :type: str
        """
        if learning_period is None:
            raise ValueError("Invalid value for `learning_period`, must not be `None`")  # noqa: E501
        if learning_period is not None and not re.search(r'^[1-9][0-9]*(\\.[0-9]+)?(o|s|m|h|d|w|y|offset)$', learning_period):  # noqa: E501
            raise ValueError(r"Invalid value for `learning_period`, must be a follow pattern or equal to `/^[1-9][0-9]*(\\.[0-9]+)?(o|s|m|h|d|w|y|offset)$/`")  # noqa: E501

        self._learning_period = learning_period

    @property
    def sensitivity(self):
        """Gets the sensitivity of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.  # noqa: E501


        :return: The sensitivity of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.  # noqa: E501
        :rtype: RuleSchemaFormulaOutlierdetectionAlgorithmDbscanSensitivity
        """
        return self._sensitivity

    @sensitivity.setter
    def sensitivity(self, sensitivity):
        """Sets the sensitivity of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.


        :param sensitivity: The sensitivity of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.  # noqa: E501
        :type: RuleSchemaFormulaOutlierdetectionAlgorithmDbscanSensitivity
        """

        self._sensitivity = sensitivity

    @property
    def sigma_coefficient(self):
        """Gets the sigma_coefficient of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.  # noqa: E501

        Number of standard deviations past which outliers are marked  # noqa: E501

        :return: The sigma_coefficient of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.  # noqa: E501
        :rtype: float
        """
        return self._sigma_coefficient

    @sigma_coefficient.setter
    def sigma_coefficient(self, sigma_coefficient):
        """Sets the sigma_coefficient of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.

        Number of standard deviations past which outliers are marked  # noqa: E501

        :param sigma_coefficient: The sigma_coefficient of this RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma.  # noqa: E501
        :type: float
        """

        self._sigma_coefficient = sigma_coefficient

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
        if issubclass(RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma, dict):
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
        if not isinstance(other, RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
