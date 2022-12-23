"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from harbor_client.api_client import ApiClient, Endpoint as _Endpoint
from harbor_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from harbor_client.model.errors import Errors
from harbor_client.model.quota import Quota
from harbor_client.model.quota_update_req import QuotaUpdateReq


class QuotaApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_quota(
                self,
                id,
                **kwargs
            ):
            """Get the specified quota  # noqa: E501

            Get the specified quota  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_quota(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Quota ID

            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Quota
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get('_request_timeout')
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                    id
            return self.call_with_http_info(**kwargs)

        self.get_quota = _Endpoint(
            settings={
                'response_type': (Quota,),
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/quotas/{id}',
                'operation_id': 'get_quota',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'x_request_id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'x_request_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'x_request_id': 'X-Request-Id',
                },
                'location_map': {
                    'id': 'path',
                    'x_request_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_quota
        )

        def __list_quotas(
                self,
                **kwargs
            ):
            """List quotas  # noqa: E501

            List quotas  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_quotas(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
                page (int): The page number. [optional] if omitted the server will use the default value of 1
                page_size (int): The size of per page. [optional] if omitted the server will use the default value of 10
                reference (str): The reference type of quota.. [optional]
                reference_id (str): The reference id of quota.. [optional]
                sort (str): Sort method, valid values include: 'hard.resource_name', '-hard.resource_name', 'used.resource_name', '-used.resource_name'. Here '-' stands for descending order, resource_name should be the real resource name of the quota. . [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [Quota]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get('_request_timeout')
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_quotas = _Endpoint(
            settings={
                'response_type': ([Quota],),
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/quotas',
                'operation_id': 'list_quotas',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'page',
                    'page_size',
                    'reference',
                    'reference_id',
                    'sort',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'min_length': 1,
                    },
                    ('page_size',): {

                        'inclusive_maximum': 100,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                    'reference':
                        (str,),
                    'reference_id':
                        (str,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'x_request_id': 'X-Request-Id',
                    'page': 'page',
                    'page_size': 'page_size',
                    'reference': 'reference',
                    'reference_id': 'reference_id',
                    'sort': 'sort',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'page': 'query',
                    'page_size': 'query',
                    'reference': 'query',
                    'reference_id': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_quotas
        )

        def __update_quota(
                self,
                id,
                quota_update_req,
                **kwargs
            ):
            """Update the specified quota  # noqa: E501

            Update hard limits of the specified quota  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_quota(id, quota_update_req, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Quota ID
                quota_update_req (QuotaUpdateReq): The new hard limits for the quota

            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get('_request_timeout')
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                    id
            kwargs['quota_update_req'] = \
                    quota_update_req
            return self.call_with_http_info(**kwargs)

        self.update_quota = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/quotas/{id}',
                'operation_id': 'update_quota',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'quota_update_req',
                    'x_request_id',
                ],
                'required': [
                    'id',
                    'quota_update_req',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'quota_update_req':
                        (QuotaUpdateReq,),
                    'x_request_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'x_request_id': 'X-Request-Id',
                },
                'location_map': {
                    'id': 'path',
                    'quota_update_req': 'body',
                    'x_request_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_quota
        )
