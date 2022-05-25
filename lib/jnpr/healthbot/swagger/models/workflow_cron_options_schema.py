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


class WorkflowCronOptionsSchema(object):
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
        'description': 'str',
        'schedule': 'str',
        'concurrency_policy': 'str',
        'starting_deadline_duration': 'str',
        'successful_jobs_history_limit': 'int',
        'failed_jobs_history_limit': 'int'
    }

    attribute_map = {
        'description': 'description',
        'schedule': 'schedule',
        'concurrency_policy': 'concurrency-policy',
        'starting_deadline_duration': 'starting-deadline-duration',
        'successful_jobs_history_limit': 'successful-jobs-history-limit',
        'failed_jobs_history_limit': 'failed-jobs-history-limit'
    }

    def __init__(self, description=None, schedule=None, concurrency_policy=None, starting_deadline_duration=None, successful_jobs_history_limit=None, failed_jobs_history_limit=None):  # noqa: E501
        """WorkflowCronOptionsSchema - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._schedule = None
        self._concurrency_policy = None
        self._starting_deadline_duration = None
        self._successful_jobs_history_limit = None
        self._failed_jobs_history_limit = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.schedule = schedule
        if concurrency_policy is not None:
            self.concurrency_policy = concurrency_policy
        if starting_deadline_duration is not None:
            self.starting_deadline_duration = starting_deadline_duration
        if successful_jobs_history_limit is not None:
            self.successful_jobs_history_limit = successful_jobs_history_limit
        if failed_jobs_history_limit is not None:
            self.failed_jobs_history_limit = failed_jobs_history_limit

    @property
    def description(self):
        """Gets the description of this WorkflowCronOptionsSchema.  # noqa: E501

        Description about this cron workflow options  # noqa: E501

        :return: The description of this WorkflowCronOptionsSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowCronOptionsSchema.

        Description about this cron workflow options  # noqa: E501

        :param description: The description of this WorkflowCronOptionsSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def schedule(self):
        """Gets the schedule of this WorkflowCronOptionsSchema.  # noqa: E501

        Cron expression of time at which workflow will be run  # noqa: E501

        :return: The schedule of this WorkflowCronOptionsSchema.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this WorkflowCronOptionsSchema.

        Cron expression of time at which workflow will be run  # noqa: E501

        :param schedule: The schedule of this WorkflowCronOptionsSchema.  # noqa: E501
        :type: str
        """
        if schedule is None:
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501

        self._schedule = schedule

    @property
    def concurrency_policy(self):
        """Gets the concurrency_policy of this WorkflowCronOptionsSchema.  # noqa: E501

        Policy that determines what to do if multiple Workflows are scheduled at the same time  # noqa: E501

        :return: The concurrency_policy of this WorkflowCronOptionsSchema.  # noqa: E501
        :rtype: str
        """
        return self._concurrency_policy

    @concurrency_policy.setter
    def concurrency_policy(self, concurrency_policy):
        """Sets the concurrency_policy of this WorkflowCronOptionsSchema.

        Policy that determines what to do if multiple Workflows are scheduled at the same time  # noqa: E501

        :param concurrency_policy: The concurrency_policy of this WorkflowCronOptionsSchema.  # noqa: E501
        :type: str
        """
        allowed_values = ["allow", "replace", "forbid"]  # noqa: E501
        if concurrency_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `concurrency_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(concurrency_policy, allowed_values)
            )

        self._concurrency_policy = concurrency_policy

    @property
    def starting_deadline_duration(self):
        """Gets the starting_deadline_duration of this WorkflowCronOptionsSchema.  # noqa: E501

        Duration after the last successful run during which a missed Workflow will be run  # noqa: E501

        :return: The starting_deadline_duration of this WorkflowCronOptionsSchema.  # noqa: E501
        :rtype: str
        """
        return self._starting_deadline_duration

    @starting_deadline_duration.setter
    def starting_deadline_duration(self, starting_deadline_duration):
        """Sets the starting_deadline_duration of this WorkflowCronOptionsSchema.

        Duration after the last successful run during which a missed Workflow will be run  # noqa: E501

        :param starting_deadline_duration: The starting_deadline_duration of this WorkflowCronOptionsSchema.  # noqa: E501
        :type: str
        """

        self._starting_deadline_duration = starting_deadline_duration

    @property
    def successful_jobs_history_limit(self):
        """Gets the successful_jobs_history_limit of this WorkflowCronOptionsSchema.  # noqa: E501

        Number of successful Workflows that will be persisted at a time  # noqa: E501

        :return: The successful_jobs_history_limit of this WorkflowCronOptionsSchema.  # noqa: E501
        :rtype: int
        """
        return self._successful_jobs_history_limit

    @successful_jobs_history_limit.setter
    def successful_jobs_history_limit(self, successful_jobs_history_limit):
        """Sets the successful_jobs_history_limit of this WorkflowCronOptionsSchema.

        Number of successful Workflows that will be persisted at a time  # noqa: E501

        :param successful_jobs_history_limit: The successful_jobs_history_limit of this WorkflowCronOptionsSchema.  # noqa: E501
        :type: int
        """

        self._successful_jobs_history_limit = successful_jobs_history_limit

    @property
    def failed_jobs_history_limit(self):
        """Gets the failed_jobs_history_limit of this WorkflowCronOptionsSchema.  # noqa: E501

        Policy that determines what to do if multiple Workflows are scheduled at the same time  # noqa: E501

        :return: The failed_jobs_history_limit of this WorkflowCronOptionsSchema.  # noqa: E501
        :rtype: int
        """
        return self._failed_jobs_history_limit

    @failed_jobs_history_limit.setter
    def failed_jobs_history_limit(self, failed_jobs_history_limit):
        """Sets the failed_jobs_history_limit of this WorkflowCronOptionsSchema.

        Policy that determines what to do if multiple Workflows are scheduled at the same time  # noqa: E501

        :param failed_jobs_history_limit: The failed_jobs_history_limit of this WorkflowCronOptionsSchema.  # noqa: E501
        :type: int
        """

        self._failed_jobs_history_limit = failed_jobs_history_limit

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
        if issubclass(WorkflowCronOptionsSchema, dict):
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
        if not isinstance(other, WorkflowCronOptionsSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other