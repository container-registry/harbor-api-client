# harbor_client.StatisticApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statistic**](StatisticApi.md#get_statistic) | **GET** /statistics | Get the statistic information about the projects and repositories


# **get_statistic**
> Statistic get_statistic(x_request_id=x_request_id)

Get the statistic information about the projects and repositories

Get the statistic information about the projects and repositories

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
api_instance = harbor_client.StatisticApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the statistic information about the projects and repositories
    api_response = api_instance.get_statistic(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticApi->get_statistic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**Statistic**](Statistic.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

