# harbor_client.SystemApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_cve_allowlist_get**](SystemApi.md#system_cve_allowlist_get) | **GET** /system/CVEAllowlist | Get the system level allowlist of CVE.
[**system_cve_allowlist_put**](SystemApi.md#system_cve_allowlist_put) | **PUT** /system/CVEAllowlist | Update the system level allowlist of CVE.
[**system_oidc_ping_post**](SystemApi.md#system_oidc_ping_post) | **POST** /system/oidc/ping | Test the OIDC endpoint.


# **system_cve_allowlist_get**
> CVEAllowlist system_cve_allowlist_get()

Get the system level allowlist of CVE.

Get the system level allowlist of CVE.  This API can be called by all authenticated users.

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import system_api
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the system level allowlist of CVE.
        api_response = api_instance.system_cve_allowlist_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling SystemApi->system_cve_allowlist_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CVEAllowlist**](CVEAllowlist.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the CVE allowlist. |  -  |
**401** | User is not authenticated. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_cve_allowlist_put**
> system_cve_allowlist_put()

Update the system level allowlist of CVE.

This API overwrites the system level allowlist of CVE with the list in request body.  Only system Admin has permission to call this API.

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import system_api
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)
    cve_allowlist = CVEAllowlist(
        items=[
            CVEAllowlistItem(
                cve_id="cve_id_example",
            ),
        ],
        project_id=1,
        id=1,
        expires_at=1,
    ) # CVEAllowlist | The allowlist with new content (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the system level allowlist of CVE.
        api_instance.system_cve_allowlist_put(cve_allowlist=cve_allowlist)
    except harbor_client.ApiException as e:
        print("Exception when calling SystemApi->system_cve_allowlist_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_allowlist** | [**CVEAllowlist**](CVEAllowlist.md)| The allowlist with new content | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the CVE allowlist. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User does not have permission to call this API. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_oidc_ping_post**
> system_oidc_ping_post(inline_object1)

Test the OIDC endpoint.

Test the OIDC endpoint, the setting of the endpoint is provided in the request.  This API can only be called by system admin.

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import system_api
from harbor_client.model.inline_object1 import InlineObject1
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)
    inline_object1 = InlineObject1(
        url="url_example",
        verify_cert=True,
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Test the OIDC endpoint.
        api_instance.system_oidc_ping_post(inline_object1)
    except harbor_client.ApiException as e:
        print("Exception when calling SystemApi->system_oidc_ping_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ping succeeded.  The OIDC endpoint is valid. |  -  |
**400** | The ping failed |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission to call this API |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

