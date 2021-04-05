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
from harbor_client.model.label import Label


class LabelApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __chartrepo_repo_charts_name_version_labels_get(
            self,
            repo,
            name,
            version,
            **kwargs
        ):
            """Return the attahced labels of chart.  # noqa: E501

            Return the attahced labels of the specified chart version.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.chartrepo_repo_charts_name_version_labels_get(repo, name, version, async_req=True)
            >>> result = thread.get()

            Args:
                repo (str): The project name
                name (str): The chart name
                version (str): The chart version

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
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
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['repo'] = \
                repo
            kwargs['name'] = \
                name
            kwargs['version'] = \
                version
            return self.call_with_http_info(**kwargs)

        self.chartrepo_repo_charts_name_version_labels_get = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/chartrepo/{repo}/charts/{name}/{version}/labels',
                'operation_id': 'chartrepo_repo_charts_name_version_labels_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'repo',
                    'name',
                    'version',
                ],
                'required': [
                    'repo',
                    'name',
                    'version',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repo':
                        (str,),
                    'name':
                        (str,),
                    'version':
                        (str,),
                },
                'attribute_map': {
                    'repo': 'repo',
                    'name': 'name',
                    'version': 'version',
                },
                'location_map': {
                    'repo': 'path',
                    'name': 'path',
                    'version': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__chartrepo_repo_charts_name_version_labels_get
        )

        def __chartrepo_repo_charts_name_version_labels_id_delete(
            self,
            repo,
            name,
            version,
            id,
            **kwargs
        ):
            """Remove label from chart.  # noqa: E501

            Remove label from the specified chart version.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.chartrepo_repo_charts_name_version_labels_id_delete(repo, name, version, id, async_req=True)
            >>> result = thread.get()

            Args:
                repo (str): The project name
                name (str): The chart name
                version (str): The chart version
                id (int): The label ID

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
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
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['repo'] = \
                repo
            kwargs['name'] = \
                name
            kwargs['version'] = \
                version
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.chartrepo_repo_charts_name_version_labels_id_delete = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/chartrepo/{repo}/charts/{name}/{version}/labels/{id}',
                'operation_id': 'chartrepo_repo_charts_name_version_labels_id_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'repo',
                    'name',
                    'version',
                    'id',
                ],
                'required': [
                    'repo',
                    'name',
                    'version',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repo':
                        (str,),
                    'name':
                        (str,),
                    'version':
                        (str,),
                    'id':
                        (int,),
                },
                'attribute_map': {
                    'repo': 'repo',
                    'name': 'name',
                    'version': 'version',
                    'id': 'id',
                },
                'location_map': {
                    'repo': 'path',
                    'name': 'path',
                    'version': 'path',
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__chartrepo_repo_charts_name_version_labels_id_delete
        )

        def __chartrepo_repo_charts_name_version_labels_post(
            self,
            repo,
            name,
            version,
            label,
            **kwargs
        ):
            """Mark label to chart.  # noqa: E501

            Mark label to the specified chart version.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.chartrepo_repo_charts_name_version_labels_post(repo, name, version, label, async_req=True)
            >>> result = thread.get()

            Args:
                repo (str): The project name
                name (str): The chart name
                version (str): The chart version
                label (Label): The label being marked to the chart version

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
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
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['repo'] = \
                repo
            kwargs['name'] = \
                name
            kwargs['version'] = \
                version
            kwargs['label'] = \
                label
            return self.call_with_http_info(**kwargs)

        self.chartrepo_repo_charts_name_version_labels_post = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/chartrepo/{repo}/charts/{name}/{version}/labels',
                'operation_id': 'chartrepo_repo_charts_name_version_labels_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'repo',
                    'name',
                    'version',
                    'label',
                ],
                'required': [
                    'repo',
                    'name',
                    'version',
                    'label',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repo':
                        (str,),
                    'name':
                        (str,),
                    'version':
                        (str,),
                    'label':
                        (Label,),
                },
                'attribute_map': {
                    'repo': 'repo',
                    'name': 'name',
                    'version': 'version',
                },
                'location_map': {
                    'repo': 'path',
                    'name': 'path',
                    'version': 'path',
                    'label': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__chartrepo_repo_charts_name_version_labels_post
        )