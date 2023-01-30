# harbor_client.LabelApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_label**](LabelApi.md#create_label) | **POST** /labels | Post creates a label
[**delete_label**](LabelApi.md#delete_label) | **DELETE** /labels/{label_id} | Delete the label specified by ID.
[**get_label_by_id**](LabelApi.md#get_label_by_id) | **GET** /labels/{label_id} | Get the label specified by ID.
[**list_labels**](LabelApi.md#list_labels) | **GET** /labels | List labels according to the query strings.
[**update_label**](LabelApi.md#update_label) | **PUT** /labels/{label_id} | Update the label properties.


# **create_label**
> create_label(label, x_request_id=x_request_id)

Post creates a label

This endpoint let user creates a label. 

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
api_instance = harbor_client.LabelApi(harbor_client.ApiClient(configuration))
label = harbor_client.Label() # Label | The json object of label.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Post creates a label
    api_instance.create_label(label, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling LabelApi->create_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | [**Label**](Label.md)| The json object of label. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_label**
> delete_label(label_id, x_request_id=x_request_id)

Delete the label specified by ID.

Delete the label specified by ID. 

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
api_instance = harbor_client.LabelApi(harbor_client.ApiClient(configuration))
label_id = 789 # int | Label ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete the label specified by ID.
    api_instance.delete_label(label_id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling LabelApi->delete_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **int**| Label ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_label_by_id**
> Label get_label_by_id(label_id, x_request_id=x_request_id)

Get the label specified by ID.

This endpoint let user get the label by specific ID. 

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
api_instance = harbor_client.LabelApi(harbor_client.ApiClient(configuration))
label_id = 789 # int | Label ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the label specified by ID.
    api_response = api_instance.get_label_by_id(label_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelApi->get_label_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **int**| Label ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_labels**
> list[Label] list_labels(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size, name=name, scope=scope, project_id=project_id)

List labels according to the query strings.

This endpoint let user list labels by name, scope and project_id 

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
api_instance = harbor_client.LabelApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
name = 'name_example' # str | The label name. (optional)
scope = 'scope_example' # str | The label scope. Valid values are g and p. g for global labels and p for project labels. (optional)
project_id = 789 # int | Relevant project ID, required when scope is p. (optional)

try:
    # List labels according to the query strings.
    api_response = api_instance.list_labels(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size, name=name, scope=scope, project_id=project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelApi->list_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **name** | **str**| The label name. | [optional] 
 **scope** | **str**| The label scope. Valid values are g and p. g for global labels and p for project labels. | [optional] 
 **project_id** | **int**| Relevant project ID, required when scope is p. | [optional] 

### Return type

[**list[Label]**](Label.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_label**
> update_label(label_id, label, x_request_id=x_request_id)

Update the label properties.

This endpoint let user update label properties. 

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
api_instance = harbor_client.LabelApi(harbor_client.ApiClient(configuration))
label_id = 789 # int | Label ID
label = harbor_client.Label() # Label | The updated label json object.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update the label properties.
    api_instance.update_label(label_id, label, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling LabelApi->update_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **int**| Label ID | 
 **label** | [**Label**](Label.md)| The updated label json object. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

