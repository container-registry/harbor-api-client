# harbor_client.QuotaApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quota**](QuotaApi.md#get_quota) | **GET** /quotas/{id} | Get the specified quota
[**list_quotas**](QuotaApi.md#list_quotas) | **GET** /quotas | List quotas
[**update_quota**](QuotaApi.md#update_quota) | **PUT** /quotas/{id} | Update the specified quota


# **get_quota**
> Quota get_quota(id, x_request_id=x_request_id)

Get the specified quota

Get the specified quota

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
api_instance = harbor_client.QuotaApi(harbor_client.ApiClient(configuration))
id = 56 # int | Quota ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the specified quota
    api_response = api_instance.get_quota(id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quotas**
> list[Quota] list_quotas(x_request_id=x_request_id, page=page, page_size=page_size, reference=reference, reference_id=reference_id, sort=sort)

List quotas

List quotas

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
api_instance = harbor_client.QuotaApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
reference = 'reference_example' # str | The reference type of quota. (optional)
reference_id = 'reference_id_example' # str | The reference id of quota. (optional)
sort = 'sort_example' # str | Sort method, valid values include: 'hard.resource_name', '-hard.resource_name', 'used.resource_name', '-used.resource_name'. Here '-' stands for descending order, resource_name should be the real resource name of the quota.  (optional)

try:
    # List quotas
    api_response = api_instance.list_quotas(x_request_id=x_request_id, page=page, page_size=page_size, reference=reference, reference_id=reference_id, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->list_quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **reference** | **str**| The reference type of quota. | [optional] 
 **reference_id** | **str**| The reference id of quota. | [optional] 
 **sort** | **str**| Sort method, valid values include: &#39;hard.resource_name&#39;, &#39;-hard.resource_name&#39;, &#39;used.resource_name&#39;, &#39;-used.resource_name&#39;. Here &#39;-&#39; stands for descending order, resource_name should be the real resource name of the quota.  | [optional] 

### Return type

[**list[Quota]**](Quota.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quota**
> update_quota(id, hard, x_request_id=x_request_id)

Update the specified quota

Update hard limits of the specified quota

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
api_instance = harbor_client.QuotaApi(harbor_client.ApiClient(configuration))
id = 56 # int | Quota ID
hard = harbor_client.QuotaUpdateReq() # QuotaUpdateReq | The new hard limits for the quota
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update the specified quota
    api_instance.update_quota(id, hard, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling QuotaApi->update_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Quota ID | 
 **hard** | [**QuotaUpdateReq**](QuotaUpdateReq.md)| The new hard limits for the quota | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

