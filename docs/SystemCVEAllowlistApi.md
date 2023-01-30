# harbor_client.SystemCVEAllowlistApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_cve_allowlist**](SystemCVEAllowlistApi.md#get_system_cve_allowlist) | **GET** /system/CVEAllowlist | Get the system level allowlist of CVE.
[**put_system_cve_allowlist**](SystemCVEAllowlistApi.md#put_system_cve_allowlist) | **PUT** /system/CVEAllowlist | Update the system level allowlist of CVE.


# **get_system_cve_allowlist**
> CVEAllowlist get_system_cve_allowlist(x_request_id=x_request_id)

Get the system level allowlist of CVE.

Get the system level allowlist of CVE.  This API can be called by all authenticated users.

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
api_instance = harbor_client.SystemCVEAllowlistApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the system level allowlist of CVE.
    api_response = api_instance.get_system_cve_allowlist(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemCVEAllowlistApi->get_system_cve_allowlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**CVEAllowlist**](CVEAllowlist.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_cve_allowlist**
> put_system_cve_allowlist(x_request_id=x_request_id, allowlist=allowlist)

Update the system level allowlist of CVE.

This API overwrites the system level allowlist of CVE with the list in request body.  Only system Admin has permission to call this API.

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
api_instance = harbor_client.SystemCVEAllowlistApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
allowlist = harbor_client.CVEAllowlist() # CVEAllowlist | The allowlist with new content (optional)

try:
    # Update the system level allowlist of CVE.
    api_instance.put_system_cve_allowlist(x_request_id=x_request_id, allowlist=allowlist)
except ApiException as e:
    print("Exception when calling SystemCVEAllowlistApi->put_system_cve_allowlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **allowlist** | [**CVEAllowlist**](CVEAllowlist.md)| The allowlist with new content | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

