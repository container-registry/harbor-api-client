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
> create_replication_policy(policy, x_request_id=x_request_id)

Create a replication policy

Create a replication policy

### Example
```python
from __future__ import print_function
import time
import harbor_client
from harbor_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor_client.ReplicationApi(harbor_client.ApiClient(configuration))
policy = harbor_client.ReplicationPolicy() # ReplicationPolicy | The replication policy
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create a replication policy
    api_instance.create_replication_policy(policy, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ReplicationApi->create_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**ReplicationPolicy**](ReplicationPolicy.md)| The replication policy | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_replication_policy**
> delete_replication_policy(id, x_request_id=x_request_id)

Delete the specific replication policy

Delete the specific replication policy

### Example
```python
from __future__ import print_function
import time
import harbor_client
from harbor_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor_client.ReplicationApi(harbor_client.ApiClient(configuration))
id = 789 # int | Replication policy ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete the specific replication policy
    api_instance.delete_replication_policy(id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ReplicationApi->delete_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Replication policy ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replication_execution**
> ReplicationExecution get_replication_execution(id, x_request_id=x_request_id)

Get the specific replication execution

Get the replication execution specified by ID

### Example
```python
from __future__ import print_function
import time
import harbor_client
from harbor_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor_client.ReplicationApi(harbor_client.ApiClient(configuration))
id = 789 # int | The ID of the execution.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the specific replication execution
    api_response = api_instance.get_replication_execution(id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->get_replication_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ReplicationExecution**](ReplicationExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replication_log**
> str get_replication_log(id, task_id, x_request_id=x_request_id)

Get the log of the specific replication task

Get the log of the specific replication task

### Example
```python
from __future__ import print_function
import time
import harbor_client
from harbor_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor_client.ReplicationApi(harbor_client.ApiClient(configuration))
id = 789 # int | The ID of the execution that the tasks belongs to.
task_id = 789 # int | The ID of the task.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the log of the specific replication task
    api_response = api_instance.get_replication_log(id, task_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->get_replication_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution that the tasks belongs to. | 
 **task_id** | **int**| The ID of the task. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replication_policy**
> ReplicationPolicy get_replication_policy(id, x_request_id=x_request_id)

Get the specific replication policy

Get the specific replication policy

### Example
```python
from __future__ import print_function
import time
import harbor_client
from harbor_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor_client.ReplicationApi(harbor_client.ApiClient(configuration))
id = 789 # int | Policy ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the specific replication policy
    api_response = api_instance.get_replication_policy(id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->get_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Policy ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ReplicationPolicy**](ReplicationPolicy.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replication_executions**
> list[ReplicationExecution] list_replication_executions(x_request_id=x_request_id, sort=sort, page=page, page_size=page_size, policy_id=policy_id, status=status, trigger=trigger)

List replication executions

List replication executions

### Example
```python
from __future__ import print_function
import time
import harbor_client
from harbor_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor_client.ReplicationApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
policy_id = 56 # int | The ID of the policy that the executions belong to. (optional)
status = 'status_example' # str | The execution status. (optional)
trigger = 'trigger_example' # str | The trigger mode. (optional)

try:
    # List replication executions
    api_response = api_instance.list_replication_executions(x_request_id=x_request_id, sort=sort, page=page, page_size=page_size, policy_id=policy_id, status=status, trigger=trigger)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->list_replication_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **policy_id** | **int**| The ID of the policy that the executions belong to. | [optional] 
 **status** | **str**| The execution status. | [optional] 
 **trigger** | **str**| The trigger mode. | [optional] 

### Return type

[**list[ReplicationExecution]**](ReplicationExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replication_policies**
> list[ReplicationPolicy] list_replication_policies(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size, name=name)

List replication policies

List replication policies

### Example
```python
from __future__ import print_function
import time
import harbor_client
from harbor_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor_client.ReplicationApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
name = 'name_example' # str | Deprecated, use \"query\" instead. The policy name. (optional)

try:
    # List replication policies
    api_response = api_instance.list_replication_policies(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->list_replication_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **name** | **str**| Deprecated, use \&quot;query\&quot; instead. The policy name. | [optional] 

### Return type

[**list[ReplicationPolicy]**](ReplicationPolicy.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replication_tasks**
> list[ReplicationTask] list_replication_tasks(id, x_request_id=x_request_id, sort=sort, page=page, page_size=page_size, status=status, resource_type=resource_type)

List replication tasks for a specific execution

List replication tasks for a specific execution

### Example
```python
from __future__ import print_function
import time
import harbor_client
from harbor_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor_client.ReplicationApi(harbor_client.ApiClient(configuration))
id = 789 # int | The ID of the execution that the tasks belongs to.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
status = 'status_example' # str | The task status. (optional)
resource_type = 'resource_type_example' # str | The resource type. (optional)

try:
    # List replication tasks for a specific execution
    api_response = api_instance.list_replication_tasks(id, x_request_id=x_request_id, sort=sort, page=page, page_size=page_size, status=status, resource_type=resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->list_replication_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution that the tasks belongs to. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **status** | **str**| The task status. | [optional] 
 **resource_type** | **str**| The resource type. | [optional] 

### Return type

[**list[ReplicationTask]**](ReplicationTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_replication**
> start_replication(execution, x_request_id=x_request_id)

Start one replication execution

Start one replication execution according to the policy

### Example
```python
from __future__ import print_function
import time
import harbor_client
from harbor_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor_client.ReplicationApi(harbor_client.ApiClient(configuration))
execution = harbor_client.StartReplicationExecution() # StartReplicationExecution | The ID of policy that the execution belongs to
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Start one replication execution
    api_instance.start_replication(execution, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ReplicationApi->start_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution** | [**StartReplicationExecution**](StartReplicationExecution.md)| The ID of policy that the execution belongs to | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_replication**
> stop_replication(id, x_request_id=x_request_id)

Stop the specific replication execution

Stop the replication execution specified by ID

### Example
```python
from __future__ import print_function
import time
import harbor_client
from harbor_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor_client.ReplicationApi(harbor_client.ApiClient(configuration))
id = 789 # int | The ID of the execution.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Stop the specific replication execution
    api_instance.stop_replication(id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ReplicationApi->stop_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_replication_policy**
> update_replication_policy(id, policy, x_request_id=x_request_id)

Update the replication policy

Update the replication policy

### Example
```python
from __future__ import print_function
import time
import harbor_client
from harbor_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor_client.ReplicationApi(harbor_client.ApiClient(configuration))
id = 789 # int | The policy ID
policy = harbor_client.ReplicationPolicy() # ReplicationPolicy | The replication policy
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update the replication policy
    api_instance.update_replication_policy(id, policy, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ReplicationApi->update_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The policy ID | 
 **policy** | [**ReplicationPolicy**](ReplicationPolicy.md)| The replication policy | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

