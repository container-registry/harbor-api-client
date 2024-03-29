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


class RetentionSelectorMetadata(object):
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
    swagger_types = {"display_text": "str", "kind": "str", "decorations": "list[str]"}

    attribute_map = {"display_text": "display_text", "kind": "kind", "decorations": "decorations"}

    def __init__(
        self, display_text=None, kind=None, decorations=None, _configuration=None
    ):  # noqa: E501
        """RetentionSelectorMetadata - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display_text = None
        self._kind = None
        self._decorations = None
        self.discriminator = None

        if display_text is not None:
            self.display_text = display_text
        if kind is not None:
            self.kind = kind
        if decorations is not None:
            self.decorations = decorations

    @property
    def display_text(self):
        """Gets the display_text of this RetentionSelectorMetadata.  # noqa: E501


        :return: The display_text of this RetentionSelectorMetadata.  # noqa: E501
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        """Sets the display_text of this RetentionSelectorMetadata.


        :param display_text: The display_text of this RetentionSelectorMetadata.  # noqa: E501
        :type: str
        """

        self._display_text = display_text

    @property
    def kind(self):
        """Gets the kind of this RetentionSelectorMetadata.  # noqa: E501


        :return: The kind of this RetentionSelectorMetadata.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this RetentionSelectorMetadata.


        :param kind: The kind of this RetentionSelectorMetadata.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def decorations(self):
        """Gets the decorations of this RetentionSelectorMetadata.  # noqa: E501


        :return: The decorations of this RetentionSelectorMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._decorations

    @decorations.setter
    def decorations(self, decorations):
        """Sets the decorations of this RetentionSelectorMetadata.


        :param decorations: The decorations of this RetentionSelectorMetadata.  # noqa: E501
        :type: list[str]
        """

        self._decorations = decorations

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
        if issubclass(RetentionSelectorMetadata, dict):
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
        if not isinstance(other, RetentionSelectorMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RetentionSelectorMetadata):
            return True

        return self.to_dict() != other.to_dict()
