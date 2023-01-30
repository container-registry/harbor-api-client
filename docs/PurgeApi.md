# harbor_client.PurgeApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_purge_schedule**](PurgeApi.md#create_purge_schedule) | **POST** /system/purgeaudit/schedule | Create a purge job schedule.
[**get_purge_history**](PurgeApi.md#get_purge_history) | **GET** /system/purgeaudit | Get purge job results.
[**get_purge_job**](PurgeApi.md#get_purge_job) | **GET** /system/purgeaudit/{purge_id} | Get purge job status.
[**get_purge_job_log**](PurgeApi.md#get_purge_job_log) | **GET** /system/purgeaudit/{purge_id}/log | Get purge job log.
[**get_purge_schedule**](PurgeApi.md#get_purge_schedule) | **GET** /system/purgeaudit/schedule | Get purge&#39;s schedule.
[**stop_purge**](PurgeApi.md#stop_purge) | **PUT** /system/purgeaudit/{purge_id} | Stop the specific purge audit log execution
[**update_purge_schedule**](PurgeApi.md#update_purge_schedule) | **PUT** /system/purgeaudit/schedule | Update purge job&#39;s schedule.


# **create_purge_schedule**
> create_purge_schedule(schedule, x_request_id=x_request_id)

Create a purge job schedule.

This endpoint is for update purge job schedule. 

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
api_instance = harbor_client.PurgeApi(harbor_client.ApiClient(configuration))
schedule = harbor_client.Schedule() # Schedule | The purge job's schedule, it is a json object. ｜ The sample format is ｜ {\"parameters\":{\"audit_retention_hour\":168,\"dry_run\":true, \"include_operations\":\"create,delete,pull\"},\"schedule\":{\"type\":\"Hourly\",\"cron\":\"0 0 * * * *\"}} ｜ the include_operation should be a comma separated string, e.g. create,delete,pull, if it is empty, no operation will be purged. 
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create a purge job schedule.
    api_instance.create_purge_schedule(schedule, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PurgeApi->create_purge_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | [**Schedule**](Schedule.md)| The purge job&#39;s schedule, it is a json object. ｜ The sample format is ｜ {\&quot;parameters\&quot;:{\&quot;audit_retention_hour\&quot;:168,\&quot;dry_run\&quot;:true, \&quot;include_operations\&quot;:\&quot;create,delete,pull\&quot;},\&quot;schedule\&quot;:{\&quot;type\&quot;:\&quot;Hourly\&quot;,\&quot;cron\&quot;:\&quot;0 0 * * * *\&quot;}} ｜ the include_operation should be a comma separated string, e.g. create,delete,pull, if it is empty, no operation will be purged.  | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purge_history**
> list[ExecHistory] get_purge_history(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)

Get purge job results.

get purge job execution history.

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
api_instance = harbor_client.PurgeApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    # Get purge job results.
    api_response = api_instance.get_purge_history(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurgeApi->get_purge_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]

### Return type

[**list[ExecHistory]**](ExecHistory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purge_job**
> ExecHistory get_purge_job(purge_id, x_request_id=x_request_id)

Get purge job status.

This endpoint let user get purge job status filtered by specific ID.

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
api_instance = harbor_client.PurgeApi(harbor_client.ApiClient(configuration))
purge_id = 789 # int | The ID of the purge log
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get purge job status.
    api_response = api_instance.get_purge_job(purge_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurgeApi->get_purge_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purge_id** | **int**| The ID of the purge log | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ExecHistory**](ExecHistory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purge_job_log**
> str get_purge_job_log(purge_id, x_request_id=x_request_id)

Get purge job log.

This endpoint let user get purge job logs filtered by specific ID.

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
api_instance = harbor_client.PurgeApi(harbor_client.ApiClient(configuration))
purge_id = 789 # int | The ID of the purge log
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get purge job log.
    api_response = api_instance.get_purge_job_log(purge_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurgeApi->get_purge_job_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purge_id** | **int**| The ID of the purge log | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purge_schedule**
> ExecHistory get_purge_schedule(x_request_id=x_request_id)

Get purge's schedule.

This endpoint is for get schedule of purge job.

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
api_instance = harbor_client.PurgeApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get purge's schedule.
    api_response = api_instance.get_purge_schedule(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurgeApi->get_purge_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ExecHistory**](ExecHistory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_purge**
> stop_purge(purge_id, x_request_id=x_request_id)

Stop the specific purge audit log execution

Stop the purge audit log execution specified by ID

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
api_instance = harbor_client.PurgeApi(harbor_client.ApiClient(configuration))
purge_id = 789 # int | The ID of the purge log
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Stop the specific purge audit log execution
    api_instance.stop_purge(purge_id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PurgeApi->stop_purge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purge_id** | **int**| The ID of the purge log | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_purge_schedule**
> update_purge_schedule(schedule, x_request_id=x_request_id)

Update purge job's schedule.

This endpoint is for update purge job schedule. 

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
api_instance = harbor_client.PurgeApi(harbor_client.ApiClient(configuration))
schedule = harbor_client.Schedule() # Schedule | The purge job's schedule, it is a json object. ｜ The sample format is ｜ {\"parameters\":{\"audit_retention_hour\":168,\"dry_run\":true, \"include_operations\":\"create,delete,pull\"},\"schedule\":{\"type\":\"Hourly\",\"cron\":\"0 0 * * * *\"}} ｜ the include_operation should be a comma separated string, e.g. create,delete,pull, if it is empty, no operation will be purged. 
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update purge job's schedule.
    api_instance.update_purge_schedule(schedule, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling PurgeApi->update_purge_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | [**Schedule**](Schedule.md)| The purge job&#39;s schedule, it is a json object. ｜ The sample format is ｜ {\&quot;parameters\&quot;:{\&quot;audit_retention_hour\&quot;:168,\&quot;dry_run\&quot;:true, \&quot;include_operations\&quot;:\&quot;create,delete,pull\&quot;},\&quot;schedule\&quot;:{\&quot;type\&quot;:\&quot;Hourly\&quot;,\&quot;cron\&quot;:\&quot;0 0 * * * *\&quot;}} ｜ the include_operation should be a comma separated string, e.g. create,delete,pull, if it is empty, no operation will be purged.  | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

