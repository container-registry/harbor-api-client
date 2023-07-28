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


class ProjectMetadataApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_project_metadatas(self, project_name_or_id, **kwargs):  # noqa: E501
        """Add metadata for the specific project  # noqa: E501

        Add metadata for the specific project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_project_metadatas(project_name_or_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :param object metadata:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.add_project_metadatas_with_http_info(
                project_name_or_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.add_project_metadatas_with_http_info(
                project_name_or_id, **kwargs
            )  # noqa: E501
            return data

    def add_project_metadatas_with_http_info(self, project_name_or_id, **kwargs):  # noqa: E501
        """Add metadata for the specific project  # noqa: E501

        Add metadata for the specific project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_project_metadatas_with_http_info(project_name_or_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :param object metadata:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "project_name_or_id",
            "x_request_id",
            "x_is_resource_name",
            "metadata",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_project_metadatas" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and (
            "project_name_or_id" not in params or params["project_name_or_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `project_name_or_id` when calling `add_project_metadatas`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `add_project_metadatas`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "project_name_or_id" in params:
            path_params["project_name_or_id"] = params["project_name_or_id"]  # noqa: E501

        query_params = []

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501
        if "x_is_resource_name" in params:
            header_params["X-Is-Resource-Name"] = params["x_is_resource_name"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if "metadata" in params:
            body_params = params["metadata"]
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
            "/projects/{project_name_or_id}/metadatas/",
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

    def delete_project_metadata(self, project_name_or_id, meta_name, **kwargs):  # noqa: E501
        """Delete the specific metadata for the specific project  # noqa: E501

        Delete the specific metadata for the specific project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project_metadata(project_name_or_id, meta_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str meta_name: The name of metadata. (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_project_metadata_with_http_info(
                project_name_or_id, meta_name, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_project_metadata_with_http_info(
                project_name_or_id, meta_name, **kwargs
            )  # noqa: E501
            return data

    def delete_project_metadata_with_http_info(
        self, project_name_or_id, meta_name, **kwargs
    ):  # noqa: E501
        """Delete the specific metadata for the specific project  # noqa: E501

        Delete the specific metadata for the specific project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project_metadata_with_http_info(project_name_or_id, meta_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str meta_name: The name of metadata. (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "project_name_or_id",
            "meta_name",
            "x_request_id",
            "x_is_resource_name",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_project_metadata" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and (
            "project_name_or_id" not in params or params["project_name_or_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `project_name_or_id` when calling `delete_project_metadata`"
            )  # noqa: E501
        # verify the required parameter 'meta_name' is set
        if self.api_client.client_side_validation and (
            "meta_name" not in params or params["meta_name"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `meta_name` when calling `delete_project_metadata`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `delete_project_metadata`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "project_name_or_id" in params:
            path_params["project_name_or_id"] = params["project_name_or_id"]  # noqa: E501
        if "meta_name" in params:
            path_params["meta_name"] = params["meta_name"]  # noqa: E501

        query_params = []

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501
        if "x_is_resource_name" in params:
            header_params["X-Is-Resource-Name"] = params["x_is_resource_name"]  # noqa: E501

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
            "/projects/{project_name_or_id}/metadatas/{meta_name}",
            "DELETE",
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

    def get_project_metadata(self, project_name_or_id, meta_name, **kwargs):  # noqa: E501
        """Get the specific metadata of the specific project  # noqa: E501

        Get the specific metadata of the specific project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_metadata(project_name_or_id, meta_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str meta_name: The name of metadata. (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: dict(str, str)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_project_metadata_with_http_info(
                project_name_or_id, meta_name, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_project_metadata_with_http_info(
                project_name_or_id, meta_name, **kwargs
            )  # noqa: E501
            return data

    def get_project_metadata_with_http_info(
        self, project_name_or_id, meta_name, **kwargs
    ):  # noqa: E501
        """Get the specific metadata of the specific project  # noqa: E501

        Get the specific metadata of the specific project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_metadata_with_http_info(project_name_or_id, meta_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str meta_name: The name of metadata. (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: dict(str, str)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "project_name_or_id",
            "meta_name",
            "x_request_id",
            "x_is_resource_name",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_metadata" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and (
            "project_name_or_id" not in params or params["project_name_or_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `project_name_or_id` when calling `get_project_metadata`"
            )  # noqa: E501
        # verify the required parameter 'meta_name' is set
        if self.api_client.client_side_validation and (
            "meta_name" not in params or params["meta_name"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `meta_name` when calling `get_project_metadata`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `get_project_metadata`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "project_name_or_id" in params:
            path_params["project_name_or_id"] = params["project_name_or_id"]  # noqa: E501
        if "meta_name" in params:
            path_params["meta_name"] = params["meta_name"]  # noqa: E501

        query_params = []

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501
        if "x_is_resource_name" in params:
            header_params["X-Is-Resource-Name"] = params["x_is_resource_name"]  # noqa: E501

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
            "/projects/{project_name_or_id}/metadatas/{meta_name}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="dict(str, str)",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_project_metadatas(self, project_name_or_id, **kwargs):  # noqa: E501
        """Get the metadata of the specific project  # noqa: E501

        Get the metadata of the specific project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_project_metadatas(project_name_or_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: dict(str, str)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_project_metadatas_with_http_info(
                project_name_or_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.list_project_metadatas_with_http_info(
                project_name_or_id, **kwargs
            )  # noqa: E501
            return data

    def list_project_metadatas_with_http_info(self, project_name_or_id, **kwargs):  # noqa: E501
        """Get the metadata of the specific project  # noqa: E501

        Get the metadata of the specific project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_project_metadatas_with_http_info(project_name_or_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :return: dict(str, str)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["project_name_or_id", "x_request_id", "x_is_resource_name"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_project_metadatas" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and (
            "project_name_or_id" not in params or params["project_name_or_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `project_name_or_id` when calling `list_project_metadatas`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `list_project_metadatas`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "project_name_or_id" in params:
            path_params["project_name_or_id"] = params["project_name_or_id"]  # noqa: E501

        query_params = []

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501
        if "x_is_resource_name" in params:
            header_params["X-Is-Resource-Name"] = params["x_is_resource_name"]  # noqa: E501

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
            "/projects/{project_name_or_id}/metadatas/",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="dict(str, str)",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_project_metadata(self, project_name_or_id, meta_name, **kwargs):  # noqa: E501
        """Update the specific metadata for the specific project  # noqa: E501

        Update the specific metadata for the specific project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project_metadata(project_name_or_id, meta_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str meta_name: The name of metadata. (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :param object metadata:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_project_metadata_with_http_info(
                project_name_or_id, meta_name, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_project_metadata_with_http_info(
                project_name_or_id, meta_name, **kwargs
            )  # noqa: E501
            return data

    def update_project_metadata_with_http_info(
        self, project_name_or_id, meta_name, **kwargs
    ):  # noqa: E501
        """Update the specific metadata for the specific project  # noqa: E501

        Update the specific metadata for the specific project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project_metadata_with_http_info(project_name_or_id, meta_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name_or_id: The name or id of the project (required)
        :param str meta_name: The name of metadata. (required)
        :param str x_request_id: An unique ID for the request
        :param bool x_is_resource_name: The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.
        :param object metadata:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "project_name_or_id",
            "meta_name",
            "x_request_id",
            "x_is_resource_name",
            "metadata",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_project_metadata" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'project_name_or_id' is set
        if self.api_client.client_side_validation and (
            "project_name_or_id" not in params or params["project_name_or_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `project_name_or_id` when calling `update_project_metadata`"
            )  # noqa: E501
        # verify the required parameter 'meta_name' is set
        if self.api_client.client_side_validation and (
            "meta_name" not in params or params["meta_name"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `meta_name` when calling `update_project_metadata`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `update_project_metadata`, length must be greater than or equal to `1`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "project_name_or_id" in params:
            path_params["project_name_or_id"] = params["project_name_or_id"]  # noqa: E501
        if "meta_name" in params:
            path_params["meta_name"] = params["meta_name"]  # noqa: E501

        query_params = []

        header_params = {}
        if "x_request_id" in params:
            header_params["X-Request-Id"] = params["x_request_id"]  # noqa: E501
        if "x_is_resource_name" in params:
            header_params["X-Is-Resource-Name"] = params["x_is_resource_name"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if "metadata" in params:
            body_params = params["metadata"]
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
            "/projects/{project_name_or_id}/metadatas/{meta_name}",
            "PUT",
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
