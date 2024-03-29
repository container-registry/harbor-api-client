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


class AuditlogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_audit_logs(self, **kwargs):  # noqa: E501
        """Get recent logs of the projects which the user is a member of  # noqa: E501

        This endpoint let user see the recent operation logs of the projects which he is member of   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_audit_logs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param str sort: Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\"
        :param int page: The page number
        :param int page_size: The size of per page
        :return: list[AuditLog]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_audit_logs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_audit_logs_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_audit_logs_with_http_info(self, **kwargs):  # noqa: E501
        """Get recent logs of the projects which the user is a member of  # noqa: E501

        This endpoint let user see the recent operation logs of the projects which he is member of   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_audit_logs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param str sort: Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\"
        :param int page: The page number
        :param int page_size: The size of per page
        :return: list[AuditLog]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["x_request_id", "q", "sort", "page", "page_size"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method list_audit_logs" % key
                )
            params[key] = val
        del params["kwargs"]

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `list_audit_logs`, length must be greater than or equal to `1`"
            )  # noqa: E501
        if self.api_client.client_side_validation and (
            "page_size" in params and params["page_size"] > 100
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for parameter `page_size` when calling `list_audit_logs`, must be a value less than or equal to `100`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if "q" in params:
            query_params.append(("q", params["q"]))  # noqa: E501
        if "sort" in params:
            query_params.append(("sort", params["sort"]))  # noqa: E501
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "page_size" in params:
            query_params.append(("page_size", params["page_size"]))  # noqa: E501

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
            "/audit-logs",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[AuditLog]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
