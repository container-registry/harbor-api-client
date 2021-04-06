# harbor_client.PingApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_get**](PingApi.md#ping_get) | **GET** /ping | Ping Harbor to check if it&#39;s alive.


# **ping_get**
> str ping_get()

Ping Harbor to check if it's alive.

This API simply replies a pong to indicate the process to handle API is up, disregarding the health status of dependent components.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import ping_api
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
    api_instance = ping_api.PingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Ping Harbor to check if it's alive.
        api_response = api_instance.ping_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling PingApi->ping_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API server is alive |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

