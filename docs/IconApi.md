# harbor_client.IconApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_icon**](IconApi.md#get_icon) | **GET** /icons/{digest} | Get artifact icon


# **get_icon**
> Icon get_icon(digest)

Get artifact icon

Get the artifact icon with the specified digest. As the original icon image is resized and encoded before returning, the parameter \"digest\" in the path doesn't match the hash of the returned content

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import icon_api
from harbor_client.model.icon import Icon
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
    api_instance = icon_api.IconApi(api_client)
    digest = "digest_example" # str | The digest of the resource
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get artifact icon
        api_response = api_instance.get_icon(digest)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling IconApi->get_icon: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get artifact icon
        api_response = api_instance.get_icon(digest, x_request_id=x_request_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling IconApi->get_icon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digest** | **str**| The digest of the resource |
 **x_request_id** | **str**| An unique ID for the request | [optional]

### Return type

[**Icon**](Icon.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

