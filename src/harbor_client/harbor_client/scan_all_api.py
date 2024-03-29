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


class ScanAllApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_scan_all_schedule(self, schedule, **kwargs):  # noqa: E501
        """Create a schedule or a manual trigger for the scan all job.  # noqa: E501

        This endpoint is for creating a schedule or a manual trigger for the scan all job, which scans all of images in Harbor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_scan_all_schedule(schedule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule schedule: Create a schedule or a manual trigger for the scan all job. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_scan_all_schedule_with_http_info(schedule, **kwargs)  # noqa: E501
        else:
            (data) = self.create_scan_all_schedule_with_http_info(schedule, **kwargs)  # noqa: E501
            return data

    def create_scan_all_schedule_with_http_info(self, schedule, **kwargs):  # noqa: E501
        """Create a schedule or a manual trigger for the scan all job.  # noqa: E501

        This endpoint is for creating a schedule or a manual trigger for the scan all job, which scans all of images in Harbor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_scan_all_schedule_with_http_info(schedule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule schedule: Create a schedule or a manual trigger for the scan all job. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["schedule", "x_request_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_scan_all_schedule" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'schedule' is set
        if self.api_client.client_side_validation and (
            "schedule" not in params or params["schedule"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `schedule` when calling `create_scan_all_schedule`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `create_scan_all_schedule`, length must be greater than or equal to `1`"
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
        if "schedule" in params:
            body_params = params["schedule"]
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
            "/system/scanAll/schedule",
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

    def get_latest_scan_all_metrics(self, **kwargs):  # noqa: E501
        """Get the metrics of the latest scan all process  # noqa: E501

        Get the metrics of the latest scan all process  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_scan_all_metrics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: Stats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_latest_scan_all_metrics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_latest_scan_all_metrics_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_latest_scan_all_metrics_with_http_info(self, **kwargs):  # noqa: E501
        """Get the metrics of the latest scan all process  # noqa: E501

        Get the metrics of the latest scan all process  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_scan_all_metrics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: Stats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["x_request_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_latest_scan_all_metrics" % key
                )
            params[key] = val
        del params["kwargs"]

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `get_latest_scan_all_metrics`, length must be greater than or equal to `1`"
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
            "/scans/all/metrics",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Stats",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_latest_scheduled_scan_all_metrics(self, **kwargs):  # noqa: E501
        """Get the metrics of the latest scheduled scan all process  # noqa: E501

        Get the metrics of the latest scheduled scan all process  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_scheduled_scan_all_metrics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: Stats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_latest_scheduled_scan_all_metrics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_latest_scheduled_scan_all_metrics_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def get_latest_scheduled_scan_all_metrics_with_http_info(self, **kwargs):  # noqa: E501
        """Get the metrics of the latest scheduled scan all process  # noqa: E501

        Get the metrics of the latest scheduled scan all process  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_scheduled_scan_all_metrics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: Stats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["x_request_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_latest_scheduled_scan_all_metrics" % key
                )
            params[key] = val
        del params["kwargs"]

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `get_latest_scheduled_scan_all_metrics`, length must be greater than or equal to `1`"
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
            "/scans/schedule/metrics",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Stats",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_scan_all_schedule(self, **kwargs):  # noqa: E501
        """Get scan all's schedule.  # noqa: E501

        This endpoint is for getting a schedule for the scan all job, which scans all of images in Harbor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scan_all_schedule(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_scan_all_schedule_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_scan_all_schedule_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_scan_all_schedule_with_http_info(self, **kwargs):  # noqa: E501
        """Get scan all's schedule.  # noqa: E501

        This endpoint is for getting a schedule for the scan all job, which scans all of images in Harbor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scan_all_schedule_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["x_request_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scan_all_schedule" % key
                )
            params[key] = val
        del params["kwargs"]

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `get_scan_all_schedule`, length must be greater than or equal to `1`"
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
            "/system/scanAll/schedule",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Schedule",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def stop_scan_all(self, **kwargs):  # noqa: E501
        """Stop scanAll job execution  # noqa: E501

        Stop scanAll job execution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stop_scan_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.stop_scan_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stop_scan_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def stop_scan_all_with_http_info(self, **kwargs):  # noqa: E501
        """Stop scanAll job execution  # noqa: E501

        Stop scanAll job execution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stop_scan_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["x_request_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method stop_scan_all" % key
                )
            params[key] = val
        del params["kwargs"]

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `stop_scan_all`, length must be greater than or equal to `1`"
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
            "/system/scanAll/stop",
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

    def update_scan_all_schedule(self, schedule, **kwargs):  # noqa: E501
        """Update scan all's schedule.  # noqa: E501

        This endpoint is for updating the schedule of scan all job, which scans all of images in Harbor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_scan_all_schedule(schedule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule schedule: Updates the schedule of scan all job, which scans all of images in Harbor. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_scan_all_schedule_with_http_info(schedule, **kwargs)  # noqa: E501
        else:
            (data) = self.update_scan_all_schedule_with_http_info(schedule, **kwargs)  # noqa: E501
            return data

    def update_scan_all_schedule_with_http_info(self, schedule, **kwargs):  # noqa: E501
        """Update scan all's schedule.  # noqa: E501

        This endpoint is for updating the schedule of scan all job, which scans all of images in Harbor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_scan_all_schedule_with_http_info(schedule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule schedule: Updates the schedule of scan all job, which scans all of images in Harbor. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["schedule", "x_request_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_scan_all_schedule" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'schedule' is set
        if self.api_client.client_side_validation and (
            "schedule" not in params or params["schedule"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `schedule` when calling `update_scan_all_schedule`"
            )  # noqa: E501

        if self.api_client.client_side_validation and (
            "x_request_id" in params and len(params["x_request_id"]) < 1
        ):
            raise ValueError(
                "Invalid value for parameter `x_request_id` when calling `update_scan_all_schedule`, length must be greater than or equal to `1`"
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
        if "schedule" in params:
            body_params = params["schedule"]
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
            "/system/scanAll/schedule",
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
