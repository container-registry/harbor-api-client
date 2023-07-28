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


class ProjectMemberEntity(object):
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
        "id": "int",
        "project_id": "int",
        "entity_name": "str",
        "role_name": "str",
        "role_id": "int",
        "entity_id": "int",
        "entity_type": "str",
    }

    attribute_map = {
        "id": "id",
        "project_id": "project_id",
        "entity_name": "entity_name",
        "role_name": "role_name",
        "role_id": "role_id",
        "entity_id": "entity_id",
        "entity_type": "entity_type",
    }

    def __init__(
        self,
        id=None,
        project_id=None,
        entity_name=None,
        role_name=None,
        role_id=None,
        entity_id=None,
        entity_type=None,
        _configuration=None,
    ):  # noqa: E501
        """ProjectMemberEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._project_id = None
        self._entity_name = None
        self._role_name = None
        self._role_id = None
        self._entity_id = None
        self._entity_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if entity_name is not None:
            self.entity_name = entity_name
        if role_name is not None:
            self.role_name = role_name
        if role_id is not None:
            self.role_id = role_id
        if entity_id is not None:
            self.entity_id = entity_id
        if entity_type is not None:
            self.entity_type = entity_type

    @property
    def id(self):
        """Gets the id of this ProjectMemberEntity.  # noqa: E501

        the project member id  # noqa: E501

        :return: The id of this ProjectMemberEntity.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectMemberEntity.

        the project member id  # noqa: E501

        :param id: The id of this ProjectMemberEntity.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this ProjectMemberEntity.  # noqa: E501

        the project id  # noqa: E501

        :return: The project_id of this ProjectMemberEntity.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ProjectMemberEntity.

        the project id  # noqa: E501

        :param project_id: The project_id of this ProjectMemberEntity.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def entity_name(self):
        """Gets the entity_name of this ProjectMemberEntity.  # noqa: E501

        the name of the group member.  # noqa: E501

        :return: The entity_name of this ProjectMemberEntity.  # noqa: E501
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this ProjectMemberEntity.

        the name of the group member.  # noqa: E501

        :param entity_name: The entity_name of this ProjectMemberEntity.  # noqa: E501
        :type: str
        """

        self._entity_name = entity_name

    @property
    def role_name(self):
        """Gets the role_name of this ProjectMemberEntity.  # noqa: E501

        the name of the role  # noqa: E501

        :return: The role_name of this ProjectMemberEntity.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this ProjectMemberEntity.

        the name of the role  # noqa: E501

        :param role_name: The role_name of this ProjectMemberEntity.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

    @property
    def role_id(self):
        """Gets the role_id of this ProjectMemberEntity.  # noqa: E501

        the role id  # noqa: E501

        :return: The role_id of this ProjectMemberEntity.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this ProjectMemberEntity.

        the role id  # noqa: E501

        :param role_id: The role_id of this ProjectMemberEntity.  # noqa: E501
        :type: int
        """

        self._role_id = role_id

    @property
    def entity_id(self):
        """Gets the entity_id of this ProjectMemberEntity.  # noqa: E501

        the id of entity, if the member is a user, it is user_id in user table. if the member is a user group, it is the user group's ID in user_group table.  # noqa: E501

        :return: The entity_id of this ProjectMemberEntity.  # noqa: E501
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this ProjectMemberEntity.

        the id of entity, if the member is a user, it is user_id in user table. if the member is a user group, it is the user group's ID in user_group table.  # noqa: E501

        :param entity_id: The entity_id of this ProjectMemberEntity.  # noqa: E501
        :type: int
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this ProjectMemberEntity.  # noqa: E501

        the entity's type, u for user entity, g for group entity.  # noqa: E501

        :return: The entity_type of this ProjectMemberEntity.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ProjectMemberEntity.

        the entity's type, u for user entity, g for group entity.  # noqa: E501

        :param entity_type: The entity_type of this ProjectMemberEntity.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

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
        if issubclass(ProjectMemberEntity, dict):
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
        if not isinstance(other, ProjectMemberEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectMemberEntity):
            return True

        return self.to_dict() != other.to_dict()
