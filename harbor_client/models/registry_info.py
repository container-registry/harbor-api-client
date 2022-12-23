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


class RegistryInfo(object):
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
        'type': 'str',
        'description': 'str',
        'supported_resource_filters': 'list[FilterStyle]',
        'supported_triggers': 'list[str]',
        'supported_copy_by_chunk': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'description': 'description',
        'supported_resource_filters': 'supported_resource_filters',
        'supported_triggers': 'supported_triggers',
        'supported_copy_by_chunk': 'supported_copy_by_chunk'
    }

    def __init__(self, type=None, description=None, supported_resource_filters=None, supported_triggers=None, supported_copy_by_chunk=None, _configuration=None):  # noqa: E501
        """RegistryInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._description = None
        self._supported_resource_filters = None
        self._supported_triggers = None
        self._supported_copy_by_chunk = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if supported_resource_filters is not None:
            self.supported_resource_filters = supported_resource_filters
        if supported_triggers is not None:
            self.supported_triggers = supported_triggers
        if supported_copy_by_chunk is not None:
            self.supported_copy_by_chunk = supported_copy_by_chunk

    @property
    def type(self):
        """Gets the type of this RegistryInfo.  # noqa: E501

        The registry type  # noqa: E501

        :return: The type of this RegistryInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RegistryInfo.

        The registry type  # noqa: E501

        :param type: The type of this RegistryInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this RegistryInfo.  # noqa: E501

        The description  # noqa: E501

        :return: The description of this RegistryInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RegistryInfo.

        The description  # noqa: E501

        :param description: The description of this RegistryInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def supported_resource_filters(self):
        """Gets the supported_resource_filters of this RegistryInfo.  # noqa: E501

        The filters that the registry supports  # noqa: E501

        :return: The supported_resource_filters of this RegistryInfo.  # noqa: E501
        :rtype: list[FilterStyle]
        """
        return self._supported_resource_filters

    @supported_resource_filters.setter
    def supported_resource_filters(self, supported_resource_filters):
        """Sets the supported_resource_filters of this RegistryInfo.

        The filters that the registry supports  # noqa: E501

        :param supported_resource_filters: The supported_resource_filters of this RegistryInfo.  # noqa: E501
        :type: list[FilterStyle]
        """

        self._supported_resource_filters = supported_resource_filters

    @property
    def supported_triggers(self):
        """Gets the supported_triggers of this RegistryInfo.  # noqa: E501

        The triggers that the registry supports  # noqa: E501

        :return: The supported_triggers of this RegistryInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_triggers

    @supported_triggers.setter
    def supported_triggers(self, supported_triggers):
        """Sets the supported_triggers of this RegistryInfo.

        The triggers that the registry supports  # noqa: E501

        :param supported_triggers: The supported_triggers of this RegistryInfo.  # noqa: E501
        :type: list[str]
        """

        self._supported_triggers = supported_triggers

    @property
    def supported_copy_by_chunk(self):
        """Gets the supported_copy_by_chunk of this RegistryInfo.  # noqa: E501

        The registry whether support copy by chunk.  # noqa: E501

        :return: The supported_copy_by_chunk of this RegistryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._supported_copy_by_chunk

    @supported_copy_by_chunk.setter
    def supported_copy_by_chunk(self, supported_copy_by_chunk):
        """Sets the supported_copy_by_chunk of this RegistryInfo.

        The registry whether support copy by chunk.  # noqa: E501

        :param supported_copy_by_chunk: The supported_copy_by_chunk of this RegistryInfo.  # noqa: E501
        :type: bool
        """

        self._supported_copy_by_chunk = supported_copy_by_chunk

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
        if issubclass(RegistryInfo, dict):
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
        if not isinstance(other, RegistryInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistryInfo):
            return True

        return self.to_dict() != other.to_dict()
