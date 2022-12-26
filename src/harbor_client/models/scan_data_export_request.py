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


class ScanDataExportRequest(object):
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
        'job_name': 'str',
        'projects': 'list[int]',
        'labels': 'list[int]',
        'repositories': 'str',
        'cve_ids': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'job_name': 'job_name',
        'projects': 'projects',
        'labels': 'labels',
        'repositories': 'repositories',
        'cve_ids': 'cveIds',
        'tags': 'tags'
    }

    def __init__(self, job_name=None, projects=None, labels=None, repositories=None, cve_ids=None, tags=None, _configuration=None):  # noqa: E501
        """ScanDataExportRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._job_name = None
        self._projects = None
        self._labels = None
        self._repositories = None
        self._cve_ids = None
        self._tags = None
        self.discriminator = None

        if job_name is not None:
            self.job_name = job_name
        if projects is not None:
            self.projects = projects
        if labels is not None:
            self.labels = labels
        if repositories is not None:
            self.repositories = repositories
        if cve_ids is not None:
            self.cve_ids = cve_ids
        if tags is not None:
            self.tags = tags

    @property
    def job_name(self):
        """Gets the job_name of this ScanDataExportRequest.  # noqa: E501

        Name of the scan data export job  # noqa: E501

        :return: The job_name of this ScanDataExportRequest.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ScanDataExportRequest.

        Name of the scan data export job  # noqa: E501

        :param job_name: The job_name of this ScanDataExportRequest.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def projects(self):
        """Gets the projects of this ScanDataExportRequest.  # noqa: E501

        A list of one or more projects for which to export the scan data, currently only one project is supported due to performance concerns, but define as array for extension in the future.  # noqa: E501

        :return: The projects of this ScanDataExportRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this ScanDataExportRequest.

        A list of one or more projects for which to export the scan data, currently only one project is supported due to performance concerns, but define as array for extension in the future.  # noqa: E501

        :param projects: The projects of this ScanDataExportRequest.  # noqa: E501
        :type: list[int]
        """

        self._projects = projects

    @property
    def labels(self):
        """Gets the labels of this ScanDataExportRequest.  # noqa: E501

        A list of one or more labels for which to export the scan data, defaults to all if empty  # noqa: E501

        :return: The labels of this ScanDataExportRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ScanDataExportRequest.

        A list of one or more labels for which to export the scan data, defaults to all if empty  # noqa: E501

        :param labels: The labels of this ScanDataExportRequest.  # noqa: E501
        :type: list[int]
        """

        self._labels = labels

    @property
    def repositories(self):
        """Gets the repositories of this ScanDataExportRequest.  # noqa: E501

        A list of repositories for which to export the scan data, defaults to all if empty  # noqa: E501

        :return: The repositories of this ScanDataExportRequest.  # noqa: E501
        :rtype: str
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        """Sets the repositories of this ScanDataExportRequest.

        A list of repositories for which to export the scan data, defaults to all if empty  # noqa: E501

        :param repositories: The repositories of this ScanDataExportRequest.  # noqa: E501
        :type: str
        """

        self._repositories = repositories

    @property
    def cve_ids(self):
        """Gets the cve_ids of this ScanDataExportRequest.  # noqa: E501

        CVE-IDs for which to export data. Multiple CVE-IDs can be specified by separating using ',' and enclosed between '{}'. Defaults to all if empty  # noqa: E501

        :return: The cve_ids of this ScanDataExportRequest.  # noqa: E501
        :rtype: str
        """
        return self._cve_ids

    @cve_ids.setter
    def cve_ids(self, cve_ids):
        """Sets the cve_ids of this ScanDataExportRequest.

        CVE-IDs for which to export data. Multiple CVE-IDs can be specified by separating using ',' and enclosed between '{}'. Defaults to all if empty  # noqa: E501

        :param cve_ids: The cve_ids of this ScanDataExportRequest.  # noqa: E501
        :type: str
        """

        self._cve_ids = cve_ids

    @property
    def tags(self):
        """Gets the tags of this ScanDataExportRequest.  # noqa: E501

        A list of tags enclosed within '{}'. Defaults to all if empty  # noqa: E501

        :return: The tags of this ScanDataExportRequest.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ScanDataExportRequest.

        A list of tags enclosed within '{}'. Defaults to all if empty  # noqa: E501

        :param tags: The tags of this ScanDataExportRequest.  # noqa: E501
        :type: str
        """

        self._tags = tags

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
        if issubclass(ScanDataExportRequest, dict):
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
        if not isinstance(other, ScanDataExportRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScanDataExportRequest):
            return True

        return self.to_dict() != other.to_dict()