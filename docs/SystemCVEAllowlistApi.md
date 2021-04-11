# harbor_client.SystemCVEAllowlistApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_cve_allowlist**](SystemCVEAllowlistApi.md#get_system_cve_allowlist) | **GET** /system/CVEAllowlist | Get the system level allowlist of CVE.
[**put_system_cve_allowlist**](SystemCVEAllowlistApi.md#put_system_cve_allowlist) | **PUT** /system/CVEAllowlist | Update the system level allowlist of CVE.


# **get_system_cve_allowlist**
> CVEAllowlist get_system_cve_allowlist()

Get the system level allowlist of CVE.

Get the system level allowlist of CVE.  This API can be called by all authenticated users.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import system_cve_allowlist_api
from harbor_client.model.errors import Errors
from harbor_client.model.cve_allowlist import CVEAllowlist
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
    api_instance = system_cve_allowlist_api.SystemCVEAllowlistApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the system level allowlist of CVE.
        api_response = api_instance.get_system_cve_allowlist()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling SystemCVEAllowlistApi->get_system_cve_allowlist: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CVEAllowlist**](CVEAllowlist.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the CVE allowlist. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_cve_allowlist**
> put_system_cve_allowlist()

Update the system level allowlist of CVE.

This API overwrites the system level allowlist of CVE with the list in request body.  Only system Admin has permission to call this API.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import system_cve_allowlist_api
from harbor_client.model.errors import Errors
from harbor_client.model.cve_allowlist import CVEAllowlist
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
    api_instance = system_cve_allowlist_api.SystemCVEAllowlistApi(api_client)
    cve_allowlist = CVEAllowlist(
        id=1,
        project_id=1,
        expires_at=1,
        items=[
            CVEAllowlistItem(
                cve_id="cve_id_example",
            ),
        ],
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # CVEAllowlist | The allowlist with new content (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the system level allowlist of CVE.
        api_instance.put_system_cve_allowlist(cve_allowlist=cve_allowlist)
    except harbor_client.ApiException as e:
        print("Exception when calling SystemCVEAllowlistApi->put_system_cve_allowlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_allowlist** | [**CVEAllowlist**](CVEAllowlist.md)| The allowlist with new content | [optional]

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
**200** | Successfully updated the CVE allowlist. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

