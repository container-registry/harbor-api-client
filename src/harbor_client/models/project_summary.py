# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from harbor_client.configuration import Configuration


class ProjectSummary(object):
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
        "repo_count": "int",
        "chart_count": "int",
        "project_admin_count": "int",
        "maintainer_count": "int",
        "developer_count": "int",
        "guest_count": "int",
        "limited_guest_count": "int",
        "quota": "ProjectSummaryQuota",
        "registry": "Registry",
    }

    attribute_map = {
        "repo_count": "repo_count",
        "chart_count": "chart_count",
        "project_admin_count": "project_admin_count",
        "maintainer_count": "maintainer_count",
        "developer_count": "developer_count",
        "guest_count": "guest_count",
        "limited_guest_count": "limited_guest_count",
        "quota": "quota",
        "registry": "registry",
    }

    def __init__(
        self,
        repo_count=None,
        chart_count=None,
        project_admin_count=None,
        maintainer_count=None,
        developer_count=None,
        guest_count=None,
        limited_guest_count=None,
        quota=None,
        registry=None,
        _configuration=None,
    ):  # noqa: E501
        """ProjectSummary - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._repo_count = None
        self._chart_count = None
        self._project_admin_count = None
        self._maintainer_count = None
        self._developer_count = None
        self._guest_count = None
        self._limited_guest_count = None
        self._quota = None
        self._registry = None
        self.discriminator = None

        if repo_count is not None:
            self.repo_count = repo_count
        if chart_count is not None:
            self.chart_count = chart_count
        if project_admin_count is not None:
            self.project_admin_count = project_admin_count
        if maintainer_count is not None:
            self.maintainer_count = maintainer_count
        if developer_count is not None:
            self.developer_count = developer_count
        if guest_count is not None:
            self.guest_count = guest_count
        if limited_guest_count is not None:
            self.limited_guest_count = limited_guest_count
        if quota is not None:
            self.quota = quota
        if registry is not None:
            self.registry = registry

    @property
    def repo_count(self):
        """Gets the repo_count of this ProjectSummary.  # noqa: E501

        The number of the repositories under this project.  # noqa: E501

        :return: The repo_count of this ProjectSummary.  # noqa: E501
        :rtype: int
        """
        return self._repo_count

    @repo_count.setter
    def repo_count(self, repo_count):
        """Sets the repo_count of this ProjectSummary.

        The number of the repositories under this project.  # noqa: E501

        :param repo_count: The repo_count of this ProjectSummary.  # noqa: E501
        :type: int
        """

        self._repo_count = repo_count

    @property
    def chart_count(self):
        """Gets the chart_count of this ProjectSummary.  # noqa: E501

        The total number of charts under this project.  # noqa: E501

        :return: The chart_count of this ProjectSummary.  # noqa: E501
        :rtype: int
        """
        return self._chart_count

    @chart_count.setter
    def chart_count(self, chart_count):
        """Sets the chart_count of this ProjectSummary.

        The total number of charts under this project.  # noqa: E501

        :param chart_count: The chart_count of this ProjectSummary.  # noqa: E501
        :type: int
        """

        self._chart_count = chart_count

    @property
    def project_admin_count(self):
        """Gets the project_admin_count of this ProjectSummary.  # noqa: E501

        The total number of project admin members.  # noqa: E501

        :return: The project_admin_count of this ProjectSummary.  # noqa: E501
        :rtype: int
        """
        return self._project_admin_count

    @project_admin_count.setter
    def project_admin_count(self, project_admin_count):
        """Sets the project_admin_count of this ProjectSummary.

        The total number of project admin members.  # noqa: E501

        :param project_admin_count: The project_admin_count of this ProjectSummary.  # noqa: E501
        :type: int
        """

        self._project_admin_count = project_admin_count

    @property
    def maintainer_count(self):
        """Gets the maintainer_count of this ProjectSummary.  # noqa: E501

        The total number of maintainer members.  # noqa: E501

        :return: The maintainer_count of this ProjectSummary.  # noqa: E501
        :rtype: int
        """
        return self._maintainer_count

    @maintainer_count.setter
    def maintainer_count(self, maintainer_count):
        """Sets the maintainer_count of this ProjectSummary.

        The total number of maintainer members.  # noqa: E501

        :param maintainer_count: The maintainer_count of this ProjectSummary.  # noqa: E501
        :type: int
        """

        self._maintainer_count = maintainer_count

    @property
    def developer_count(self):
        """Gets the developer_count of this ProjectSummary.  # noqa: E501

        The total number of developer members.  # noqa: E501

        :return: The developer_count of this ProjectSummary.  # noqa: E501
        :rtype: int
        """
        return self._developer_count

    @developer_count.setter
    def developer_count(self, developer_count):
        """Sets the developer_count of this ProjectSummary.

        The total number of developer members.  # noqa: E501

        :param developer_count: The developer_count of this ProjectSummary.  # noqa: E501
        :type: int
        """

        self._developer_count = developer_count

    @property
    def guest_count(self):
        """Gets the guest_count of this ProjectSummary.  # noqa: E501

        The total number of guest members.  # noqa: E501

        :return: The guest_count of this ProjectSummary.  # noqa: E501
        :rtype: int
        """
        return self._guest_count

    @guest_count.setter
    def guest_count(self, guest_count):
        """Sets the guest_count of this ProjectSummary.

        The total number of guest members.  # noqa: E501

        :param guest_count: The guest_count of this ProjectSummary.  # noqa: E501
        :type: int
        """

        self._guest_count = guest_count

    @property
    def limited_guest_count(self):
        """Gets the limited_guest_count of this ProjectSummary.  # noqa: E501

        The total number of limited guest members.  # noqa: E501

        :return: The limited_guest_count of this ProjectSummary.  # noqa: E501
        :rtype: int
        """
        return self._limited_guest_count

    @limited_guest_count.setter
    def limited_guest_count(self, limited_guest_count):
        """Sets the limited_guest_count of this ProjectSummary.

        The total number of limited guest members.  # noqa: E501

        :param limited_guest_count: The limited_guest_count of this ProjectSummary.  # noqa: E501
        :type: int
        """

        self._limited_guest_count = limited_guest_count

    @property
    def quota(self):
        """Gets the quota of this ProjectSummary.  # noqa: E501


        :return: The quota of this ProjectSummary.  # noqa: E501
        :rtype: ProjectSummaryQuota
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ProjectSummary.


        :param quota: The quota of this ProjectSummary.  # noqa: E501
        :type: ProjectSummaryQuota
        """

        self._quota = quota

    @property
    def registry(self):
        """Gets the registry of this ProjectSummary.  # noqa: E501


        :return: The registry of this ProjectSummary.  # noqa: E501
        :rtype: Registry
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this ProjectSummary.


        :param registry: The registry of this ProjectSummary.  # noqa: E501
        :type: Registry
        """

        self._registry = registry

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(ProjectSummary, dict):
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
        if not isinstance(other, ProjectSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectSummary):
            return True

        return self.to_dict() != other.to_dict()
