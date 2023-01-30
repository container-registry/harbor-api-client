# harbor_client.ScannerApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scanner**](ScannerApi.md#create_scanner) | **POST** /scanners | Create a scanner registration
[**delete_scanner**](ScannerApi.md#delete_scanner) | **DELETE** /scanners/{registration_id} | Delete a scanner registration
[**get_scanner**](ScannerApi.md#get_scanner) | **GET** /scanners/{registration_id} | Get a scanner registration details
[**get_scanner_metadata**](ScannerApi.md#get_scanner_metadata) | **GET** /scanners/{registration_id}/metadata | Get the metadata of the specified scanner registration
[**list_scanners**](ScannerApi.md#list_scanners) | **GET** /scanners | List scanner registrations
[**ping_scanner**](ScannerApi.md#ping_scanner) | **POST** /scanners/ping | Tests scanner registration settings
[**set_scanner_as_default**](ScannerApi.md#set_scanner_as_default) | **PATCH** /scanners/{registration_id} | Set system default scanner registration
[**update_scanner**](ScannerApi.md#update_scanner) | **PUT** /scanners/{registration_id} | Update a scanner registration


# **create_scanner**
> create_scanner(registration, x_request_id=x_request_id)

Create a scanner registration

Creats a new scanner registration with the given data. 

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
api_instance = harbor_client.ScannerApi(harbor_client.ApiClient(configuration))
registration = harbor_client.ScannerRegistrationReq() # ScannerRegistrationReq | A scanner registration to be created.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create a scanner registration
    api_instance.create_scanner(registration, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ScannerApi->create_scanner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration** | [**ScannerRegistrationReq**](ScannerRegistrationReq.md)| A scanner registration to be created. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scanner**
> ScannerRegistration delete_scanner(registration_id, x_request_id=x_request_id)

Delete a scanner registration

Deletes the specified scanner registration. 

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
api_instance = harbor_client.ScannerApi(harbor_client.ApiClient(configuration))
registration_id = 'registration_id_example' # str | The scanner registration identifier.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete a scanner registration
    api_response = api_instance.delete_scanner(registration_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannerApi->delete_scanner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ScannerRegistration**](ScannerRegistration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scanner**
> ScannerRegistration get_scanner(registration_id, x_request_id=x_request_id)

Get a scanner registration details

Retruns the details of the specified scanner registration. 

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
api_instance = harbor_client.ScannerApi(harbor_client.ApiClient(configuration))
registration_id = 'registration_id_example' # str | The scanner registration identifer.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get a scanner registration details
    api_response = api_instance.get_scanner(registration_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannerApi->get_scanner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifer. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ScannerRegistration**](ScannerRegistration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scanner_metadata**
> ScannerAdapterMetadata get_scanner_metadata(registration_id, x_request_id=x_request_id)

Get the metadata of the specified scanner registration

Get the metadata of the specified scanner registration, including the capabilities and customized properties. 

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
api_instance = harbor_client.ScannerApi(harbor_client.ApiClient(configuration))
registration_id = 'registration_id_example' # str | The scanner registration identifier.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the metadata of the specified scanner registration
    api_response = api_instance.get_scanner_metadata(registration_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannerApi->get_scanner_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ScannerAdapterMetadata**](ScannerAdapterMetadata.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scanners**
> list[ScannerRegistration] list_scanners(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)

List scanner registrations

Returns a list of currently configured scanner registrations. 

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
api_instance = harbor_client.ScannerApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    # List scanner registrations
    api_response = api_instance.list_scanners(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannerApi->list_scanners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]

### Return type

[**list[ScannerRegistration]**](ScannerRegistration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_scanner**
> ping_scanner(settings, x_request_id=x_request_id)

Tests scanner registration settings

Pings scanner adapter to test endpoint URL and authorization settings. 

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
api_instance = harbor_client.ScannerApi(harbor_client.ApiClient(configuration))
settings = harbor_client.ScannerRegistrationSettings() # ScannerRegistrationSettings | A scanner registration settings to be tested.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Tests scanner registration settings
    api_instance.ping_scanner(settings, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ScannerApi->ping_scanner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**ScannerRegistrationSettings**](ScannerRegistrationSettings.md)| A scanner registration settings to be tested. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_scanner_as_default**
> set_scanner_as_default(registration_id, payload, x_request_id=x_request_id)

Set system default scanner registration

Set the specified scanner registration as the system default one. 

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
api_instance = harbor_client.ScannerApi(harbor_client.ApiClient(configuration))
registration_id = 'registration_id_example' # str | The scanner registration identifier.
payload = harbor_client.IsDefault() # IsDefault | 
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Set system default scanner registration
    api_instance.set_scanner_as_default(registration_id, payload, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ScannerApi->set_scanner_as_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. | 
 **payload** | [**IsDefault**](IsDefault.md)|  | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scanner**
> update_scanner(registration_id, registration, x_request_id=x_request_id)

Update a scanner registration

Updates the specified scanner registration. 

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
api_instance = harbor_client.ScannerApi(harbor_client.ApiClient(configuration))
registration_id = 'registration_id_example' # str | The scanner registration identifier.
registration = harbor_client.ScannerRegistrationReq() # ScannerRegistrationReq | A scanner registraiton to be updated.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update a scanner registration
    api_instance.update_scanner(registration_id, registration, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ScannerApi->update_scanner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. | 
 **registration** | [**ScannerRegistrationReq**](ScannerRegistrationReq.md)| A scanner registraiton to be updated. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

