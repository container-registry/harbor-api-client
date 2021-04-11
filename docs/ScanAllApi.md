# harbor_client.ScanAllApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scan_all_schedule**](ScanAllApi.md#create_scan_all_schedule) | **POST** /system/scanAll/schedule | Create a schedule or a manual trigger for the scan all job.
[**get_latest_scan_all_metrics**](ScanAllApi.md#get_latest_scan_all_metrics) | **GET** /scans/all/metrics | Get the metrics of the latest scan all process
[**get_latest_scheduled_scan_all_metrics**](ScanAllApi.md#get_latest_scheduled_scan_all_metrics) | **GET** /scans/schedule/metrics | Get the metrics of the latest scheduled scan all process
[**get_scan_all_schedule**](ScanAllApi.md#get_scan_all_schedule) | **GET** /system/scanAll/schedule | Get scan all&#39;s schedule.
[**update_scan_all_schedule**](ScanAllApi.md#update_scan_all_schedule) | **PUT** /system/scanAll/schedule | Update scan all&#39;s schedule.


# **create_scan_all_schedule**
> create_scan_all_schedule(schedule)

Create a schedule or a manual trigger for the scan all job.

This endpoint is for creating a schedule or a manual trigger for the scan all job, which scans all of images in Harbor.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scan_all_api
from harbor_client.model.schedule import Schedule
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
    api_instance = scan_all_api.ScanAllApi(api_client)
    schedule = Schedule(
        id=1,
        status="status_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        schedule=ScheduleObj(
            type="Hourly",
            cron="cron_example",
        ),
        parameters={
            "key": {},
        },
    ) # Schedule | Create a schedule or a manual trigger for the scan all job.

    # example passing only required values which don't have defaults set
    try:
        # Create a schedule or a manual trigger for the scan all job.
        api_instance.create_scan_all_schedule(schedule)
    except harbor_client.ApiException as e:
        print("Exception when calling ScanAllApi->create_scan_all_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | [**Schedule**](Schedule.md)| Create a schedule or a manual trigger for the scan all job. |

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
**412** | Precondition failed |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_scan_all_metrics**
> Stats get_latest_scan_all_metrics()

Get the metrics of the latest scan all process

Get the metrics of the latest scan all process

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scan_all_api
from harbor_client.model.stats import Stats
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
    api_instance = scan_all_api.ScanAllApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the metrics of the latest scan all process
        api_response = api_instance.get_latest_scan_all_metrics()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScanAllApi->get_latest_scan_all_metrics: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Stats**](Stats.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**412** | Precondition failed |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_scheduled_scan_all_metrics**
> Stats get_latest_scheduled_scan_all_metrics()

Get the metrics of the latest scheduled scan all process

Get the metrics of the latest scheduled scan all process

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scan_all_api
from harbor_client.model.stats import Stats
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
    api_instance = scan_all_api.ScanAllApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the metrics of the latest scheduled scan all process
        api_response = api_instance.get_latest_scheduled_scan_all_metrics()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScanAllApi->get_latest_scheduled_scan_all_metrics: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Stats**](Stats.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**412** | Precondition failed |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scan_all_schedule**
> Schedule get_scan_all_schedule()

Get scan all's schedule.

This endpoint is for getting a schedule for the scan all job, which scans all of images in Harbor.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scan_all_api
from harbor_client.model.schedule import Schedule
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
    api_instance = scan_all_api.ScanAllApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get scan all's schedule.
        api_response = api_instance.get_scan_all_schedule()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScanAllApi->get_scan_all_schedule: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Schedule**](Schedule.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a schedule for the scan all job, which scans all of images in Harbor. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**412** | Precondition failed |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scan_all_schedule**
> update_scan_all_schedule(schedule)

Update scan all's schedule.

This endpoint is for updating the schedule of scan all job, which scans all of images in Harbor.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scan_all_api
from harbor_client.model.schedule import Schedule
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
    api_instance = scan_all_api.ScanAllApi(api_client)
    schedule = Schedule(
        id=1,
        status="status_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        schedule=ScheduleObj(
            type="Hourly",
            cron="cron_example",
        ),
        parameters={
            "key": {},
        },
    ) # Schedule | Updates the schedule of scan all job, which scans all of images in Harbor.

    # example passing only required values which don't have defaults set
    try:
        # Update scan all's schedule.
        api_instance.update_scan_all_schedule(schedule)
    except harbor_client.ApiException as e:
        print("Exception when calling ScanAllApi->update_scan_all_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | [**Schedule**](Schedule.md)| Updates the schedule of scan all job, which scans all of images in Harbor. |

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
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**412** | Precondition failed |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

