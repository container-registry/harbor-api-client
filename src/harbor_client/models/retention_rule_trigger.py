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


class RetentionRuleTrigger(object):
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
    swagger_types = {"kind": "str", "settings": "object", "references": "object"}

    attribute_map = {"kind": "kind", "settings": "settings", "references": "references"}

    def __init__(
        self, kind=None, settings=None, references=None, _configuration=None
    ):  # noqa: E501
        """RetentionRuleTrigger - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._kind = None
        self._settings = None
        self._references = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if settings is not None:
            self.settings = settings
        if references is not None:
            self.references = references

    @property
    def kind(self):
        """Gets the kind of this RetentionRuleTrigger.  # noqa: E501


        :return: The kind of this RetentionRuleTrigger.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this RetentionRuleTrigger.


        :param kind: The kind of this RetentionRuleTrigger.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def settings(self):
        """Gets the settings of this RetentionRuleTrigger.  # noqa: E501


        :return: The settings of this RetentionRuleTrigger.  # noqa: E501
        :rtype: object
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this RetentionRuleTrigger.


        :param settings: The settings of this RetentionRuleTrigger.  # noqa: E501
        :type: object
        """

        self._settings = settings

    @property
    def references(self):
        """Gets the references of this RetentionRuleTrigger.  # noqa: E501


        :return: The references of this RetentionRuleTrigger.  # noqa: E501
        :rtype: object
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this RetentionRuleTrigger.


        :param references: The references of this RetentionRuleTrigger.  # noqa: E501
        :type: object
        """

        self._references = references

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
        if issubclass(RetentionRuleTrigger, dict):
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
        if not isinstance(other, RetentionRuleTrigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RetentionRuleTrigger):
            return True

        return self.to_dict() != other.to_dict()
