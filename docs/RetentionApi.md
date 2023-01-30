# harbor_client.RetentionApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_retention**](RetentionApi.md#create_retention) | **POST** /retentions | Create Retention Policy
[**delete_retention**](RetentionApi.md#delete_retention) | **DELETE** /retentions/{id} | Delete Retention Policy
[**get_rentenition_metadata**](RetentionApi.md#get_rentenition_metadata) | **GET** /retentions/metadatas | Get Retention Metadatas
[**get_retention**](RetentionApi.md#get_retention) | **GET** /retentions/{id} | Get Retention Policy
[**get_retention_task_log**](RetentionApi.md#get_retention_task_log) | **GET** /retentions/{id}/executions/{eid}/tasks/{tid} | Get Retention job task log
[**list_retention_executions**](RetentionApi.md#list_retention_executions) | **GET** /retentions/{id}/executions | Get Retention executions
[**list_retention_tasks**](RetentionApi.md#list_retention_tasks) | **GET** /retentions/{id}/executions/{eid}/tasks | Get Retention tasks
[**operate_retention_execution**](RetentionApi.md#operate_retention_execution) | **PATCH** /retentions/{id}/executions/{eid} | Stop a Retention execution
[**trigger_retention_execution**](RetentionApi.md#trigger_retention_execution) | **POST** /retentions/{id}/executions | Trigger a Retention Execution
[**update_retention**](RetentionApi.md#update_retention) | **PUT** /retentions/{id} | Update Retention Policy


# **create_retention**
> create_retention(policy, x_request_id=x_request_id)

Create Retention Policy

Create Retention Policy, you can reference metadatas API for the policy model. You can check project metadatas to find whether a retention policy is already binded. This method should only be called when no retention policy binded to project yet.

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
api_instance = harbor_client.RetentionApi(harbor_client.ApiClient(configuration))
policy = harbor_client.RetentionPolicy() # RetentionPolicy | Create Retention Policy successfully.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create Retention Policy
    api_instance.create_retention(policy, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling RetentionApi->create_retention: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**RetentionPolicy**](RetentionPolicy.md)| Create Retention Policy successfully. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_retention**
> delete_retention(id, x_request_id=x_request_id)

Delete Retention Policy

Delete Retention Policy, you can reference metadatas API for the policy model. You can check project metadatas to find whether a retention policy is already binded. This method should only be called when retention policy has already binded to project.

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
api_instance = harbor_client.RetentionApi(harbor_client.ApiClient(configuration))
id = 789 # int | Retention ID.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete Retention Policy
    api_instance.delete_retention(id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling RetentionApi->delete_retention: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rentenition_metadata**
> RetentionMetadata get_rentenition_metadata(x_request_id=x_request_id)

Get Retention Metadatas

Get Retention Metadatas.

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
api_instance = harbor_client.RetentionApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get Retention Metadatas
    api_response = api_instance.get_rentenition_metadata(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->get_rentenition_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**RetentionMetadata**](RetentionMetadata.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_retention**
> RetentionPolicy get_retention(id, x_request_id=x_request_id)

Get Retention Policy

Get Retention Policy.

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
api_instance = harbor_client.RetentionApi(harbor_client.ApiClient(configuration))
id = 789 # int | Retention ID.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get Retention Policy
    api_response = api_instance.get_retention(id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->get_retention: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**RetentionPolicy**](RetentionPolicy.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_retention_task_log**
> str get_retention_task_log(id, eid, tid, x_request_id=x_request_id)

Get Retention job task log

Get Retention job task log, tags ratain or deletion detail will be shown in a table.

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
api_instance = harbor_client.RetentionApi(harbor_client.ApiClient(configuration))
id = 789 # int | Retention ID.
eid = 789 # int | Retention execution ID.
tid = 789 # int | Retention execution ID.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get Retention job task log
    api_response = api_instance.get_retention_task_log(id, eid, tid, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->get_retention_task_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **eid** | **int**| Retention execution ID. | 
 **tid** | **int**| Retention execution ID. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_retention_executions**
> list[RetentionExecution] list_retention_executions(id, x_request_id=x_request_id, page=page, page_size=page_size)

Get Retention executions

Get Retention executions, execution status may be delayed before job service schedule it up.

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
api_instance = harbor_client.RetentionApi(harbor_client.ApiClient(configuration))
id = 789 # int | Retention ID.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 789 # int | The page number. (optional)
page_size = 789 # int | The size of per page. (optional)

try:
    # Get Retention executions
    api_response = api_instance.list_retention_executions(id, x_request_id=x_request_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->list_retention_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number. | [optional] 
 **page_size** | **int**| The size of per page. | [optional] 

### Return type

[**list[RetentionExecution]**](RetentionExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_retention_tasks**
> list[RetentionExecutionTask] list_retention_tasks(id, eid, x_request_id=x_request_id, page=page, page_size=page_size)

Get Retention tasks

Get Retention tasks, each repository as a task.

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
api_instance = harbor_client.RetentionApi(harbor_client.ApiClient(configuration))
id = 789 # int | Retention ID.
eid = 789 # int | Retention execution ID.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 789 # int | The page number. (optional)
page_size = 789 # int | The size of per page. (optional)

try:
    # Get Retention tasks
    api_response = api_instance.list_retention_tasks(id, eid, x_request_id=x_request_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->list_retention_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **eid** | **int**| Retention execution ID. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number. | [optional] 
 **page_size** | **int**| The size of per page. | [optional] 

### Return type

[**list[RetentionExecutionTask]**](RetentionExecutionTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operate_retention_execution**
> operate_retention_execution(id, eid, body, x_request_id=x_request_id)

Stop a Retention execution

Stop a Retention execution, only support \"stop\" action now.

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
api_instance = harbor_client.RetentionApi(harbor_client.ApiClient(configuration))
id = 789 # int | Retention ID.
eid = 789 # int | Retention execution ID.
body = harbor_client.Body1() # Body1 | The action, only support \"stop\" now.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Stop a Retention execution
    api_instance.operate_retention_execution(id, eid, body, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling RetentionApi->operate_retention_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **eid** | **int**| Retention execution ID. | 
 **body** | [**Body1**](Body1.md)| The action, only support \&quot;stop\&quot; now. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_retention_execution**
> trigger_retention_execution(id, body, x_request_id=x_request_id)

Trigger a Retention Execution

Trigger a Retention Execution, if dry_run is True, nothing would be deleted actually.

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
api_instance = harbor_client.RetentionApi(harbor_client.ApiClient(configuration))
id = 789 # int | Retention ID.
body = harbor_client.Body() # Body | 
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Trigger a Retention Execution
    api_instance.trigger_retention_execution(id, body, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling RetentionApi->trigger_retention_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **body** | [**Body**](Body.md)|  | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_retention**
> update_retention(id, policy, x_request_id=x_request_id)

Update Retention Policy

Update Retention Policy, you can reference metadatas API for the policy model. You can check project metadatas to find whether a retention policy is already binded. This method should only be called when retention policy has already binded to project.

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
api_instance = harbor_client.RetentionApi(harbor_client.ApiClient(configuration))
id = 789 # int | Retention ID.
policy = harbor_client.RetentionPolicy() # RetentionPolicy | 
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update Retention Policy
    api_instance.update_retention(id, policy, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling RetentionApi->update_retention: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **policy** | [**RetentionPolicy**](RetentionPolicy.md)|  | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

