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


class OidcApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ping_oidc(self, endpoint, **kwargs):  # noqa: E501
        """Test the OIDC endpoint.  # noqa: E501

        Test the OIDC endpoint, the setting of the endpoint is provided in the request.  This API can only be called by system admin.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ping_oidc(endpoint, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Endpoint endpoint: Request body for OIDC endpoint to be tested. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ping_oidc_with_http_info(endpoint, **kwargs)  # noqa: E501
        else:
            (data) = self.ping_oidc_with_http_info(endpoint, **kwargs)  # noqa: E501
            return data

    def ping_oidc_with_http_info(self, endpoint, **kwargs):  # noqa: E501
        """Test the OIDC endpoint.  # noqa: E501

        Test the OIDC endpoint, the setting of the endpoint is provided in the request.  This API can only be called by system admin.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ping_oidc_with_http_info(endpoint, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Endpoint endpoint: Request body for OIDC endpoint to be tested. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint', 'x_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ping_oidc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint' is set
        if self.api_client.client_side_validation and ('endpoint' not in params or
                                                       params['endpoint'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `endpoint` when calling `ping_oidc`")  # noqa: E501

        if self.api_client.client_side_validation and ('x_request_id' in params and
                                                       len(params['x_request_id']) < 1):
            raise ValueError("Invalid value for parameter `x_request_id` when calling `ping_oidc`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'endpoint' in params:
            body_params = params['endpoint']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/system/oidc/ping', 'POST',
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