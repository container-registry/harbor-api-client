# harbor_client.RegistryApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_registry**](RegistryApi.md#create_registry) | **POST** /registries | Create a registry
[**delete_registry**](RegistryApi.md#delete_registry) | **DELETE** /registries/{id} | Delete the specific registry
[**get_registry**](RegistryApi.md#get_registry) | **GET** /registries/{id} | Get the specific registry
[**get_registry_info**](RegistryApi.md#get_registry_info) | **GET** /registries/{id}/info | Get the registry info
[**list_registries**](RegistryApi.md#list_registries) | **GET** /registries | List the registries
[**list_registry_provider_infos**](RegistryApi.md#list_registry_provider_infos) | **GET** /replication/adapterinfos | List all registered registry provider information
[**list_registry_provider_types**](RegistryApi.md#list_registry_provider_types) | **GET** /replication/adapters | List registry adapters
[**ping_registry**](RegistryApi.md#ping_registry) | **POST** /registries/ping | Check status of a registry
[**update_registry**](RegistryApi.md#update_registry) | **PUT** /registries/{id} | Update the registry


# **create_registry**
> create_registry(registry, x_request_id=x_request_id)

Create a registry

Create a registry

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
api_instance = harbor_client.RegistryApi(harbor_client.ApiClient(configuration))
registry = harbor_client.Registry() # Registry | The registry
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create a registry
    api_instance.create_registry(registry, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling RegistryApi->create_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | [**Registry**](Registry.md)| The registry | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registry**
> delete_registry(id, x_request_id=x_request_id)

Delete the specific registry

Delete the specific registry

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
api_instance = harbor_client.RegistryApi(harbor_client.ApiClient(configuration))
id = 789 # int | Registry ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete the specific registry
    api_instance.delete_registry(id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Registry ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry**
> Registry get_registry(id, x_request_id=x_request_id)

Get the specific registry

Get the specific registry

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
api_instance = harbor_client.RegistryApi(harbor_client.ApiClient(configuration))
id = 789 # int | Registry ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the specific registry
    api_response = api_instance.get_registry(id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Registry ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**Registry**](Registry.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_info**
> RegistryInfo get_registry_info(id, x_request_id=x_request_id)

Get the registry info

Get the registry info

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
api_instance = harbor_client.RegistryApi(harbor_client.ApiClient(configuration))
id = 789 # int | Registry ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the registry info
    api_response = api_instance.get_registry_info(id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_registry_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Registry ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**RegistryInfo**](RegistryInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_registries**
> list[Registry] list_registries(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size, name=name)

List the registries

List the registries

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
api_instance = harbor_client.RegistryApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
name = 'name_example' # str | Deprecated, use `q` instead. (optional)

try:
    # List the registries
    api_response = api_instance.list_registries(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->list_registries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **name** | **str**| Deprecated, use &#x60;q&#x60; instead. | [optional] 

### Return type

[**list[Registry]**](Registry.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_registry_provider_infos**
> dict(str, RegistryProviderInfo) list_registry_provider_infos(x_request_id=x_request_id)

List all registered registry provider information

List all registered registry provider information

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
api_instance = harbor_client.RegistryApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # List all registered registry provider information
    api_response = api_instance.list_registry_provider_infos(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->list_registry_provider_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**dict(str, RegistryProviderInfo)**](RegistryProviderInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_registry_provider_types**
> list[str] list_registry_provider_types(x_request_id=x_request_id)

List registry adapters

List registry adapters

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
api_instance = harbor_client.RegistryApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # List registry adapters
    api_response = api_instance.list_registry_provider_types(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->list_registry_provider_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

**list[str]**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_registry**
> ping_registry(registry, x_request_id=x_request_id)

Check status of a registry

Check status of a registry

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
api_instance = harbor_client.RegistryApi(harbor_client.ApiClient(configuration))
registry = harbor_client.RegistryPing() # RegistryPing | The registry
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Check status of a registry
    api_instance.ping_registry(registry, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling RegistryApi->ping_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | [**RegistryPing**](RegistryPing.md)| The registry | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_registry**
> update_registry(id, registry, x_request_id=x_request_id)

Update the registry

Update the registry

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
api_instance = harbor_client.RegistryApi(harbor_client.ApiClient(configuration))
id = 789 # int | The registry ID
registry = harbor_client.RegistryUpdate() # RegistryUpdate | The registry
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update the registry
    api_instance.update_registry(id, registry, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling RegistryApi->update_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The registry ID | 
 **registry** | [**RegistryUpdate**](RegistryUpdate.md)| The registry | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

