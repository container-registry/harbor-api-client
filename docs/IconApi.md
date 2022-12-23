# harbor_client.IconApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_icon**](IconApi.md#get_icon) | **GET** /icons/{digest} | Get artifact icon


# **get_icon**
> Icon get_icon(digest, x_request_id=x_request_id)

Get artifact icon

Get the artifact icon with the specified digest. As the original icon image is resized and encoded before returning, the parameter \"digest\" in the path doesn't match the hash of the returned content

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
api_instance = harbor_client.IconApi(harbor_client.ApiClient(configuration))
digest = 'digest_example' # str | The digest of the resource
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get artifact icon
    api_response = api_instance.get_icon(digest, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

