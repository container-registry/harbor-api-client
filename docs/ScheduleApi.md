# harbor_client.ScheduleApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schedule_paused**](ScheduleApi.md#get_schedule_paused) | **GET** /schedules/{job_type}/paused | 
[**list_schedules**](ScheduleApi.md#list_schedules) | **GET** /schedules | 


# **get_schedule_paused**
> SchedulerStatus get_schedule_paused(job_type, x_request_id=x_request_id)



Get scheduler paused status

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
api_instance = harbor_client.ScheduleApi(harbor_client.ApiClient(configuration))
job_type = 'job_type_example' # str | The type of the job. 'all' stands for all job types, current only support query with all
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    api_response = api_instance.get_schedule_paused(job_type, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->get_schedule_paused: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type** | **str**| The type of the job. &#39;all&#39; stands for all job types, current only support query with all | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**SchedulerStatus**](SchedulerStatus.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schedules**
> list[ScheduleTask] list_schedules(x_request_id=x_request_id, page=page, page_size=page_size)



List schedules

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
api_instance = harbor_client.ScheduleApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    api_response = api_instance.list_schedules(x_request_id=x_request_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->list_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]

### Return type

[**list[ScheduleTask]**](ScheduleTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

