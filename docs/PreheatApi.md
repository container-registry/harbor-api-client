# harbor_client.PreheatApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_instance**](PreheatApi.md#create_instance) | **POST** /p2p/preheat/instances | Create p2p provider instances
[**create_policy**](PreheatApi.md#create_policy) | **POST** /projects/{project_name}/preheat/policies | Create a preheat policy under a project
[**delete_instance**](PreheatApi.md#delete_instance) | **DELETE** /p2p/preheat/instances/{preheat_instance_name} | Delete the specified P2P provider instance
[**delete_policy**](PreheatApi.md#delete_policy) | **DELETE** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Delete a preheat policy
[**get_execution**](PreheatApi.md#get_execution) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id} | Get a execution detail by id
[**get_instance**](PreheatApi.md#get_instance) | **GET** /p2p/preheat/instances/{preheat_instance_name} | Get a P2P provider instance
[**get_policy**](PreheatApi.md#get_policy) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Get a preheat policy
[**get_preheat_log**](PreheatApi.md#get_preheat_log) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id}/tasks/{task_id}/logs | Get the log text stream of the specified task for the given execution
[**list_executions**](PreheatApi.md#list_executions) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions | List executions for the given policy
[**list_instances**](PreheatApi.md#list_instances) | **GET** /p2p/preheat/instances | List P2P provider instances
[**list_policies**](PreheatApi.md#list_policies) | **GET** /projects/{project_name}/preheat/policies | List preheat policies
[**list_providers**](PreheatApi.md#list_providers) | **GET** /p2p/preheat/providers | List P2P providers
[**list_providers_under_project**](PreheatApi.md#list_providers_under_project) | **GET** /projects/{project_name}/preheat/providers | Get all providers at project level
[**list_tasks**](PreheatApi.md#list_tasks) | **GET** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id}/tasks | List all the related tasks for the given execution
[**manual_preheat**](PreheatApi.md#manual_preheat) | **POST** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Manual preheat
[**ping_instances**](PreheatApi.md#ping_instances) | **POST** /p2p/preheat/instances/ping | Ping status of a instance.
[**stop_execution**](PreheatApi.md#stop_execution) | **PATCH** /projects/{project_name}/preheat/policies/{preheat_policy_name}/executions/{execution_id} | Stop a execution
[**update_instance**](PreheatApi.md#update_instance) | **PUT** /p2p/preheat/instances/{preheat_instance_name} | Update the specified P2P provider instance
[**update_policy**](PreheatApi.md#update_policy) | **PUT** /projects/{project_name}/preheat/policies/{preheat_policy_name} | Update preheat policy


# **create_instance**
> create_instance(instance, x_request_id=x_request_id)

Create p2p provider instances

Create p2p provider instances

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
instance = harbor_client.Instance() # Instance | The JSON object of instance.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create p2p provider instances
    api_instance.create_instance(instance, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PreheatApi->create_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**Instance**](Instance.md)| The JSON object of instance. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy**
> create_policy(project_name, policy, x_request_id=x_request_id)

Create a preheat policy under a project

Create a preheat policy under a project

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
policy = harbor_client.PreheatPolicy() # PreheatPolicy | The policy schema info
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create a preheat policy under a project
    api_instance.create_policy(project_name, policy, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PreheatApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **policy** | [**PreheatPolicy**](PreheatPolicy.md)| The policy schema info | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_instance**
> delete_instance(preheat_instance_name, x_request_id=x_request_id)

Delete the specified P2P provider instance

Delete the specified P2P provider instance

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
preheat_instance_name = 'preheat_instance_name_example' # str | Instance Name
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete the specified P2P provider instance
    api_instance.delete_instance(preheat_instance_name, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PreheatApi->delete_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preheat_instance_name** | **str**| Instance Name | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(project_name, preheat_policy_name, x_request_id=x_request_id)

Delete a preheat policy

Delete a preheat policy

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
preheat_policy_name = 'preheat_policy_name_example' # str | Preheat Policy Name
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete a preheat policy
    api_instance.delete_policy(project_name, preheat_policy_name, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PreheatApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **preheat_policy_name** | **str**| Preheat Policy Name | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution**
> Execution get_execution(project_name, preheat_policy_name, execution_id, x_request_id=x_request_id)

Get a execution detail by id

Get a execution detail by id

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
preheat_policy_name = 'preheat_policy_name_example' # str | Preheat Policy Name
execution_id = 56 # int | Execution ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get a execution detail by id
    api_response = api_instance.get_execution(project_name, preheat_policy_name, execution_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreheatApi->get_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **preheat_policy_name** | **str**| Preheat Policy Name | 
 **execution_id** | **int**| Execution ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**Execution**](Execution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance**
> Instance get_instance(preheat_instance_name, x_request_id=x_request_id)

Get a P2P provider instance

Get a P2P provider instance

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
preheat_instance_name = 'preheat_instance_name_example' # str | Instance Name
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get a P2P provider instance
    api_response = api_instance.get_instance(preheat_instance_name, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreheatApi->get_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preheat_instance_name** | **str**| Instance Name | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**Instance**](Instance.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> PreheatPolicy get_policy(project_name, preheat_policy_name, x_request_id=x_request_id)

Get a preheat policy

Get a preheat policy

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
preheat_policy_name = 'preheat_policy_name_example' # str | Preheat Policy Name
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get a preheat policy
    api_response = api_instance.get_policy(project_name, preheat_policy_name, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreheatApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **preheat_policy_name** | **str**| Preheat Policy Name | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**PreheatPolicy**](PreheatPolicy.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preheat_log**
> str get_preheat_log(project_name, preheat_policy_name, execution_id, task_id, x_request_id=x_request_id)

Get the log text stream of the specified task for the given execution

Get the log text stream of the specified task for the given execution

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
preheat_policy_name = 'preheat_policy_name_example' # str | Preheat Policy Name
execution_id = 56 # int | Execution ID
task_id = 56 # int | Task ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the log text stream of the specified task for the given execution
    api_response = api_instance.get_preheat_log(project_name, preheat_policy_name, execution_id, task_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreheatApi->get_preheat_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **preheat_policy_name** | **str**| Preheat Policy Name | 
 **execution_id** | **int**| Execution ID | 
 **task_id** | **int**| Task ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_executions**
> list[Execution] list_executions(project_name, preheat_policy_name, x_request_id=x_request_id, page=page, page_size=page_size, q=q, sort=sort)

List executions for the given policy

List executions for the given policy

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
preheat_policy_name = 'preheat_policy_name_example' # str | Preheat Policy Name
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)

try:
    # List executions for the given policy
    api_response = api_instance.list_executions(project_name, preheat_policy_name, x_request_id=x_request_id, page=page, page_size=page_size, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreheatApi->list_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **preheat_policy_name** | **str**| Preheat Policy Name | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 

### Return type

[**list[Execution]**](Execution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instances**
> list[Instance] list_instances(x_request_id=x_request_id, page=page, page_size=page_size, q=q, sort=sort)

List P2P provider instances

List P2P provider instances

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)

try:
    # List P2P provider instances
    api_response = api_instance.list_instances(x_request_id=x_request_id, page=page, page_size=page_size, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreheatApi->list_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 

### Return type

[**list[Instance]**](Instance.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policies**
> list[PreheatPolicy] list_policies(project_name, x_request_id=x_request_id, page=page, page_size=page_size, q=q, sort=sort)

List preheat policies

List preheat policies

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)

try:
    # List preheat policies
    api_response = api_instance.list_policies(project_name, x_request_id=x_request_id, page=page, page_size=page_size, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreheatApi->list_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 

### Return type

[**list[PreheatPolicy]**](PreheatPolicy.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> list[Metadata] list_providers(x_request_id=x_request_id)

List P2P providers

List P2P providers

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # List P2P providers
    api_response = api_instance.list_providers(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreheatApi->list_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers_under_project**
> list[ProviderUnderProject] list_providers_under_project(project_name, x_request_id=x_request_id)

Get all providers at project level

Get all providers at project level

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get all providers at project level
    api_response = api_instance.list_providers_under_project(project_name, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreheatApi->list_providers_under_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**list[ProviderUnderProject]**](ProviderUnderProject.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> list[Task] list_tasks(project_name, preheat_policy_name, execution_id, x_request_id=x_request_id, page=page, page_size=page_size, q=q, sort=sort)

List all the related tasks for the given execution

List all the related tasks for the given execution

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
preheat_policy_name = 'preheat_policy_name_example' # str | Preheat Policy Name
execution_id = 56 # int | Execution ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)

try:
    # List all the related tasks for the given execution
    api_response = api_instance.list_tasks(project_name, preheat_policy_name, execution_id, x_request_id=x_request_id, page=page, page_size=page_size, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreheatApi->list_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **preheat_policy_name** | **str**| Preheat Policy Name | 
 **execution_id** | **int**| Execution ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 

### Return type

[**list[Task]**](Task.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manual_preheat**
> manual_preheat(project_name, preheat_policy_name, policy, x_request_id=x_request_id)

Manual preheat

Manual preheat

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
preheat_policy_name = 'preheat_policy_name_example' # str | Preheat Policy Name
policy = harbor_client.PreheatPolicy() # PreheatPolicy | The policy schema info
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Manual preheat
    api_instance.manual_preheat(project_name, preheat_policy_name, policy, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PreheatApi->manual_preheat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **preheat_policy_name** | **str**| Preheat Policy Name | 
 **policy** | [**PreheatPolicy**](PreheatPolicy.md)| The policy schema info | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_instances**
> ping_instances(instance, x_request_id=x_request_id)

Ping status of a instance.

This endpoint checks status of a instance, the instance can be given by ID or Endpoint URL (together with credential) 

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
instance = harbor_client.Instance() # Instance | The JSON object of instance.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Ping status of a instance.
    api_instance.ping_instances(instance, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PreheatApi->ping_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**Instance**](Instance.md)| The JSON object of instance. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_execution**
> stop_execution(project_name, preheat_policy_name, execution_id, execution, x_request_id=x_request_id)

Stop a execution

Stop a execution

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
preheat_policy_name = 'preheat_policy_name_example' # str | Preheat Policy Name
execution_id = 56 # int | Execution ID
execution = harbor_client.Execution() # Execution | The data of execution
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Stop a execution
    api_instance.stop_execution(project_name, preheat_policy_name, execution_id, execution, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PreheatApi->stop_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **preheat_policy_name** | **str**| Preheat Policy Name | 
 **execution_id** | **int**| Execution ID | 
 **execution** | [**Execution**](Execution.md)| The data of execution | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instance**
> update_instance(preheat_instance_name, instance, x_request_id=x_request_id)

Update the specified P2P provider instance

Update the specified P2P provider instance

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
preheat_instance_name = 'preheat_instance_name_example' # str | Instance Name
instance = harbor_client.Instance() # Instance | The instance to update
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update the specified P2P provider instance
    api_instance.update_instance(preheat_instance_name, instance, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PreheatApi->update_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preheat_instance_name** | **str**| Instance Name | 
 **instance** | [**Instance**](Instance.md)| The instance to update | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> update_policy(project_name, preheat_policy_name, policy, x_request_id=x_request_id)

Update preheat policy

Update preheat policy

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
api_instance = harbor_client.PreheatApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
preheat_policy_name = 'preheat_policy_name_example' # str | Preheat Policy Name
policy = harbor_client.PreheatPolicy() # PreheatPolicy | The policy schema info
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update preheat policy
    api_instance.update_policy(project_name, preheat_policy_name, policy, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PreheatApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **preheat_policy_name** | **str**| Preheat Policy Name | 
 **policy** | [**PreheatPolicy**](PreheatPolicy.md)| The policy schema info | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

