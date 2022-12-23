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


class Tag(object):
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
        'repository_id': 'int',
        'artifact_id': 'int',
        'name': 'str',
        'push_time': 'datetime',
        'pull_time': 'datetime',
        'immutable': 'bool',
        'signed': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'repository_id': 'repository_id',
        'artifact_id': 'artifact_id',
        'name': 'name',
        'push_time': 'push_time',
        'pull_time': 'pull_time',
        'immutable': 'immutable',
        'signed': 'signed'
    }

    def __init__(self, id=None, repository_id=None, artifact_id=None, name=None, push_time=None, pull_time=None, immutable=None, signed=None, _configuration=None):  # noqa: E501
        """Tag - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._repository_id = None
        self._artifact_id = None
        self._name = None
        self._push_time = None
        self._pull_time = None
        self._immutable = None
        self._signed = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if repository_id is not None:
            self.repository_id = repository_id
        if artifact_id is not None:
            self.artifact_id = artifact_id
        if name is not None:
            self.name = name
        if push_time is not None:
            self.push_time = push_time
        if pull_time is not None:
            self.pull_time = pull_time
        if immutable is not None:
            self.immutable = immutable
        if signed is not None:
            self.signed = signed

    @property
    def id(self):
        """Gets the id of this Tag.  # noqa: E501

        The ID of the tag  # noqa: E501

        :return: The id of this Tag.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tag.

        The ID of the tag  # noqa: E501

        :param id: The id of this Tag.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def repository_id(self):
        """Gets the repository_id of this Tag.  # noqa: E501

        The ID of the repository that the tag belongs to  # noqa: E501

        :return: The repository_id of this Tag.  # noqa: E501
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this Tag.

        The ID of the repository that the tag belongs to  # noqa: E501

        :param repository_id: The repository_id of this Tag.  # noqa: E501
        :type: int
        """

        self._repository_id = repository_id

    @property
    def artifact_id(self):
        """Gets the artifact_id of this Tag.  # noqa: E501

        The ID of the artifact that the tag attached to  # noqa: E501

        :return: The artifact_id of this Tag.  # noqa: E501
        :rtype: int
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """Sets the artifact_id of this Tag.

        The ID of the artifact that the tag attached to  # noqa: E501

        :param artifact_id: The artifact_id of this Tag.  # noqa: E501
        :type: int
        """

        self._artifact_id = artifact_id

    @property
    def name(self):
        """Gets the name of this Tag.  # noqa: E501

        The name of the tag  # noqa: E501

        :return: The name of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.

        The name of the tag  # noqa: E501

        :param name: The name of this Tag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def push_time(self):
        """Gets the push_time of this Tag.  # noqa: E501

        The push time of the tag  # noqa: E501

        :return: The push_time of this Tag.  # noqa: E501
        :rtype: datetime
        """
        return self._push_time

    @push_time.setter
    def push_time(self, push_time):
        """Sets the push_time of this Tag.

        The push time of the tag  # noqa: E501

        :param push_time: The push_time of this Tag.  # noqa: E501
        :type: datetime
        """

        self._push_time = push_time

    @property
    def pull_time(self):
        """Gets the pull_time of this Tag.  # noqa: E501

        The latest pull time of the tag  # noqa: E501

        :return: The pull_time of this Tag.  # noqa: E501
        :rtype: datetime
        """
        return self._pull_time

    @pull_time.setter
    def pull_time(self, pull_time):
        """Sets the pull_time of this Tag.

        The latest pull time of the tag  # noqa: E501

        :param pull_time: The pull_time of this Tag.  # noqa: E501
        :type: datetime
        """

        self._pull_time = pull_time

    @property
    def immutable(self):
        """Gets the immutable of this Tag.  # noqa: E501

        The immutable status of the tag  # noqa: E501

        :return: The immutable of this Tag.  # noqa: E501
        :rtype: bool
        """
        return self._immutable

    @immutable.setter
    def immutable(self, immutable):
        """Sets the immutable of this Tag.

        The immutable status of the tag  # noqa: E501

        :param immutable: The immutable of this Tag.  # noqa: E501
        :type: bool
        """

        self._immutable = immutable

    @property
    def signed(self):
        """Gets the signed of this Tag.  # noqa: E501

        The attribute indicates whether the tag is signed or not  # noqa: E501

        :return: The signed of this Tag.  # noqa: E501
        :rtype: bool
        """
        return self._signed

    @signed.setter
    def signed(self, signed):
        """Sets the signed of this Tag.

        The attribute indicates whether the tag is signed or not  # noqa: E501

        :param signed: The signed of this Tag.  # noqa: E501
        :type: bool
        """

        self._signed = signed

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
        if issubclass(Tag, dict):
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
        if not isinstance(other, Tag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tag):
            return True

        return self.to_dict() != other.to_dict()
