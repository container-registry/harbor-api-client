# harbor_client.RetentionApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_retention**](RetentionApi.md#create_retention) | **POST** /retentions | Create Retention Policy
[**get_rentenition_metadata**](RetentionApi.md#get_rentenition_metadata) | **GET** /retentions/metadatas | Get Retention Metadatas
[**get_retention**](RetentionApi.md#get_retention) | **GET** /retentions/{id} | Get Retention Policy
[**get_retention_task_log**](RetentionApi.md#get_retention_task_log) | **GET** /retentions/{id}/executions/{eid}/tasks/{tid} | Get Retention job task log
[**list_retention_executions**](RetentionApi.md#list_retention_executions) | **GET** /retentions/{id}/executions | Get Retention executions
[**list_retention_tasks**](RetentionApi.md#list_retention_tasks) | **GET** /retentions/{id}/executions/{eid}/tasks | Get Retention tasks
[**operate_retention_execution**](RetentionApi.md#operate_retention_execution) | **PATCH** /retentions/{id}/executions/{eid} | Stop a Retention execution
[**trigger_retention_execution**](RetentionApi.md#trigger_retention_execution) | **POST** /retentions/{id}/executions | Trigger a Retention Execution
[**update_retention**](RetentionApi.md#update_retention) | **PUT** /retentions/{id} | Update Retention Policy


# **create_retention**
> create_retention(retention_policy)

Create Retention Policy

Create Retention Policy, you can reference metadatas API for the policy model. You can check project metadatas to find whether a retention policy is already binded. This method should only be called when no retention policy binded to project yet.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import retention_api
from harbor_client.model.retention_policy import RetentionPolicy
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = retention_api.RetentionApi(api_client)
    retention_policy = RetentionPolicy(
        id=1,
        algorithm="algorithm_example",
        rules=[
            RetentionRule(
                id=1,
                priority=1,
                disabled=True,
                action="action_example",
                template="template_example",
                params={
                    "key": {},
                },
                tag_selectors=[
                    RetentionSelector(
                        kind="kind_example",
                        decoration="decoration_example",
                        pattern="pattern_example",
                        extras="extras_example",
                    ),
                ],
                scope_selectors={
                    "key": [
                        RetentionSelector(
                            kind="kind_example",
                            decoration="decoration_example",
                            pattern="pattern_example",
                            extras="extras_example",
                        ),
                    ],
                },
            ),
        ],
        trigger=RetentionRuleTrigger(
            kind="kind_example",
            settings={},
            references={},
        ),
        scope=RetentionPolicyScope(
            level="level_example",
            ref=1,
        ),
    ) # RetentionPolicy | Create Retention Policy successfully.

    # example passing only required values which don't have defaults set
    try:
        # Create Retention Policy
        api_instance.create_retention(retention_policy)
    except harbor_client.ApiException as e:
        print("Exception when calling RetentionApi->create_retention: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retention_policy** | [**RetentionPolicy**](RetentionPolicy.md)| Create Retention Policy successfully. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-Request-Id - The ID of the corresponding request for the response <br>  * Location - The URL of the created resource <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rentenition_metadata**
> RetentionMetadata get_rentenition_metadata()

Get Retention Metadatas

Get Retention Metadatas.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import retention_api
from harbor_client.model.retention_metadata import RetentionMetadata
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = retention_api.RetentionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Retention Metadatas
        api_response = api_instance.get_rentenition_metadata()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling RetentionApi->get_rentenition_metadata: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RetentionMetadata**](RetentionMetadata.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Retention Metadatas successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_retention**
> RetentionPolicy get_retention(id)

Get Retention Policy

Get Retention Policy.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import retention_api
from harbor_client.model.retention_policy import RetentionPolicy
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = retention_api.RetentionApi(api_client)
    id = 1 # int | Retention ID.

    # example passing only required values which don't have defaults set
    try:
        # Get Retention Policy
        api_response = api_instance.get_retention(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling RetentionApi->get_retention: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. |

### Return type

[**RetentionPolicy**](RetentionPolicy.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Retention Policy successfully. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_retention_task_log**
> str get_retention_task_log(id, eid, tid)

Get Retention job task log

Get Retention job task log, tags ratain or deletion detail will be shown in a table.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import retention_api
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = retention_api.RetentionApi(api_client)
    id = 1 # int | Retention ID.
    eid = 1 # int | Retention execution ID.
    tid = 1 # int | Retention execution ID.

    # example passing only required values which don't have defaults set
    try:
        # Get Retention job task log
        api_response = api_instance.get_retention_task_log(id, eid, tid)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling RetentionApi->get_retention_task_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. |
 **eid** | **int**| Retention execution ID. |
 **tid** | **int**| Retention execution ID. |

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Retention job task log successfully. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_retention_executions**
> [RetentionExecution] list_retention_executions(id)

Get Retention executions

Get Retention executions, execution status may be delayed before job service schedule it up.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import retention_api
from harbor_client.model.retention_execution import RetentionExecution
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = retention_api.RetentionApi(api_client)
    id = 1 # int | Retention ID.
    page = 1 # int | The page number. (optional)
    page_size = 1 # int | The size of per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Retention executions
        api_response = api_instance.list_retention_executions(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling RetentionApi->list_retention_executions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Retention executions
        api_response = api_instance.list_retention_executions(id, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling RetentionApi->list_retention_executions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. |
 **page** | **int**| The page number. | [optional]
 **page_size** | **int**| The size of per page. | [optional]

### Return type

[**[RetentionExecution]**](RetentionExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a Retention execution successfully. |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_retention_tasks**
> [RetentionExecutionTask] list_retention_tasks(id, eid)

Get Retention tasks

Get Retention tasks, each repository as a task.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import retention_api
from harbor_client.model.retention_execution_task import RetentionExecutionTask
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = retention_api.RetentionApi(api_client)
    id = 1 # int | Retention ID.
    eid = 1 # int | Retention execution ID.
    page = 1 # int | The page number. (optional)
    page_size = 1 # int | The size of per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Retention tasks
        api_response = api_instance.list_retention_tasks(id, eid)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling RetentionApi->list_retention_tasks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Retention tasks
        api_response = api_instance.list_retention_tasks(id, eid, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling RetentionApi->list_retention_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. |
 **eid** | **int**| Retention execution ID. |
 **page** | **int**| The page number. | [optional]
 **page_size** | **int**| The size of per page. | [optional]

### Return type

[**[RetentionExecutionTask]**](RetentionExecutionTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Retention job tasks successfully. |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operate_retention_execution**
> operate_retention_execution(id, eid, inline_object2)

Stop a Retention execution

Stop a Retention execution, only support \"stop\" action now.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import retention_api
from harbor_client.model.errors import Errors
from harbor_client.model.inline_object2 import InlineObject2
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = retention_api.RetentionApi(api_client)
    id = 1 # int | Retention ID.
    eid = 1 # int | Retention execution ID.
    inline_object2 = InlineObject2(
        action="action_example",
    ) # InlineObject2 | 

    # example passing only required values which don't have defaults set
    try:
        # Stop a Retention execution
        api_instance.operate_retention_execution(id, eid, inline_object2)
    except harbor_client.ApiException as e:
        print("Exception when calling RetentionApi->operate_retention_execution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. |
 **eid** | **int**| Retention execution ID. |
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stop a Retention job successfully. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_retention_execution**
> trigger_retention_execution(id, inline_object1)

Trigger a Retention Execution

Trigger a Retention Execution, if dry_run is True, nothing would be deleted actually.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import retention_api
from harbor_client.model.inline_object1 import InlineObject1
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = retention_api.RetentionApi(api_client)
    id = 1 # int | Retention ID.
    inline_object1 = InlineObject1(
        dry_run=True,
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Trigger a Retention Execution
        api_instance.trigger_retention_execution(id, inline_object1)
    except harbor_client.ApiException as e:
        print("Exception when calling RetentionApi->trigger_retention_execution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. |
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Trigger a Retention job successfully. |  -  |
**201** | Created |  * X-Request-Id - The ID of the corresponding request for the response <br>  * Location - The URL of the created resource <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_retention**
> update_retention(id, retention_policy)

Update Retention Policy

Update Retention Policy, you can reference metadatas API for the policy model. You can check project metadatas to find whether a retention policy is already binded. This method should only be called when retention policy has already binded to project.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import retention_api
from harbor_client.model.retention_policy import RetentionPolicy
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = retention_api.RetentionApi(api_client)
    id = 1 # int | Retention ID.
    retention_policy = RetentionPolicy(
        id=1,
        algorithm="algorithm_example",
        rules=[
            RetentionRule(
                id=1,
                priority=1,
                disabled=True,
                action="action_example",
                template="template_example",
                params={
                    "key": {},
                },
                tag_selectors=[
                    RetentionSelector(
                        kind="kind_example",
                        decoration="decoration_example",
                        pattern="pattern_example",
                        extras="extras_example",
                    ),
                ],
                scope_selectors={
                    "key": [
                        RetentionSelector(
                            kind="kind_example",
                            decoration="decoration_example",
                            pattern="pattern_example",
                            extras="extras_example",
                        ),
                    ],
                },
            ),
        ],
        trigger=RetentionRuleTrigger(
            kind="kind_example",
            settings={},
            references={},
        ),
        scope=RetentionPolicyScope(
            level="level_example",
            ref=1,
        ),
    ) # RetentionPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update Retention Policy
        api_instance.update_retention(id, retention_policy)
    except harbor_client.ApiException as e:
        print("Exception when calling RetentionApi->update_retention: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. |
 **retention_policy** | [**RetentionPolicy**](RetentionPolicy.md)|  |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Retention Policy successfully. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

