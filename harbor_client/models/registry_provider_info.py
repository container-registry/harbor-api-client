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


class RegistryProviderInfo(object):
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
        'endpoint_pattern': 'RegistryProviderEndpointPattern',
        'credential_pattern': 'RegistryProviderCredentialPattern'
    }

    attribute_map = {
        'endpoint_pattern': 'endpoint_pattern',
        'credential_pattern': 'credential_pattern'
    }

    def __init__(self, endpoint_pattern=None, credential_pattern=None, _configuration=None):  # noqa: E501
        """RegistryProviderInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._endpoint_pattern = None
        self._credential_pattern = None
        self.discriminator = None

        if endpoint_pattern is not None:
            self.endpoint_pattern = endpoint_pattern
        if credential_pattern is not None:
            self.credential_pattern = credential_pattern

    @property
    def endpoint_pattern(self):
        """Gets the endpoint_pattern of this RegistryProviderInfo.  # noqa: E501

        The endpoint pattern  # noqa: E501

        :return: The endpoint_pattern of this RegistryProviderInfo.  # noqa: E501
        :rtype: RegistryProviderEndpointPattern
        """
        return self._endpoint_pattern

    @endpoint_pattern.setter
    def endpoint_pattern(self, endpoint_pattern):
        """Sets the endpoint_pattern of this RegistryProviderInfo.

        The endpoint pattern  # noqa: E501

        :param endpoint_pattern: The endpoint_pattern of this RegistryProviderInfo.  # noqa: E501
        :type: RegistryProviderEndpointPattern
        """

        self._endpoint_pattern = endpoint_pattern

    @property
    def credential_pattern(self):
        """Gets the credential_pattern of this RegistryProviderInfo.  # noqa: E501

        The credential pattern  # noqa: E501

        :return: The credential_pattern of this RegistryProviderInfo.  # noqa: E501
        :rtype: RegistryProviderCredentialPattern
        """
        return self._credential_pattern

    @credential_pattern.setter
    def credential_pattern(self, credential_pattern):
        """Sets the credential_pattern of this RegistryProviderInfo.

        The credential pattern  # noqa: E501

        :param credential_pattern: The credential_pattern of this RegistryProviderInfo.  # noqa: E501
        :type: RegistryProviderCredentialPattern
        """

        self._credential_pattern = credential_pattern

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
        if issubclass(RegistryProviderInfo, dict):
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
        if not isinstance(other, RegistryProviderInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistryProviderInfo):
            return True

        return self.to_dict() != other.to_dict()
