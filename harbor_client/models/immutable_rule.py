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


class ImmutableRule(object):
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
        'id': 'int',
        'priority': 'int',
        'disabled': 'bool',
        'action': 'str',
        'template': 'str',
        'params': 'dict(str, object)',
        'tag_selectors': 'list[ImmutableSelector]',
        'scope_selectors': 'dict(str, list[ImmutableSelector])'
    }

    attribute_map = {
        'id': 'id',
        'priority': 'priority',
        'disabled': 'disabled',
        'action': 'action',
        'template': 'template',
        'params': 'params',
        'tag_selectors': 'tag_selectors',
        'scope_selectors': 'scope_selectors'
    }

    def __init__(self, id=None, priority=None, disabled=None, action=None, template=None, params=None, tag_selectors=None, scope_selectors=None, _configuration=None):  # noqa: E501
        """ImmutableRule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._priority = None
        self._disabled = None
        self._action = None
        self._template = None
        self._params = None
        self._tag_selectors = None
        self._scope_selectors = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if priority is not None:
            self.priority = priority
        if disabled is not None:
            self.disabled = disabled
        if action is not None:
            self.action = action
        if template is not None:
            self.template = template
        if params is not None:
            self.params = params
        if tag_selectors is not None:
            self.tag_selectors = tag_selectors
        if scope_selectors is not None:
            self.scope_selectors = scope_selectors

    @property
    def id(self):
        """Gets the id of this ImmutableRule.  # noqa: E501


        :return: The id of this ImmutableRule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImmutableRule.


        :param id: The id of this ImmutableRule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def priority(self):
        """Gets the priority of this ImmutableRule.  # noqa: E501


        :return: The priority of this ImmutableRule.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ImmutableRule.


        :param priority: The priority of this ImmutableRule.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def disabled(self):
        """Gets the disabled of this ImmutableRule.  # noqa: E501


        :return: The disabled of this ImmutableRule.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this ImmutableRule.


        :param disabled: The disabled of this ImmutableRule.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def action(self):
        """Gets the action of this ImmutableRule.  # noqa: E501


        :return: The action of this ImmutableRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ImmutableRule.


        :param action: The action of this ImmutableRule.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def template(self):
        """Gets the template of this ImmutableRule.  # noqa: E501


        :return: The template of this ImmutableRule.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ImmutableRule.


        :param template: The template of this ImmutableRule.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def params(self):
        """Gets the params of this ImmutableRule.  # noqa: E501


        :return: The params of this ImmutableRule.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ImmutableRule.


        :param params: The params of this ImmutableRule.  # noqa: E501
        :type: dict(str, object)
        """

        self._params = params

    @property
    def tag_selectors(self):
        """Gets the tag_selectors of this ImmutableRule.  # noqa: E501


        :return: The tag_selectors of this ImmutableRule.  # noqa: E501
        :rtype: list[ImmutableSelector]
        """
        return self._tag_selectors

    @tag_selectors.setter
    def tag_selectors(self, tag_selectors):
        """Sets the tag_selectors of this ImmutableRule.


        :param tag_selectors: The tag_selectors of this ImmutableRule.  # noqa: E501
        :type: list[ImmutableSelector]
        """

        self._tag_selectors = tag_selectors

    @property
    def scope_selectors(self):
        """Gets the scope_selectors of this ImmutableRule.  # noqa: E501


        :return: The scope_selectors of this ImmutableRule.  # noqa: E501
        :rtype: dict(str, list[ImmutableSelector])
        """
        return self._scope_selectors

    @scope_selectors.setter
    def scope_selectors(self, scope_selectors):
        """Sets the scope_selectors of this ImmutableRule.


        :param scope_selectors: The scope_selectors of this ImmutableRule.  # noqa: E501
        :type: dict(str, list[ImmutableSelector])
        """

        self._scope_selectors = scope_selectors

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
        if issubclass(ImmutableRule, dict):
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
        if not isinstance(other, ImmutableRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImmutableRule):
            return True

        return self.to_dict() != other.to_dict()
