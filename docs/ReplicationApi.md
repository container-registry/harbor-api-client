# harbor_client.ReplicationApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_replication_execution**](ReplicationApi.md#get_replication_execution) | **GET** /replication/executions/{id} | Get the specific replication execution
[**get_replication_log**](ReplicationApi.md#get_replication_log) | **GET** /replication/executions/{id}/tasks/{task_id}/log | Get the log of the specific replication task
[**list_replication_executions**](ReplicationApi.md#list_replication_executions) | **GET** /replication/executions | List replication executions
[**list_replication_tasks**](ReplicationApi.md#list_replication_tasks) | **GET** /replication/executions/{id}/tasks | List replication tasks for a specific execution
[**start_replication**](ReplicationApi.md#start_replication) | **POST** /replication/executions | Start one replication execution
[**stop_replication**](ReplicationApi.md#stop_replication) | **PUT** /replication/executions/{id} | Stop the specific replication execution


# **get_replication_execution**
> ReplicationExecution get_replication_execution(id)

Get the specific replication execution

Get the replication execution specified by ID

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import replication_api
from harbor_client.model.replication_execution import ReplicationExecution
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
    api_instance = replication_api.ReplicationApi(api_client)
    id = 1 # int | The ID of the execution.

    # example passing only required values which don't have defaults set
    try:
        # Get the specific replication execution
        api_response = api_instance.get_replication_execution(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->get_replication_execution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution. |

### Return type

[**ReplicationExecution**](ReplicationExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replication_log**
> str get_replication_log(id, task_id)

Get the log of the specific replication task

Get the log of the specific replication task

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import replication_api
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
    api_instance = replication_api.ReplicationApi(api_client)
    id = 1 # int | The ID of the execution that the tasks belongs to.
    task_id = 1 # int | The ID of the task.

    # example passing only required values which don't have defaults set
    try:
        # Get the log of the specific replication task
        api_response = api_instance.get_replication_log(id, task_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->get_replication_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution that the tasks belongs to. |
 **task_id** | **int**| The ID of the task. |

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Type - The content type of the addition <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replication_executions**
> [ReplicationExecution] list_replication_executions()

List replication executions

List replication executions

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import replication_api
from harbor_client.model.replication_execution import ReplicationExecution
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
    api_instance = replication_api.ReplicationApi(api_client)
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10
    policy_id = 1 # int | The ID of the policy that the executions belong to. (optional)
    status = "status_example" # str | The execution status. (optional)
    trigger = "trigger_example" # str | The trigger mode. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List replication executions
        api_response = api_instance.list_replication_executions(page=page, page_size=page_size, policy_id=policy_id, status=status, trigger=trigger)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->list_replication_executions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10
 **policy_id** | **int**| The ID of the policy that the executions belong to. | [optional]
 **status** | **str**| The execution status. | [optional]
 **trigger** | **str**| The trigger mode. | [optional]

### Return type

[**[ReplicationExecution]**](ReplicationExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Total-Count - The total count of tags <br>  * Link - Link refers to the previous page and next page <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replication_tasks**
> [ReplicationTask] list_replication_tasks(id)

List replication tasks for a specific execution

List replication tasks for a specific execution

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import replication_api
from harbor_client.model.replication_task import ReplicationTask
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
    api_instance = replication_api.ReplicationApi(api_client)
    id = 1 # int | The ID of the execution that the tasks belongs to.
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10
    status = "status_example" # str | The task status. (optional)
    resource_type = "resource_type_example" # str | The resource type. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List replication tasks for a specific execution
        api_response = api_instance.list_replication_tasks(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->list_replication_tasks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List replication tasks for a specific execution
        api_response = api_instance.list_replication_tasks(id, page=page, page_size=page_size, status=status, resource_type=resource_type)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->list_replication_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution that the tasks belongs to. |
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10
 **status** | **str**| The task status. | [optional]
 **resource_type** | **str**| The resource type. | [optional]

### Return type

[**[ReplicationTask]**](ReplicationTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Total-Count - The total count of tags <br>  * Link - Link refers to the previous page and next page <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_replication**
> start_replication(execution)

Start one replication execution

Start one replication execution according to the policy

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import replication_api
from harbor_client.model.start_replication_execution import StartReplicationExecution
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
    api_instance = replication_api.ReplicationApi(api_client)
    execution = StartReplicationExecution(
        policy_id=1,
    ) # StartReplicationExecution | The ID of policy that the execution belongs to

    # example passing only required values which don't have defaults set
    try:
        # Start one replication execution
        api_instance.start_replication(execution)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->start_replication: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution** | [**StartReplicationExecution**](StartReplicationExecution.md)| The ID of policy that the execution belongs to |

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
**201** | Created |  * X-Request-Id - The ID of the corresponding request for the response <br>  * Location - The location of the resource <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_replication**
> stop_replication(id)

Stop the specific replication execution

Stop the replication execution specified by ID

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import replication_api
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
    api_instance = replication_api.ReplicationApi(api_client)
    id = 1 # int | The ID of the execution.

    # example passing only required values which don't have defaults set
    try:
        # Stop the specific replication execution
        api_instance.stop_replication(id)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->stop_replication: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

