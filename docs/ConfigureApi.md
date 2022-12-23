# harbor_client.ConfigureApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configurations**](ConfigureApi.md#get_configurations) | **GET** /configurations | Get system configurations.
[**get_internalconfig**](ConfigureApi.md#get_internalconfig) | **GET** /internalconfig | Get internal configurations.
[**update_configurations**](ConfigureApi.md#update_configurations) | **PUT** /configurations | Modify system configurations.


# **get_configurations**
> ConfigurationsResponse get_configurations(x_request_id=x_request_id)

Get system configurations.

This endpoint is for retrieving system configurations that only provides for admin user. 

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
api_instance = harbor_client.ConfigureApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get system configurations.
    api_response = api_instance.get_configurations(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigureApi->get_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ConfigurationsResponse**](ConfigurationsResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_internalconfig**
> InternalConfigurationsResponse get_internalconfig(x_request_id=x_request_id)

Get internal configurations.

This endpoint is for retrieving system configurations that only provides for internal api call. 

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
api_instance = harbor_client.ConfigureApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get internal configurations.
    api_response = api_instance.get_internalconfig(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigureApi->get_internalconfig: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**InternalConfigurationsResponse**](InternalConfigurationsResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configurations**
> update_configurations(configurations, x_request_id=x_request_id)

Modify system configurations.

This endpoint is for modifying system configurations that only provides for admin user. 

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
api_instance = harbor_client.ConfigureApi(harbor_client.ApiClient(configuration))
configurations = harbor_client.Configurations() # Configurations | The configuration map can contain a subset of the attributes of the schema, which are to be updated.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Modify system configurations.
    api_instance.update_configurations(configurations, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ConfigureApi->update_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configurations** | [**Configurations**](Configurations.md)| The configuration map can contain a subset of the attributes of the schema, which are to be updated. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

