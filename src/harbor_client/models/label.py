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


class Label(object):
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
        "name": "str",
        "description": "str",
        "color": "str",
        "scope": "str",
        "project_id": "int",
        "creation_time": "datetime",
        "update_time": "datetime",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "description": "description",
        "color": "color",
        "scope": "scope",
        "project_id": "project_id",
        "creation_time": "creation_time",
        "update_time": "update_time",
    }

    def __init__(
        self,
        id=None,
        name=None,
        description=None,
        color=None,
        scope=None,
        project_id=None,
        creation_time=None,
        update_time=None,
        _configuration=None,
    ):  # noqa: E501
        """Label - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._color = None
        self._scope = None
        self._project_id = None
        self._creation_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if color is not None:
            self.color = color
        if scope is not None:
            self.scope = scope
        if project_id is not None:
            self.project_id = project_id
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this Label.  # noqa: E501

        The ID of the label  # noqa: E501

        :return: The id of this Label.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Label.

        The ID of the label  # noqa: E501

        :param id: The id of this Label.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Label.  # noqa: E501

        The name the label  # noqa: E501

        :return: The name of this Label.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Label.

        The name the label  # noqa: E501

        :param name: The name of this Label.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Label.  # noqa: E501

        The description the label  # noqa: E501

        :return: The description of this Label.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Label.

        The description the label  # noqa: E501

        :param description: The description of this Label.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def color(self):
        """Gets the color of this Label.  # noqa: E501

        The color the label  # noqa: E501

        :return: The color of this Label.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Label.

        The color the label  # noqa: E501

        :param color: The color of this Label.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def scope(self):
        """Gets the scope of this Label.  # noqa: E501

        The scope the label  # noqa: E501

        :return: The scope of this Label.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Label.

        The scope the label  # noqa: E501

        :param scope: The scope of this Label.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def project_id(self):
        """Gets the project_id of this Label.  # noqa: E501

        The ID of project that the label belongs to  # noqa: E501

        :return: The project_id of this Label.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Label.

        The ID of project that the label belongs to  # noqa: E501

        :param project_id: The project_id of this Label.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def creation_time(self):
        """Gets the creation_time of this Label.  # noqa: E501

        The creation time the label  # noqa: E501

        :return: The creation_time of this Label.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Label.

        The creation time the label  # noqa: E501

        :param creation_time: The creation_time of this Label.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this Label.  # noqa: E501

        The update time of the label  # noqa: E501

        :return: The update_time of this Label.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Label.

        The update time of the label  # noqa: E501

        :param update_time: The update_time of this Label.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

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
        if issubclass(Label, dict):
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
        if not isinstance(other, Label):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Label):
            return True

        return self.to_dict() != other.to_dict()
