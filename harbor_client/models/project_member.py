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


class ProjectMember(object):
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
        'role_id': 'int',
        'member_user': 'UserEntity',
        'member_group': 'UserGroup'
    }

    attribute_map = {
        'role_id': 'role_id',
        'member_user': 'member_user',
        'member_group': 'member_group'
    }

    def __init__(self, role_id=None, member_user=None, member_group=None, _configuration=None):  # noqa: E501
        """ProjectMember - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._role_id = None
        self._member_user = None
        self._member_group = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        if member_user is not None:
            self.member_user = member_user
        if member_group is not None:
            self.member_group = member_group

    @property
    def role_id(self):
        """Gets the role_id of this ProjectMember.  # noqa: E501

        The role id 1 for projectAdmin, 2 for developer, 3 for guest, 4 for maintainer  # noqa: E501

        :return: The role_id of this ProjectMember.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this ProjectMember.

        The role id 1 for projectAdmin, 2 for developer, 3 for guest, 4 for maintainer  # noqa: E501

        :param role_id: The role_id of this ProjectMember.  # noqa: E501
        :type: int
        """

        self._role_id = role_id

    @property
    def member_user(self):
        """Gets the member_user of this ProjectMember.  # noqa: E501


        :return: The member_user of this ProjectMember.  # noqa: E501
        :rtype: UserEntity
        """
        return self._member_user

    @member_user.setter
    def member_user(self, member_user):
        """Sets the member_user of this ProjectMember.


        :param member_user: The member_user of this ProjectMember.  # noqa: E501
        :type: UserEntity
        """

        self._member_user = member_user

    @property
    def member_group(self):
        """Gets the member_group of this ProjectMember.  # noqa: E501


        :return: The member_group of this ProjectMember.  # noqa: E501
        :rtype: UserGroup
        """
        return self._member_group

    @member_group.setter
    def member_group(self, member_group):
        """Sets the member_group of this ProjectMember.


        :param member_group: The member_group of this ProjectMember.  # noqa: E501
        :type: UserGroup
        """

        self._member_group = member_group

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
        if issubclass(ProjectMember, dict):
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
        if not isinstance(other, ProjectMember):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectMember):
            return True

        return self.to_dict() != other.to_dict()
