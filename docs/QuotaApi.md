# harbor_client.QuotaApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quota**](QuotaApi.md#get_quota) | **GET** /quotas/{id} | Get the specified quota
[**list_quotas**](QuotaApi.md#list_quotas) | **GET** /quotas | List quotas
[**update_quota**](QuotaApi.md#update_quota) | **PUT** /quotas/{id} | Update the specified quota


# **get_quota**
> Quota get_quota(id)

Get the specified quota

Get the specified quota

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import quota_api
from harbor_client.model.errors import Errors
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

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quota_api.QuotaApi(api_client)
    id = 1 # int | Quota ID
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the specified quota
        api_response = api_instance.get_quota(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling QuotaApi->get_quota: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the specified quota
        api_response = api_instance.get_quota(id, x_request_id=x_request_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling QuotaApi->get_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Quota ID |
 **x_request_id** | **str**| An unique ID for the request | [optional]

### Return type

[**Quota**](Quota.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the quota. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quotas**
> [Quota] list_quotas()

List quotas

List quotas

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import quota_api
from harbor_client.model.errors import Errors
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

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quota_api.QuotaApi(api_client)
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10
    reference = "reference_example" # str | The reference type of quota. (optional)
    reference_id = "reference_id_example" # str | The reference id of quota. (optional)
    sort = "sort_example" # str | Sort method, valid values include: 'hard.resource_name', '-hard.resource_name', 'used.resource_name', '-used.resource_name'. Here '-' stands for descending order, resource_name should be the real resource name of the quota.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List quotas
        api_response = api_instance.list_quotas(x_request_id=x_request_id, page=page, page_size=page_size, reference=reference, reference_id=reference_id, sort=sort)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling QuotaApi->list_quotas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10
 **reference** | **str**| The reference type of quota. | [optional]
 **reference_id** | **str**| The reference id of quota. | [optional]
 **sort** | **str**| Sort method, valid values include: &#39;hard.resource_name&#39;, &#39;-hard.resource_name&#39;, &#39;used.resource_name&#39;, &#39;-used.resource_name&#39;. Here &#39;-&#39; stands for descending order, resource_name should be the real resource name of the quota.  | [optional]

### Return type

[**[Quota]**](Quota.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the quotas. |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quota**
> update_quota(id, quota_update_req)

Update the specified quota

Update hard limits of the specified quota

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import quota_api
from harbor_client.model.quota_update_req import QuotaUpdateReq
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
    api_instance = quota_api.QuotaApi(api_client)
    id = 1 # int | Quota ID
    quota_update_req = QuotaUpdateReq(
        hard=ResourceList(
            key=1,
        ),
    ) # QuotaUpdateReq | The new hard limits for the quota
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the specified quota
        api_instance.update_quota(id, quota_update_req)
    except harbor_client.ApiException as e:
        print("Exception when calling QuotaApi->update_quota: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the specified quota
        api_instance.update_quota(id, quota_update_req, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
        print("Exception when calling QuotaApi->update_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Quota ID |
 **quota_update_req** | [**QuotaUpdateReq**](QuotaUpdateReq.md)| The new hard limits for the quota |
 **x_request_id** | **str**| An unique ID for the request | [optional]

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
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

