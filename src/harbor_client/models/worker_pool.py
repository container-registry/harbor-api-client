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


class WorkerPool(object):
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
        "pid": "int",
        "worker_pool_id": "str",
        "start_at": "datetime",
        "heartbeat_at": "datetime",
        "concurrency": "int",
        "host": "str",
    }

    attribute_map = {
        "pid": "pid",
        "worker_pool_id": "worker_pool_id",
        "start_at": "start_at",
        "heartbeat_at": "heartbeat_at",
        "concurrency": "concurrency",
        "host": "host",
    }

    def __init__(
        self,
        pid=None,
        worker_pool_id=None,
        start_at=None,
        heartbeat_at=None,
        concurrency=None,
        host=None,
        _configuration=None,
    ):  # noqa: E501
        """WorkerPool - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pid = None
        self._worker_pool_id = None
        self._start_at = None
        self._heartbeat_at = None
        self._concurrency = None
        self._host = None
        self.discriminator = None

        if pid is not None:
            self.pid = pid
        if worker_pool_id is not None:
            self.worker_pool_id = worker_pool_id
        if start_at is not None:
            self.start_at = start_at
        if heartbeat_at is not None:
            self.heartbeat_at = heartbeat_at
        if concurrency is not None:
            self.concurrency = concurrency
        if host is not None:
            self.host = host

    @property
    def pid(self):
        """Gets the pid of this WorkerPool.  # noqa: E501

        the process id of jobservice  # noqa: E501

        :return: The pid of this WorkerPool.  # noqa: E501
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this WorkerPool.

        the process id of jobservice  # noqa: E501

        :param pid: The pid of this WorkerPool.  # noqa: E501
        :type: int
        """

        self._pid = pid

    @property
    def worker_pool_id(self):
        """Gets the worker_pool_id of this WorkerPool.  # noqa: E501

        the id of the worker pool  # noqa: E501

        :return: The worker_pool_id of this WorkerPool.  # noqa: E501
        :rtype: str
        """
        return self._worker_pool_id

    @worker_pool_id.setter
    def worker_pool_id(self, worker_pool_id):
        """Sets the worker_pool_id of this WorkerPool.

        the id of the worker pool  # noqa: E501

        :param worker_pool_id: The worker_pool_id of this WorkerPool.  # noqa: E501
        :type: str
        """

        self._worker_pool_id = worker_pool_id

    @property
    def start_at(self):
        """Gets the start_at of this WorkerPool.  # noqa: E501

        The start time of the work pool  # noqa: E501

        :return: The start_at of this WorkerPool.  # noqa: E501
        :rtype: datetime
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this WorkerPool.

        The start time of the work pool  # noqa: E501

        :param start_at: The start_at of this WorkerPool.  # noqa: E501
        :type: datetime
        """

        self._start_at = start_at

    @property
    def heartbeat_at(self):
        """Gets the heartbeat_at of this WorkerPool.  # noqa: E501

        The heartbeat time of the work pool  # noqa: E501

        :return: The heartbeat_at of this WorkerPool.  # noqa: E501
        :rtype: datetime
        """
        return self._heartbeat_at

    @heartbeat_at.setter
    def heartbeat_at(self, heartbeat_at):
        """Sets the heartbeat_at of this WorkerPool.

        The heartbeat time of the work pool  # noqa: E501

        :param heartbeat_at: The heartbeat_at of this WorkerPool.  # noqa: E501
        :type: datetime
        """

        self._heartbeat_at = heartbeat_at

    @property
    def concurrency(self):
        """Gets the concurrency of this WorkerPool.  # noqa: E501

        The concurrency of the work pool  # noqa: E501

        :return: The concurrency of this WorkerPool.  # noqa: E501
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this WorkerPool.

        The concurrency of the work pool  # noqa: E501

        :param concurrency: The concurrency of this WorkerPool.  # noqa: E501
        :type: int
        """

        self._concurrency = concurrency

    @property
    def host(self):
        """Gets the host of this WorkerPool.  # noqa: E501

        The host of the work pool  # noqa: E501

        :return: The host of this WorkerPool.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this WorkerPool.

        The host of the work pool  # noqa: E501

        :param host: The host of this WorkerPool.  # noqa: E501
        :type: str
        """

        self._host = host

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
        if issubclass(WorkerPool, dict):
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
        if not isinstance(other, WorkerPool):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkerPool):
            return True

        return self.to_dict() != other.to_dict()
