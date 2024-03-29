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


class WebhookLastTrigger(object):
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
        "policy_name": "str",
        "event_type": "str",
        "enabled": "bool",
        "creation_time": "datetime",
        "last_trigger_time": "datetime",
    }

    attribute_map = {
        "policy_name": "policy_name",
        "event_type": "event_type",
        "enabled": "enabled",
        "creation_time": "creation_time",
        "last_trigger_time": "last_trigger_time",
    }

    def __init__(
        self,
        policy_name=None,
        event_type=None,
        enabled=None,
        creation_time=None,
        last_trigger_time=None,
        _configuration=None,
    ):  # noqa: E501
        """WebhookLastTrigger - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._policy_name = None
        self._event_type = None
        self._enabled = None
        self._creation_time = None
        self._last_trigger_time = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if event_type is not None:
            self.event_type = event_type
        if enabled is not None:
            self.enabled = enabled
        if creation_time is not None:
            self.creation_time = creation_time
        if last_trigger_time is not None:
            self.last_trigger_time = last_trigger_time

    @property
    def policy_name(self):
        """Gets the policy_name of this WebhookLastTrigger.  # noqa: E501

        The webhook policy name.  # noqa: E501

        :return: The policy_name of this WebhookLastTrigger.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this WebhookLastTrigger.

        The webhook policy name.  # noqa: E501

        :param policy_name: The policy_name of this WebhookLastTrigger.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def event_type(self):
        """Gets the event_type of this WebhookLastTrigger.  # noqa: E501

        The webhook event type.  # noqa: E501

        :return: The event_type of this WebhookLastTrigger.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this WebhookLastTrigger.

        The webhook event type.  # noqa: E501

        :param event_type: The event_type of this WebhookLastTrigger.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def enabled(self):
        """Gets the enabled of this WebhookLastTrigger.  # noqa: E501

        Whether or not the webhook policy enabled.  # noqa: E501

        :return: The enabled of this WebhookLastTrigger.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this WebhookLastTrigger.

        Whether or not the webhook policy enabled.  # noqa: E501

        :param enabled: The enabled of this WebhookLastTrigger.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def creation_time(self):
        """Gets the creation_time of this WebhookLastTrigger.  # noqa: E501

        The creation time of webhook policy.  # noqa: E501

        :return: The creation_time of this WebhookLastTrigger.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this WebhookLastTrigger.

        The creation time of webhook policy.  # noqa: E501

        :param creation_time: The creation_time of this WebhookLastTrigger.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def last_trigger_time(self):
        """Gets the last_trigger_time of this WebhookLastTrigger.  # noqa: E501

        The last trigger time of webhook policy.  # noqa: E501

        :return: The last_trigger_time of this WebhookLastTrigger.  # noqa: E501
        :rtype: datetime
        """
        return self._last_trigger_time

    @last_trigger_time.setter
    def last_trigger_time(self, last_trigger_time):
        """Sets the last_trigger_time of this WebhookLastTrigger.

        The last trigger time of webhook policy.  # noqa: E501

        :param last_trigger_time: The last_trigger_time of this WebhookLastTrigger.  # noqa: E501
        :type: datetime
        """

        self._last_trigger_time = last_trigger_time

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
        if issubclass(WebhookLastTrigger, dict):
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
        if not isinstance(other, WebhookLastTrigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookLastTrigger):
            return True

        return self.to_dict() != other.to_dict()
