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


class ConfigureApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_configurations(self, **kwargs):    # noqa: E501
        """Get system configurations.  # noqa: E501

        This endpoint is for retrieving system configurations that only provides for admin user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_configurations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: ConfigurationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_configurations_with_http_info(**kwargs)  # noqa: E501

    def get_configurations_with_http_info(self, **kwargs):    # noqa: E501
        """Get system configurations.  # noqa: E501

        This endpoint is for retrieving system configurations that only provides for admin user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_configurations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: ConfigurationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        all_params = [
            'x_request_id',
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout',
        ]
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_configurations"
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('x_request_id' in params and
                                                       len(params['x_request_id']) < 1):
            raise ValueError("Invalid value for parameter `x_request_id` when calling `get_configurations`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/configurations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigurationsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_internalconfig(self, **kwargs):    # noqa: E501
        """Get internal configurations.  # noqa: E501

        This endpoint is for retrieving system configurations that only provides for internal api call.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_internalconfig(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: InternalConfigurationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_internalconfig_with_http_info(**kwargs)  # noqa: E501

    def get_internalconfig_with_http_info(self, **kwargs):    # noqa: E501
        """Get internal configurations.  # noqa: E501

        This endpoint is for retrieving system configurations that only provides for internal api call.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_internalconfig_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :return: InternalConfigurationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        all_params = [
            'x_request_id',
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout',
        ]
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method get_internalconfig"
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('x_request_id' in params and
                                                       len(params['x_request_id']) < 1):
            raise ValueError("Invalid value for parameter `x_request_id` when calling `get_internalconfig`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/internalconfig', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InternalConfigurationsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_configurations(self, configurations, **kwargs):    # noqa: E501
        """Modify system configurations.  # noqa: E501

        This endpoint is for modifying system configurations that only provides for admin user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_configurations(configurations, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Configurations configurations: The configuration map can contain a subset of the attributes of the schema, which are to be updated. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_configurations_with_http_info(configurations, **kwargs)  # noqa: E501

    def update_configurations_with_http_info(self, configurations, **kwargs):    # noqa: E501
        """Modify system configurations.  # noqa: E501

        This endpoint is for modifying system configurations that only provides for admin user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_configurations_with_http_info(configurations, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Configurations configurations: The configuration map can contain a subset of the attributes of the schema, which are to be updated. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            'configurations',
            'x_request_id',
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout',
        ]
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    f"Got an unexpected keyword argument '{key}' to method update_configurations"
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'configurations' is set
        if self.api_client.client_side_validation and ('configurations' not in params or
                                                       params['configurations'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `configurations` when calling `update_configurations`")  # noqa: E501

        if self.api_client.client_side_validation and ('x_request_id' in params and
                                                       len(params['x_request_id']) < 1):
            raise ValueError("Invalid value for parameter `x_request_id` when calling `update_configurations`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = params.get('configurations')
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/configurations', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
