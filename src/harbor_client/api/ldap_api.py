# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from harbor_client.api_client import ApiClient


class LdapApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def import_ldap_user(self, uid_list, **kwargs):  # noqa: E501
        """Import selected available ldap users.  # noqa: E501

        This endpoint adds the selected available ldap users to harbor based on related configuration parameters from the system. System will try to guess the user email address and realname, add to harbor user information. If have errors when import user, will return the list of importing failed uid and the failed reason.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_ldap_user(uid_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LdapImportUsers uid_list: The uid listed for importing. This list will check users validity of ldap service based on configuration from the system. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.import_ldap_user_with_http_info(uid_list, **kwargs)  # noqa: E501
        else:
            (data) = self.import_ldap_user_with_http_info(uid_list, **kwargs)  # noqa: E501
            return data

    def import_ldap_user_with_http_info(self, uid_list, **kwargs):  # noqa: E501
        """Import selected available ldap users.  # noqa: E501

        This endpoint adds the selected available ldap users to harbor based on related configuration parameters from the system. System will try to guess the user email address and realname, add to harbor user information. If have errors when import user, will return the list of importing failed uid and the failed reason.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_ldap_user_with_http_info(uid_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LdapImportUsers uid_list: The uid listed for importing. This list will check users validity of ldap service based on configuration from the system. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["uid_list", "x_request_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method import_ldap_user" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'uid_list' is set
        if self.api_client.client_side_validation and (
            "uid_list" not in params or params["uid_list"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `uid_list` when calling `import_ldap_user`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `import_ldap_user`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if "uid_list" in params:
            body_params = params["uid_list"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basic"]  # noqa: E501

        return self.api_client.call_api(
            "/ldap/users/import",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def ping_ldap(self, **kwargs):  # noqa: E501
        """Ping available ldap service.  # noqa: E501

        This endpoint ping the available ldap service for test related configuration parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ping_ldap(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :param LdapConf ldapconf: ldap configuration. support input ldap service configuration. If it is a empty request, will load current configuration from the system.
        :return: LdapPingResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.ping_ldap_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.ping_ldap_with_http_info(**kwargs)  # noqa: E501
            return data

    def ping_ldap_with_http_info(self, **kwargs):  # noqa: E501
        """Ping available ldap service.  # noqa: E501

        This endpoint ping the available ldap service for test related configuration parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ping_ldap_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :param LdapConf ldapconf: ldap configuration. support input ldap service configuration. If it is a empty request, will load current configuration from the system.
        :return: LdapPingResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["x_request_id", "ldapconf"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method ping_ldap" % key
                )
            params[key] = val
        del params["kwargs"]

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `ping_ldap`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if "ldapconf" in params:
            body_params = params["ldapconf"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basic"]  # noqa: E501

        return self.api_client.call_api(
            "/ldap/ping",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="LdapPingResult",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def search_ldap_group(self, **kwargs):  # noqa: E501
        """Search available ldap groups.  # noqa: E501

        This endpoint searches the available ldap groups based on related configuration parameters. support to search by groupname or groupdn.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_ldap_group(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :param str groupname: Ldap group name
        :param str groupdn: The LDAP group DN
        :return: list[UserGroup]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.search_ldap_group_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_ldap_group_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_ldap_group_with_http_info(self, **kwargs):  # noqa: E501
        """Search available ldap groups.  # noqa: E501

        This endpoint searches the available ldap groups based on related configuration parameters. support to search by groupname or groupdn.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_ldap_group_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :param str groupname: Ldap group name
        :param str groupdn: The LDAP group DN
        :return: list[UserGroup]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["x_request_id", "groupname", "groupdn"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method search_ldap_group" % key
                )
            params[key] = val
        del params["kwargs"]

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `search_ldap_group`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if "groupname" in params:
            query_params.append(("groupname", params["groupname"]))  # noqa: E501
        if "groupdn" in params:
            query_params.append(("groupdn", params["groupdn"]))  # noqa: E501

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basic"]  # noqa: E501

        return self.api_client.call_api(
            "/ldap/groups/search",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[UserGroup]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def search_ldap_user(self, **kwargs):  # noqa: E501
        """Search available ldap users.  # noqa: E501

        This endpoint searches the available ldap users based on related configuration parameters. Support searched by input ladp configuration, load configuration from the system and specific filter.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_ldap_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :param str username: Registered user ID
        :return: list[LdapUser]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.search_ldap_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_ldap_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_ldap_user_with_http_info(self, **kwargs):  # noqa: E501
        """Search available ldap users.  # noqa: E501

        This endpoint searches the available ldap users based on related configuration parameters. Support searched by input ladp configuration, load configuration from the system and specific filter.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_ldap_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :param str username: Registered user ID
        :return: list[LdapUser]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["x_request_id", "username"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method search_ldap_user" % key
                )
            params[key] = val
        del params["kwargs"]

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `search_ldap_user`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if "username" in params:
            query_params.append(("username", params["username"]))  # noqa: E501

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basic"]  # noqa: E501

        return self.api_client.call_api(
            "/ldap/users/search",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[LdapUser]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
