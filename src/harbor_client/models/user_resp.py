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


class UserResp(object):
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
        "email": "str",
        "realname": "str",
        "comment": "str",
        "user_id": "int",
        "username": "str",
        "sysadmin_flag": "bool",
        "admin_role_in_auth": "bool",
        "oidc_user_meta": "OIDCUserInfo",
        "creation_time": "datetime",
        "update_time": "datetime",
    }

    attribute_map = {
        "email": "email",
        "realname": "realname",
        "comment": "comment",
        "user_id": "user_id",
        "username": "username",
        "sysadmin_flag": "sysadmin_flag",
        "admin_role_in_auth": "admin_role_in_auth",
        "oidc_user_meta": "oidc_user_meta",
        "creation_time": "creation_time",
        "update_time": "update_time",
    }

    def __init__(
        self,
        email=None,
        realname=None,
        comment=None,
        user_id=None,
        username=None,
        sysadmin_flag=None,
        admin_role_in_auth=None,
        oidc_user_meta=None,
        creation_time=None,
        update_time=None,
        _configuration=None,
    ):  # noqa: E501
        """UserResp - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._realname = None
        self._comment = None
        self._user_id = None
        self._username = None
        self._sysadmin_flag = None
        self._admin_role_in_auth = None
        self._oidc_user_meta = None
        self._creation_time = None
        self._update_time = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if realname is not None:
            self.realname = realname
        if comment is not None:
            self.comment = comment
        if user_id is not None:
            self.user_id = user_id
        if username is not None:
            self.username = username
        if sysadmin_flag is not None:
            self.sysadmin_flag = sysadmin_flag
        if admin_role_in_auth is not None:
            self.admin_role_in_auth = admin_role_in_auth
        if oidc_user_meta is not None:
            self.oidc_user_meta = oidc_user_meta
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def email(self):
        """Gets the email of this UserResp.  # noqa: E501


        :return: The email of this UserResp.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserResp.


        :param email: The email of this UserResp.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def realname(self):
        """Gets the realname of this UserResp.  # noqa: E501


        :return: The realname of this UserResp.  # noqa: E501
        :rtype: str
        """
        return self._realname

    @realname.setter
    def realname(self, realname):
        """Sets the realname of this UserResp.


        :param realname: The realname of this UserResp.  # noqa: E501
        :type: str
        """

        self._realname = realname

    @property
    def comment(self):
        """Gets the comment of this UserResp.  # noqa: E501


        :return: The comment of this UserResp.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UserResp.


        :param comment: The comment of this UserResp.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def user_id(self):
        """Gets the user_id of this UserResp.  # noqa: E501


        :return: The user_id of this UserResp.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserResp.


        :param user_id: The user_id of this UserResp.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def username(self):
        """Gets the username of this UserResp.  # noqa: E501


        :return: The username of this UserResp.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserResp.


        :param username: The username of this UserResp.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def sysadmin_flag(self):
        """Gets the sysadmin_flag of this UserResp.  # noqa: E501


        :return: The sysadmin_flag of this UserResp.  # noqa: E501
        :rtype: bool
        """
        return self._sysadmin_flag

    @sysadmin_flag.setter
    def sysadmin_flag(self, sysadmin_flag):
        """Sets the sysadmin_flag of this UserResp.


        :param sysadmin_flag: The sysadmin_flag of this UserResp.  # noqa: E501
        :type: bool
        """

        self._sysadmin_flag = sysadmin_flag

    @property
    def admin_role_in_auth(self):
        """Gets the admin_role_in_auth of this UserResp.  # noqa: E501

        indicate the admin privilege is grant by authenticator (LDAP), is always false unless it is the current login user  # noqa: E501

        :return: The admin_role_in_auth of this UserResp.  # noqa: E501
        :rtype: bool
        """
        return self._admin_role_in_auth

    @admin_role_in_auth.setter
    def admin_role_in_auth(self, admin_role_in_auth):
        """Sets the admin_role_in_auth of this UserResp.

        indicate the admin privilege is grant by authenticator (LDAP), is always false unless it is the current login user  # noqa: E501

        :param admin_role_in_auth: The admin_role_in_auth of this UserResp.  # noqa: E501
        :type: bool
        """

        self._admin_role_in_auth = admin_role_in_auth

    @property
    def oidc_user_meta(self):
        """Gets the oidc_user_meta of this UserResp.  # noqa: E501


        :return: The oidc_user_meta of this UserResp.  # noqa: E501
        :rtype: OIDCUserInfo
        """
        return self._oidc_user_meta

    @oidc_user_meta.setter
    def oidc_user_meta(self, oidc_user_meta):
        """Sets the oidc_user_meta of this UserResp.


        :param oidc_user_meta: The oidc_user_meta of this UserResp.  # noqa: E501
        :type: OIDCUserInfo
        """

        self._oidc_user_meta = oidc_user_meta

    @property
    def creation_time(self):
        """Gets the creation_time of this UserResp.  # noqa: E501

        The creation time of the user.  # noqa: E501

        :return: The creation_time of this UserResp.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this UserResp.

        The creation time of the user.  # noqa: E501

        :param creation_time: The creation_time of this UserResp.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this UserResp.  # noqa: E501

        The update time of the user.  # noqa: E501

        :return: The update_time of this UserResp.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UserResp.

        The update time of the user.  # noqa: E501

        :param update_time: The update_time of this UserResp.  # noqa: E501
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
        if issubclass(UserResp, dict):
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
        if not isinstance(other, UserResp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserResp):
            return True

        return self.to_dict() != other.to_dict()
