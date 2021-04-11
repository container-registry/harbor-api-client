# harbor_client.SysteminfoApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systeminfo_get**](SysteminfoApi.md#systeminfo_get) | **GET** /systeminfo | Get general system info
[**systeminfo_getcert_get**](SysteminfoApi.md#systeminfo_getcert_get) | **GET** /systeminfo/getcert | Get default root certificate.
[**systeminfo_volumes_get**](SysteminfoApi.md#systeminfo_volumes_get) | **GET** /systeminfo/volumes | Get system volume info (total/free size).


# **systeminfo_get**
> GeneralInfo systeminfo_get()

Get general system info

This API is for retrieving general system info, this can be called by anonymous request.  Some attributes will be omitted in the response when this API is called by anonymous request. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import systeminfo_api
from harbor_client.model.errors import Errors
from harbor_client.model.general_info import GeneralInfo
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
    api_instance = systeminfo_api.SysteminfoApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get general system info
        api_response = api_instance.systeminfo_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling SysteminfoApi->systeminfo_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralInfo**](GeneralInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get general info successfully. |  -  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminfo_getcert_get**
> file_type systeminfo_getcert_get()

Get default root certificate.

This endpoint is for downloading a default root certificate. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import systeminfo_api
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
    api_instance = systeminfo_api.SysteminfoApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get default root certificate.
        api_response = api_instance.systeminfo_getcert_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling SysteminfoApi->systeminfo_getcert_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**file_type**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get default root certificate successfully. |  * Content-Disposition - To set the filename of the downloaded file. <br>  |
**404** | Not found the default root certificate. |  -  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminfo_volumes_get**
> SystemInfo systeminfo_volumes_get()

Get system volume info (total/free size).

This endpoint is for retrieving system volume info that only provides for admin user.  Note that the response only reflects the storage status of local disk. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import systeminfo_api
from harbor_client.model.system_info import SystemInfo
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
    api_instance = systeminfo_api.SysteminfoApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get system volume info (total/free size).
        api_response = api_instance.systeminfo_volumes_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling SysteminfoApi->systeminfo_volumes_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get system volumes successfully. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

