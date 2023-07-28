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


class RegistryProviderEndpointPattern(object):
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
    swagger_types = {"endpoint_type": "str", "endpoints": "list[RegistryEndpoint]"}

    attribute_map = {"endpoint_type": "endpoint_type", "endpoints": "endpoints"}

    def __init__(self, endpoint_type=None, endpoints=None, _configuration=None):  # noqa: E501
        """RegistryProviderEndpointPattern - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._endpoint_type = None
        self._endpoints = None
        self.discriminator = None

        if endpoint_type is not None:
            self.endpoint_type = endpoint_type
        if endpoints is not None:
            self.endpoints = endpoints

    @property
    def endpoint_type(self):
        """Gets the endpoint_type of this RegistryProviderEndpointPattern.  # noqa: E501

        The endpoint type  # noqa: E501

        :return: The endpoint_type of this RegistryProviderEndpointPattern.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """Sets the endpoint_type of this RegistryProviderEndpointPattern.

        The endpoint type  # noqa: E501

        :param endpoint_type: The endpoint_type of this RegistryProviderEndpointPattern.  # noqa: E501
        :type: str
        """

        self._endpoint_type = endpoint_type

    @property
    def endpoints(self):
        """Gets the endpoints of this RegistryProviderEndpointPattern.  # noqa: E501

        The endpoint list  # noqa: E501

        :return: The endpoints of this RegistryProviderEndpointPattern.  # noqa: E501
        :rtype: list[RegistryEndpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this RegistryProviderEndpointPattern.

        The endpoint list  # noqa: E501

        :param endpoints: The endpoints of this RegistryProviderEndpointPattern.  # noqa: E501
        :type: list[RegistryEndpoint]
        """

        self._endpoints = endpoints

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
        if issubclass(RegistryProviderEndpointPattern, dict):
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
        if not isinstance(other, RegistryProviderEndpointPattern):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistryProviderEndpointPattern):
            return True

        return self.to_dict() != other.to_dict()
