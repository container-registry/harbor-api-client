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


class ReplicationTask(object):
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
        'id': 'int',
        'execution_id': 'int',
        'status': 'str',
        'job_id': 'str',
        'operation': 'str',
        'resource_type': 'str',
        'src_resource': 'str',
        'dst_resource': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'execution_id': 'execution_id',
        'status': 'status',
        'job_id': 'job_id',
        'operation': 'operation',
        'resource_type': 'resource_type',
        'src_resource': 'src_resource',
        'dst_resource': 'dst_resource',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, execution_id=None, status=None, job_id=None, operation=None, resource_type=None, src_resource=None, dst_resource=None, start_time=None, end_time=None, _configuration=None):  # noqa: E501
        """ReplicationTask - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._execution_id = None
        self._status = None
        self._job_id = None
        self._operation = None
        self._resource_type = None
        self._src_resource = None
        self._dst_resource = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if execution_id is not None:
            self.execution_id = execution_id
        if status is not None:
            self.status = status
        if job_id is not None:
            self.job_id = job_id
        if operation is not None:
            self.operation = operation
        if resource_type is not None:
            self.resource_type = resource_type
        if src_resource is not None:
            self.src_resource = src_resource
        if dst_resource is not None:
            self.dst_resource = dst_resource
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        """Gets the id of this ReplicationTask.  # noqa: E501

        The ID of the task  # noqa: E501

        :return: The id of this ReplicationTask.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReplicationTask.

        The ID of the task  # noqa: E501

        :param id: The id of this ReplicationTask.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def execution_id(self):
        """Gets the execution_id of this ReplicationTask.  # noqa: E501

        The ID of the execution that the task belongs to  # noqa: E501

        :return: The execution_id of this ReplicationTask.  # noqa: E501
        :rtype: int
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this ReplicationTask.

        The ID of the execution that the task belongs to  # noqa: E501

        :param execution_id: The execution_id of this ReplicationTask.  # noqa: E501
        :type: int
        """

        self._execution_id = execution_id

    @property
    def status(self):
        """Gets the status of this ReplicationTask.  # noqa: E501

        The status of the task  # noqa: E501

        :return: The status of this ReplicationTask.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReplicationTask.

        The status of the task  # noqa: E501

        :param status: The status of this ReplicationTask.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def job_id(self):
        """Gets the job_id of this ReplicationTask.  # noqa: E501

        The ID of the underlying job that the task related to  # noqa: E501

        :return: The job_id of this ReplicationTask.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ReplicationTask.

        The ID of the underlying job that the task related to  # noqa: E501

        :param job_id: The job_id of this ReplicationTask.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def operation(self):
        """Gets the operation of this ReplicationTask.  # noqa: E501

        The operation of the task  # noqa: E501

        :return: The operation of this ReplicationTask.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this ReplicationTask.

        The operation of the task  # noqa: E501

        :param operation: The operation of this ReplicationTask.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def resource_type(self):
        """Gets the resource_type of this ReplicationTask.  # noqa: E501

        The type of the resource that the task operates  # noqa: E501

        :return: The resource_type of this ReplicationTask.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ReplicationTask.

        The type of the resource that the task operates  # noqa: E501

        :param resource_type: The resource_type of this ReplicationTask.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def src_resource(self):
        """Gets the src_resource of this ReplicationTask.  # noqa: E501

        The source resource that the task operates  # noqa: E501

        :return: The src_resource of this ReplicationTask.  # noqa: E501
        :rtype: str
        """
        return self._src_resource

    @src_resource.setter
    def src_resource(self, src_resource):
        """Sets the src_resource of this ReplicationTask.

        The source resource that the task operates  # noqa: E501

        :param src_resource: The src_resource of this ReplicationTask.  # noqa: E501
        :type: str
        """

        self._src_resource = src_resource

    @property
    def dst_resource(self):
        """Gets the dst_resource of this ReplicationTask.  # noqa: E501

        The destination resource that the task operates  # noqa: E501

        :return: The dst_resource of this ReplicationTask.  # noqa: E501
        :rtype: str
        """
        return self._dst_resource

    @dst_resource.setter
    def dst_resource(self, dst_resource):
        """Sets the dst_resource of this ReplicationTask.

        The destination resource that the task operates  # noqa: E501

        :param dst_resource: The dst_resource of this ReplicationTask.  # noqa: E501
        :type: str
        """

        self._dst_resource = dst_resource

    @property
    def start_time(self):
        """Gets the start_time of this ReplicationTask.  # noqa: E501

        The start time of the task  # noqa: E501

        :return: The start_time of this ReplicationTask.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ReplicationTask.

        The start time of the task  # noqa: E501

        :param start_time: The start_time of this ReplicationTask.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ReplicationTask.  # noqa: E501

        The end time of the task  # noqa: E501

        :return: The end_time of this ReplicationTask.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ReplicationTask.

        The end time of the task  # noqa: E501

        :param end_time: The end_time of this ReplicationTask.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

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
        if issubclass(ReplicationTask, dict):
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
        if not isinstance(other, ReplicationTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReplicationTask):
            return True

        return self.to_dict() != other.to_dict()
