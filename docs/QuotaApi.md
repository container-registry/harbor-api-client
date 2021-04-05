# harbor_client.QuotaApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotas_id_get**](QuotaApi.md#quotas_id_get) | **GET** /quotas/{id} | Get the specified quota
[**quotas_id_put**](QuotaApi.md#quotas_id_put) | **PUT** /quotas/{id} | Update the specified quota


# **quotas_id_get**
> Quota quotas_id_get(id)

Get the specified quota

Get the specified quota

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import quota_api
from harbor_client.model.quota import Quota
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
    api_instance = quota_api.QuotaApi(api_client)
    id = 1 # int | Quota ID

    # example passing only required values which don't have defaults set
    try:
        # Get the specified quota
        api_response = api_instance.quotas_id_get(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling QuotaApi->quotas_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Quota ID |

### Return type

[**Quota**](Quota.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the quota. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission to call this API |  -  |
**404** | Quota does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_id_put**
> quotas_id_put(id, quota_update_req)

Update the specified quota

Update hard limits of the specified quota

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import quota_api
from harbor_client.model.quota_update_req import QuotaUpdateReq
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
    api_instance = quota_api.QuotaApi(api_client)
    id = 1 # int | Quota ID
    quota_update_req = QuotaUpdateReq(
        hard=ResourceList(
            key=1,
        ),
    ) # QuotaUpdateReq | The new hard limits for the quota

    # example passing only required values which don't have defaults set
    try:
        # Update the specified quota
        api_instance.quotas_id_put(id, quota_update_req)
    except harbor_client.ApiException as e:
        print("Exception when calling QuotaApi->quotas_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Quota ID |
 **quota_update_req** | [**QuotaUpdateReq**](QuotaUpdateReq.md)| The new hard limits for the quota |

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
**200** | Updated quota hard limits successfully. |  -  |
**400** | Illegal format of quota update request. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission to the quota. |  -  |
**404** | Quota ID does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

