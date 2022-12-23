# harbor_client.ScanAllApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scan_all_schedule**](ScanAllApi.md#create_scan_all_schedule) | **POST** /system/scanAll/schedule | Create a schedule or a manual trigger for the scan all job.
[**get_latest_scan_all_metrics**](ScanAllApi.md#get_latest_scan_all_metrics) | **GET** /scans/all/metrics | Get the metrics of the latest scan all process
[**get_latest_scheduled_scan_all_metrics**](ScanAllApi.md#get_latest_scheduled_scan_all_metrics) | **GET** /scans/schedule/metrics | Get the metrics of the latest scheduled scan all process
[**get_scan_all_schedule**](ScanAllApi.md#get_scan_all_schedule) | **GET** /system/scanAll/schedule | Get scan all&#39;s schedule.
[**stop_scan_all**](ScanAllApi.md#stop_scan_all) | **POST** /system/scanAll/stop | Stop scanAll job execution
[**update_scan_all_schedule**](ScanAllApi.md#update_scan_all_schedule) | **PUT** /system/scanAll/schedule | Update scan all&#39;s schedule.


# **create_scan_all_schedule**
> create_scan_all_schedule(schedule, x_request_id=x_request_id)

Create a schedule or a manual trigger for the scan all job.

This endpoint is for creating a schedule or a manual trigger for the scan all job, which scans all of images in Harbor.

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
api_instance = harbor_client.ScanAllApi(harbor_client.ApiClient(configuration))
schedule = harbor_client.Schedule() # Schedule | Create a schedule or a manual trigger for the scan all job.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create a schedule or a manual trigger for the scan all job.
    api_instance.create_scan_all_schedule(schedule, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ScanAllApi->create_scan_all_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | [**Schedule**](Schedule.md)| Create a schedule or a manual trigger for the scan all job. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_scan_all_metrics**
> Stats get_latest_scan_all_metrics(x_request_id=x_request_id)

Get the metrics of the latest scan all process

Get the metrics of the latest scan all process

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
api_instance = harbor_client.ScanAllApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the metrics of the latest scan all process
    api_response = api_instance.get_latest_scan_all_metrics(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanAllApi->get_latest_scan_all_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**Stats**](Stats.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_scheduled_scan_all_metrics**
> Stats get_latest_scheduled_scan_all_metrics(x_request_id=x_request_id)

Get the metrics of the latest scheduled scan all process

Get the metrics of the latest scheduled scan all process

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
api_instance = harbor_client.ScanAllApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the metrics of the latest scheduled scan all process
    api_response = api_instance.get_latest_scheduled_scan_all_metrics(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanAllApi->get_latest_scheduled_scan_all_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**Stats**](Stats.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scan_all_schedule**
> Schedule get_scan_all_schedule(x_request_id=x_request_id)

Get scan all's schedule.

This endpoint is for getting a schedule for the scan all job, which scans all of images in Harbor.

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
api_instance = harbor_client.ScanAllApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get scan all's schedule.
    api_response = api_instance.get_scan_all_schedule(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanAllApi->get_scan_all_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_scan_all**
> stop_scan_all(x_request_id=x_request_id)

Stop scanAll job execution

Stop scanAll job execution

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
api_instance = harbor_client.ScanAllApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Stop scanAll job execution
    api_instance.stop_scan_all(x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ScanAllApi->stop_scan_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scan_all_schedule**
> update_scan_all_schedule(schedule, x_request_id=x_request_id)

Update scan all's schedule.

This endpoint is for updating the schedule of scan all job, which scans all of images in Harbor.

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
api_instance = harbor_client.ScanAllApi(harbor_client.ApiClient(configuration))
schedule = harbor_client.Schedule() # Schedule | Updates the schedule of scan all job, which scans all of images in Harbor.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update scan all's schedule.
    api_instance.update_scan_all_schedule(schedule, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ScanAllApi->update_scan_all_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | [**Schedule**](Schedule.md)| Updates the schedule of scan all job, which scans all of images in Harbor. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

