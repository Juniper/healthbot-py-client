# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse200(object):
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
        'job_id': 'str',
        'job_result': 'str',
        'job_status': 'str'
    }

    attribute_map = {
        'job_id': 'job-id',
        'job_result': 'job-result',
        'job_status': 'job-status'
    }

    def __init__(self, job_id=None, job_result=None, job_status=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._job_result = None
        self._job_status = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_result is not None:
            self.job_result = job_result
        if job_status is not None:
            self.job_status = job_status

    @property
    def job_id(self):
        """Gets the job_id of this InlineResponse200.  # noqa: E501


        :return: The job_id of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this InlineResponse200.


        :param job_id: The job_id of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def job_result(self):
        """Gets the job_result of this InlineResponse200.  # noqa: E501


        :return: The job_result of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        """Sets the job_result of this InlineResponse200.


        :param job_result: The job_result of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._job_result = job_result

    @property
    def job_status(self):
        """Gets the job_status of this InlineResponse200.  # noqa: E501


        :return: The job_status of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this InlineResponse200.


        :param job_status: The job_status of this InlineResponse200.  # noqa: E501
        :type: str
        """
        allowed_values = ["finished", "killed", "pending", "started"]  # noqa: E501
        if job_status not in allowed_values:
            raise ValueError(
                "Invalid value for `job_status` ({0}), must be one of {1}"  # noqa: E501
                .format(job_status, allowed_values)
            )

        self._job_status = job_status

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other