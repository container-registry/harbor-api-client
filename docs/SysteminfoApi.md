# harbor_client.SysteminfoApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cert**](SysteminfoApi.md#get_cert) | **GET** /systeminfo/getcert | Get default root certificate.
[**get_system_info**](SysteminfoApi.md#get_system_info) | **GET** /systeminfo | Get general system info
[**get_volumes**](SysteminfoApi.md#get_volumes) | **GET** /systeminfo/volumes | Get system volume info (total/free size).


# **get_cert**
> file get_cert(x_request_id=x_request_id)

Get default root certificate.

This endpoint is for downloading a default root certificate. 

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
api_instance = harbor_client.SysteminfoApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get default root certificate.
    api_response = api_instance.get_cert(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SysteminfoApi->get_cert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**file**](file.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_info**
> GeneralInfo get_system_info(x_request_id=x_request_id)

Get general system info

This API is for retrieving general system info, this can be called by anonymous request.  Some attributes will be omitted in the response when this API is called by anonymous request. 

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
api_instance = harbor_client.SysteminfoApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get general system info
    api_response = api_instance.get_system_info(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SysteminfoApi->get_system_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**GeneralInfo**](GeneralInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volumes**
> SystemInfo get_volumes(x_request_id=x_request_id)

Get system volume info (total/free size).

This endpoint is for retrieving system volume info that only provides for admin user.  Note that the response only reflects the storage status of local disk. 

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
api_instance = harbor_client.SysteminfoApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get system volume info (total/free size).
    api_response = api_instance.get_volumes(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SysteminfoApi->get_volumes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

