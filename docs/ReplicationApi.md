# harbor_client.ReplicationApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_replication_policy**](ReplicationApi.md#create_replication_policy) | **POST** /replication/policies | Create a replication policy
[**delete_replication_policy**](ReplicationApi.md#delete_replication_policy) | **DELETE** /replication/policies/{id} | Delete the specific replication policy
[**get_replication_execution**](ReplicationApi.md#get_replication_execution) | **GET** /replication/executions/{id} | Get the specific replication execution
[**get_replication_log**](ReplicationApi.md#get_replication_log) | **GET** /replication/executions/{id}/tasks/{task_id}/log | Get the log of the specific replication task
[**get_replication_policy**](ReplicationApi.md#get_replication_policy) | **GET** /replication/policies/{id} | Get the specific replication policy
[**list_replication_executions**](ReplicationApi.md#list_replication_executions) | **GET** /replication/executions | List replication executions
[**list_replication_policies**](ReplicationApi.md#list_replication_policies) | **GET** /replication/policies | List replication policies
[**list_replication_tasks**](ReplicationApi.md#list_replication_tasks) | **GET** /replication/executions/{id}/tasks | List replication tasks for a specific execution
[**start_replication**](ReplicationApi.md#start_replication) | **POST** /replication/executions | Start one replication execution
[**stop_replication**](ReplicationApi.md#stop_replication) | **PUT** /replication/executions/{id} | Stop the specific replication execution
[**update_replication_policy**](ReplicationApi.md#update_replication_policy) | **PUT** /replication/policies/{id} | Update the replication policy


# **create_replication_policy**
> create_replication_policy(replication_policy)

Create a replication policy

Create a replication policy

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import replication_api
from harbor_client.model.replication_policy import ReplicationPolicy
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
    replication_policy = ReplicationPolicy(
        id=1,
        name="name_example",
        description="description_example",
        src_registry=Registry(
            id=1,
            url="url_example",
            name="name_example",
            credential=RegistryCredential(
                type="type_example",
                access_key="access_key_example",
                access_secret="access_secret_example",
            ),
            type="type_example",
            insecure=True,
            description="description_example",
            status="status_example",
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        dest_registry=Registry(
            id=1,
            url="url_example",
            name="name_example",
            credential=RegistryCredential(
                type="type_example",
                access_key="access_key_example",
                access_secret="access_secret_example",
            ),
            type="type_example",
            insecure=True,
            description="description_example",
            status="status_example",
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        dest_namespace="dest_namespace_example",
        trigger=ReplicationTrigger(
            type="type_example",
            trigger_settings=ReplicationTriggerSettings(
                cron="cron_example",
            ),
        ),
        filters=[
            ReplicationFilter(
                type="type_example",
                value={},
            ),
        ],
        replicate_deletion=True,
        deletion=True,
        override=True,
        enabled=True,
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # ReplicationPolicy | The replication policy

    # example passing only required values which don't have defaults set
    try:
        # Create a replication policy
        api_instance.create_replication_policy(replication_policy)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->create_replication_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replication_policy** | [**ReplicationPolicy**](ReplicationPolicy.md)| The replication policy |

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
**409** | Conflict |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_replication_policy**
> delete_replication_policy(id)

Delete the specific replication policy

Delete the specific replication policy

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
    id = 1 # int | Replication policy ID

    # example passing only required values which don't have defaults set
    try:
        # Delete the specific replication policy
        api_instance.delete_replication_policy(id)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->delete_replication_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Replication policy ID |

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
**412** | Precondition failed |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
 - **Accept**: text/plain, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Type - The content type of response body <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replication_policy**
> ReplicationPolicy get_replication_policy(id)

Get the specific replication policy

Get the specific replication policy

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import replication_api
from harbor_client.model.replication_policy import ReplicationPolicy
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
    id = 1 # int | Policy ID

    # example passing only required values which don't have defaults set
    try:
        # Get the specific replication policy
        api_response = api_instance.get_replication_policy(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->get_replication_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Policy ID |

### Return type

[**ReplicationPolicy**](ReplicationPolicy.md)

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
    sort = "sort_example" # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10
    policy_id = 1 # int | The ID of the policy that the executions belong to. (optional)
    status = "status_example" # str | The execution status. (optional)
    trigger = "trigger_example" # str | The trigger mode. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List replication executions
        api_response = api_instance.list_replication_executions(sort=sort, page=page, page_size=page_size, policy_id=policy_id, status=status, trigger=trigger)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->list_replication_executions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional]
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
**200** | Success |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replication_policies**
> [ReplicationPolicy] list_replication_policies()

List replication policies

List replication policies

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import replication_api
from harbor_client.model.replication_policy import ReplicationPolicy
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
    q = "q_example" # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
    sort = "sort_example" # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10
    name = "name_example" # str | Deprecated, use \"query\" instead. The policy name. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List replication policies
        api_response = api_instance.list_replication_policies(q=q, sort=sort, page=page, page_size=page_size, name=name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->list_replication_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional]
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional]
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10
 **name** | **str**| Deprecated, use \&quot;query\&quot; instead. The policy name. | [optional]

### Return type

[**[ReplicationPolicy]**](ReplicationPolicy.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
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
    sort = "sort_example" # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
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
        api_response = api_instance.list_replication_tasks(id, sort=sort, page=page, page_size=page_size, status=status, resource_type=resource_type)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->list_replication_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution that the tasks belongs to. |
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional]
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
**200** | Success |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_replication**
> start_replication(start_replication_execution)

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
    start_replication_execution = StartReplicationExecution(
        policy_id=1,
    ) # StartReplicationExecution | The ID of policy that the execution belongs to

    # example passing only required values which don't have defaults set
    try:
        # Start one replication execution
        api_instance.start_replication(start_replication_execution)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->start_replication: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_replication_execution** | [**StartReplicationExecution**](StartReplicationExecution.md)| The ID of policy that the execution belongs to |

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

# **update_replication_policy**
> update_replication_policy(id, replication_policy)

Update the replication policy

Update the replication policy

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import replication_api
from harbor_client.model.replication_policy import ReplicationPolicy
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
    id = 1 # int | The policy ID
    replication_policy = ReplicationPolicy(
        id=1,
        name="name_example",
        description="description_example",
        src_registry=Registry(
            id=1,
            url="url_example",
            name="name_example",
            credential=RegistryCredential(
                type="type_example",
                access_key="access_key_example",
                access_secret="access_secret_example",
            ),
            type="type_example",
            insecure=True,
            description="description_example",
            status="status_example",
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        dest_registry=Registry(
            id=1,
            url="url_example",
            name="name_example",
            credential=RegistryCredential(
                type="type_example",
                access_key="access_key_example",
                access_secret="access_secret_example",
            ),
            type="type_example",
            insecure=True,
            description="description_example",
            status="status_example",
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        dest_namespace="dest_namespace_example",
        trigger=ReplicationTrigger(
            type="type_example",
            trigger_settings=ReplicationTriggerSettings(
                cron="cron_example",
            ),
        ),
        filters=[
            ReplicationFilter(
                type="type_example",
                value={},
            ),
        ],
        replicate_deletion=True,
        deletion=True,
        override=True,
        enabled=True,
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # ReplicationPolicy | The replication policy

    # example passing only required values which don't have defaults set
    try:
        # Update the replication policy
        api_instance.update_replication_policy(id, replication_policy)
    except harbor_client.ApiException as e:
        print("Exception when calling ReplicationApi->update_replication_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The policy ID |
 **replication_policy** | [**ReplicationPolicy**](ReplicationPolicy.md)| The replication policy |

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
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**409** | Conflict |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

