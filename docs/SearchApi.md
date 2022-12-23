# harbor_client.SearchApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /search | Search for projects, repositories and helm charts


# **search**
> Search search(q, x_request_id=x_request_id)

Search for projects, repositories and helm charts

The Search endpoint returns information about the projects, repositories and helm charts offered at public status or related to the current logged in user. The response includes the project, repository list and charts in a proper display order.

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
api_instance = harbor_client.SearchApi(harbor_client.ApiClient(configuration))
q = 'q_example' # str | Search parameter for project and repository name.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Search for projects, repositories and helm charts
    api_response = api_instance.search(q, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search parameter for project and repository name. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**Search**](Search.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

