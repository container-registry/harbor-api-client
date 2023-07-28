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


class Registry(object):
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
        "url": "str",
        "name": "str",
        "credential": "RegistryCredential",
        "type": "str",
        "insecure": "bool",
        "description": "str",
        "status": "str",
        "creation_time": "datetime",
        "update_time": "datetime",
    }

    attribute_map = {
        "id": "id",
        "url": "url",
        "name": "name",
        "credential": "credential",
        "type": "type",
        "insecure": "insecure",
        "description": "description",
        "status": "status",
        "creation_time": "creation_time",
        "update_time": "update_time",
    }

    def __init__(
        self,
        id=None,
        url=None,
        name=None,
        credential=None,
        type=None,
        insecure=None,
        description=None,
        status=None,
        creation_time=None,
        update_time=None,
        _configuration=None,
    ):  # noqa: E501
        """Registry - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._url = None
        self._name = None
        self._credential = None
        self._type = None
        self._insecure = None
        self._description = None
        self._status = None
        self._creation_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if name is not None:
            self.name = name
        if credential is not None:
            self.credential = credential
        if type is not None:
            self.type = type
        if insecure is not None:
            self.insecure = insecure
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this Registry.  # noqa: E501

        The registry ID.  # noqa: E501

        :return: The id of this Registry.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Registry.

        The registry ID.  # noqa: E501

        :param id: The id of this Registry.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this Registry.  # noqa: E501

        The registry URL string.  # noqa: E501

        :return: The url of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Registry.

        The registry URL string.  # noqa: E501

        :param url: The url of this Registry.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this Registry.  # noqa: E501

        The registry name.  # noqa: E501

        :return: The name of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Registry.

        The registry name.  # noqa: E501

        :param name: The name of this Registry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def credential(self):
        """Gets the credential of this Registry.  # noqa: E501


        :return: The credential of this Registry.  # noqa: E501
        :rtype: RegistryCredential
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this Registry.


        :param credential: The credential of this Registry.  # noqa: E501
        :type: RegistryCredential
        """

        self._credential = credential

    @property
    def type(self):
        """Gets the type of this Registry.  # noqa: E501

        Type of the registry, e.g. 'harbor'.  # noqa: E501

        :return: The type of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Registry.

        Type of the registry, e.g. 'harbor'.  # noqa: E501

        :param type: The type of this Registry.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def insecure(self):
        """Gets the insecure of this Registry.  # noqa: E501

        Whether or not the certificate will be verified when Harbor tries to access the server.  # noqa: E501

        :return: The insecure of this Registry.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this Registry.

        Whether or not the certificate will be verified when Harbor tries to access the server.  # noqa: E501

        :param insecure: The insecure of this Registry.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

    @property
    def description(self):
        """Gets the description of this Registry.  # noqa: E501

        Description of the registry.  # noqa: E501

        :return: The description of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Registry.

        Description of the registry.  # noqa: E501

        :param description: The description of this Registry.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this Registry.  # noqa: E501

        Health status of the registry.  # noqa: E501

        :return: The status of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Registry.

        Health status of the registry.  # noqa: E501

        :param status: The status of this Registry.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def creation_time(self):
        """Gets the creation_time of this Registry.  # noqa: E501

        The create time of the policy.  # noqa: E501

        :return: The creation_time of this Registry.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Registry.

        The create time of the policy.  # noqa: E501

        :param creation_time: The creation_time of this Registry.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this Registry.  # noqa: E501

        The update time of the policy.  # noqa: E501

        :return: The update_time of this Registry.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Registry.

        The update time of the policy.  # noqa: E501

        :param update_time: The update_time of this Registry.  # noqa: E501
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
        if issubclass(Registry, dict):
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
        if not isinstance(other, Registry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Registry):
            return True

        return self.to_dict() != other.to_dict()
