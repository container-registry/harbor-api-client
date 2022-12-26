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


class Scanner(object):
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
        'name': 'str',
        'vendor': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'vendor': 'vendor',
        'version': 'version'
    }

    def __init__(self, name=None, vendor=None, version=None, _configuration=None):  # noqa: E501
        """Scanner - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._vendor = None
        self._version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if vendor is not None:
            self.vendor = vendor
        if version is not None:
            self.version = version

    @property
    def name(self):
        """Gets the name of this Scanner.  # noqa: E501

        Name of the scanner  # noqa: E501

        :return: The name of this Scanner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Scanner.

        Name of the scanner  # noqa: E501

        :param name: The name of this Scanner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def vendor(self):
        """Gets the vendor of this Scanner.  # noqa: E501

        Name of the scanner provider  # noqa: E501

        :return: The vendor of this Scanner.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this Scanner.

        Name of the scanner provider  # noqa: E501

        :param vendor: The vendor of this Scanner.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def version(self):
        """Gets the version of this Scanner.  # noqa: E501

        Version of the scanner adapter  # noqa: E501

        :return: The version of this Scanner.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Scanner.

        Version of the scanner adapter  # noqa: E501

        :param version: The version of this Scanner.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(Scanner, dict):
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
        if not isinstance(other, Scanner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Scanner):
            return True

        return self.to_dict() != other.to_dict()