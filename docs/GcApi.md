# harbor_client.GcApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gc_schedule**](GcApi.md#create_gc_schedule) | **POST** /system/gc/schedule | Create a gc schedule.
[**get_gc**](GcApi.md#get_gc) | **GET** /system/gc/{gc_id} | Get gc status.
[**get_gc_history**](GcApi.md#get_gc_history) | **GET** /system/gc | Get gc results.
[**get_gc_log**](GcApi.md#get_gc_log) | **GET** /system/gc/{gc_id}/log | Get gc job log.
[**get_gc_schedule**](GcApi.md#get_gc_schedule) | **GET** /system/gc/schedule | Get gc&#39;s schedule.
[**stop_gc**](GcApi.md#stop_gc) | **PUT** /system/gc/{gc_id} | Stop the specific GC execution
[**update_gc_schedule**](GcApi.md#update_gc_schedule) | **PUT** /system/gc/schedule | Update gc&#39;s schedule.


# **create_gc_schedule**
> create_gc_schedule(schedule, x_request_id=x_request_id)

Create a gc schedule.

This endpoint is for update gc schedule. 

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
api_instance = harbor_client.GcApi(harbor_client.ApiClient(configuration))
schedule = harbor_client.Schedule() # Schedule | Updates of gc's schedule.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create a gc schedule.
    api_instance.create_gc_schedule(schedule, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling GcApi->create_gc_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | [**Schedule**](Schedule.md)| Updates of gc&#39;s schedule. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gc**
> GCHistory get_gc(gc_id, x_request_id=x_request_id)

Get gc status.

This endpoint let user get gc status filtered by specific ID.

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
api_instance = harbor_client.GcApi(harbor_client.ApiClient(configuration))
gc_id = 789 # int | The ID of the gc log
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get gc status.
    api_response = api_instance.get_gc(gc_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GcApi->get_gc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gc_id** | **int**| The ID of the gc log | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**GCHistory**](GCHistory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gc_history**
> list[GCHistory] get_gc_history(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)

Get gc results.

This endpoint let user get gc execution history.

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
api_instance = harbor_client.GcApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    # Get gc results.
    api_response = api_instance.get_gc_history(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GcApi->get_gc_history: %s\n" % e)
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

[**list[GCHistory]**](GCHistory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gc_log**
> str get_gc_log(gc_id, x_request_id=x_request_id)

Get gc job log.

This endpoint let user get gc job logs filtered by specific ID.

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
api_instance = harbor_client.GcApi(harbor_client.ApiClient(configuration))
gc_id = 789 # int | The ID of the gc log
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get gc job log.
    api_response = api_instance.get_gc_log(gc_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GcApi->get_gc_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gc_id** | **int**| The ID of the gc log | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gc_schedule**
> GCHistory get_gc_schedule(x_request_id=x_request_id)

Get gc's schedule.

This endpoint is for get schedule of gc job.

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
api_instance = harbor_client.GcApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get gc's schedule.
    api_response = api_instance.get_gc_schedule(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GcApi->get_gc_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**GCHistory**](GCHistory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_gc**
> stop_gc(gc_id, x_request_id=x_request_id)

Stop the specific GC execution

Stop the GC execution specified by ID

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
api_instance = harbor_client.GcApi(harbor_client.ApiClient(configuration))
gc_id = 789 # int | The ID of the gc log
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Stop the specific GC execution
    api_instance.stop_gc(gc_id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling GcApi->stop_gc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gc_id** | **int**| The ID of the gc log | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gc_schedule**
> update_gc_schedule(schedule, x_request_id=x_request_id)

Update gc's schedule.

This endpoint is for update gc schedule. 

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
api_instance = harbor_client.GcApi(harbor_client.ApiClient(configuration))
schedule = harbor_client.Schedule() # Schedule | Updates of gc's schedule.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update gc's schedule.
    api_instance.update_gc_schedule(schedule, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling GcApi->update_gc_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | [**Schedule**](Schedule.md)| Updates of gc&#39;s schedule. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

