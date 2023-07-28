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


class OverallHealthStatus(object):
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
    swagger_types = {"status": "str", "components": "list[ComponentHealthStatus]"}

    attribute_map = {"status": "status", "components": "components"}

    def __init__(self, status=None, components=None, _configuration=None):  # noqa: E501
        """OverallHealthStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._components = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if components is not None:
            self.components = components

    @property
    def status(self):
        """Gets the status of this OverallHealthStatus.  # noqa: E501

        The overall health status. It is \"healthy\" only when all the components' status are \"healthy\"  # noqa: E501

        :return: The status of this OverallHealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OverallHealthStatus.

        The overall health status. It is \"healthy\" only when all the components' status are \"healthy\"  # noqa: E501

        :param status: The status of this OverallHealthStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def components(self):
        """Gets the components of this OverallHealthStatus.  # noqa: E501


        :return: The components of this OverallHealthStatus.  # noqa: E501
        :rtype: list[ComponentHealthStatus]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this OverallHealthStatus.


        :param components: The components of this OverallHealthStatus.  # noqa: E501
        :type: list[ComponentHealthStatus]
        """

        self._components = components

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
        if issubclass(OverallHealthStatus, dict):
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
        if not isinstance(other, OverallHealthStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OverallHealthStatus):
            return True

        return self.to_dict() != other.to_dict()
