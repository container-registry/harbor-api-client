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


class BoolConfigItem(object):
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
    swagger_types = {"value": "bool", "editable": "bool"}

    attribute_map = {"value": "value", "editable": "editable"}

    def __init__(self, value=None, editable=None, _configuration=None):  # noqa: E501
        """BoolConfigItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._value = None
        self._editable = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if editable is not None:
            self.editable = editable

    @property
    def value(self):
        """Gets the value of this BoolConfigItem.  # noqa: E501

        The boolean value of current config item  # noqa: E501

        :return: The value of this BoolConfigItem.  # noqa: E501
        :rtype: bool
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BoolConfigItem.

        The boolean value of current config item  # noqa: E501

        :param value: The value of this BoolConfigItem.  # noqa: E501
        :type: bool
        """

        self._value = value

    @property
    def editable(self):
        """Gets the editable of this BoolConfigItem.  # noqa: E501

        The configure item can be updated or not  # noqa: E501

        :return: The editable of this BoolConfigItem.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this BoolConfigItem.

        The configure item can be updated or not  # noqa: E501

        :param editable: The editable of this BoolConfigItem.  # noqa: E501
        :type: bool
        """

        self._editable = editable

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
        if issubclass(BoolConfigItem, dict):
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
        if not isinstance(other, BoolConfigItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BoolConfigItem):
            return True

        return self.to_dict() != other.to_dict()
