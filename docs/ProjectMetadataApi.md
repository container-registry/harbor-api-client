# harbor_client.ProjectMetadataApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project_metadatas**](ProjectMetadataApi.md#add_project_metadatas) | **POST** /projects/{project_name_or_id}/metadatas/ | Add metadata for the specific project
[**delete_project_metadata**](ProjectMetadataApi.md#delete_project_metadata) | **DELETE** /projects/{project_name_or_id}/metadatas/{meta_name} | Delete the specific metadata for the specific project
[**get_project_metadata**](ProjectMetadataApi.md#get_project_metadata) | **GET** /projects/{project_name_or_id}/metadatas/{meta_name} | Get the specific metadata of the specific project
[**list_project_metadatas**](ProjectMetadataApi.md#list_project_metadatas) | **GET** /projects/{project_name_or_id}/metadatas/ | Get the metadata of the specific project
[**update_project_metadata**](ProjectMetadataApi.md#update_project_metadata) | **PUT** /projects/{project_name_or_id}/metadatas/{meta_name} | Update the specific metadata for the specific project


# **add_project_metadatas**
> add_project_metadatas(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, metadata=metadata)

Add metadata for the specific project

Add metadata for the specific project

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
api_instance = harbor_client.ProjectMetadataApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)
metadata = NULL # object |  (optional)

try:
    # Add metadata for the specific project
    api_instance.add_project_metadatas(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, metadata=metadata)
except ApiException as e:
    print("Exception when calling ProjectMetadataApi->add_project_metadatas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]
 **metadata** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_metadata**
> delete_project_metadata(project_name_or_id, meta_name, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Delete the specific metadata for the specific project

Delete the specific metadata for the specific project

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
api_instance = harbor_client.ProjectMetadataApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
meta_name = 'meta_name_example' # str | The name of metadata.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Delete the specific metadata for the specific project
    api_instance.delete_project_metadata(project_name_or_id, meta_name, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
except ApiException as e:
    print("Exception when calling ProjectMetadataApi->delete_project_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **meta_name** | **str**| The name of metadata. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_metadata**
> dict(str, str) get_project_metadata(project_name_or_id, meta_name, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Get the specific metadata of the specific project

Get the specific metadata of the specific project

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
api_instance = harbor_client.ProjectMetadataApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
meta_name = 'meta_name_example' # str | The name of metadata.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Get the specific metadata of the specific project
    api_response = api_instance.get_project_metadata(project_name_or_id, meta_name, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMetadataApi->get_project_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **meta_name** | **str**| The name of metadata. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]

### Return type

**dict(str, str)**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_metadatas**
> dict(str, str) list_project_metadatas(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Get the metadata of the specific project

Get the metadata of the specific project

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
api_instance = harbor_client.ProjectMetadataApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Get the metadata of the specific project
    api_response = api_instance.list_project_metadatas(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMetadataApi->list_project_metadatas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]

### Return type

**dict(str, str)**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_metadata**
> update_project_metadata(project_name_or_id, meta_name, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, metadata=metadata)

Update the specific metadata for the specific project

Update the specific metadata for the specific project

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
api_instance = harbor_client.ProjectMetadataApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
meta_name = 'meta_name_example' # str | The name of metadata.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)
metadata = NULL # object |  (optional)

try:
    # Update the specific metadata for the specific project
    api_instance.update_project_metadata(project_name_or_id, meta_name, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, metadata=metadata)
except ApiException as e:
    print("Exception when calling ProjectMetadataApi->update_project_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **meta_name** | **str**| The name of metadata. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]
 **metadata** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

