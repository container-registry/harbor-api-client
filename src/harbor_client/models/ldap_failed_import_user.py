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


class LdapFailedImportUser(object):
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
    swagger_types = {"uid": "str", "error": "str"}

    attribute_map = {"uid": "uid", "error": "error"}

    def __init__(self, uid=None, error=None, _configuration=None):  # noqa: E501
        """LdapFailedImportUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._uid = None
        self._error = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if error is not None:
            self.error = error

    @property
    def uid(self):
        """Gets the uid of this LdapFailedImportUser.  # noqa: E501

        the uid can't add to system.  # noqa: E501

        :return: The uid of this LdapFailedImportUser.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this LdapFailedImportUser.

        the uid can't add to system.  # noqa: E501

        :param uid: The uid of this LdapFailedImportUser.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def error(self):
        """Gets the error of this LdapFailedImportUser.  # noqa: E501

        fail reason.  # noqa: E501

        :return: The error of this LdapFailedImportUser.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this LdapFailedImportUser.

        fail reason.  # noqa: E501

        :param error: The error of this LdapFailedImportUser.  # noqa: E501
        :type: str
        """

        self._error = error

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
        if issubclass(LdapFailedImportUser, dict):
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
        if not isinstance(other, LdapFailedImportUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LdapFailedImportUser):
            return True

        return self.to_dict() != other.to_dict()
