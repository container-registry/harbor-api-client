# harbor_client.ProjectApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /projects | Create a new project.
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /projects/{project_name_or_id} | Delete project by projectID
[**get_logs**](ProjectApi.md#get_logs) | **GET** /projects/{project_name}/logs | Get recent logs of the projects
[**get_project**](ProjectApi.md#get_project) | **GET** /projects/{project_name_or_id} | Return specific project detail information
[**get_project_deletable**](ProjectApi.md#get_project_deletable) | **GET** /projects/{project_name_or_id}/_deletable | Get the deletable status of the project
[**get_project_summary**](ProjectApi.md#get_project_summary) | **GET** /projects/{project_name_or_id}/summary | Get summary of the project.
[**get_scanner_of_project**](ProjectApi.md#get_scanner_of_project) | **GET** /projects/{project_name_or_id}/scanner | Get project level scanner
[**head_project**](ProjectApi.md#head_project) | **HEAD** /projects | Check if the project name user provided already exists.
[**list_projects**](ProjectApi.md#list_projects) | **GET** /projects | List projects
[**list_scanner_candidates_of_project**](ProjectApi.md#list_scanner_candidates_of_project) | **GET** /projects/{project_name_or_id}/scanner/candidates | Get scanner registration candidates for configurating project level scanner
[**set_scanner_of_project**](ProjectApi.md#set_scanner_of_project) | **PUT** /projects/{project_name_or_id}/scanner | Configure scanner for the specified project
[**update_project**](ProjectApi.md#update_project) | **PUT** /projects/{project_name_or_id} | Update properties for a selected project.


# **create_project**
> create_project(project, x_request_id=x_request_id, x_resource_name_in_location=x_resource_name_in_location)

Create a new project.

This endpoint is for user to create a new project.

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
project = harbor_client.ProjectReq() # ProjectReq | New created project.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_resource_name_in_location = false # bool | The flag to indicate whether to return the name of the resource in Location. When X-Resource-Name-In-Location is true, the Location will return the name of the resource. (optional) (default to false)

try:
    # Create a new project.
    api_instance.create_project(project, x_request_id=x_request_id, x_resource_name_in_location=x_resource_name_in_location)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**ProjectReq**](ProjectReq.md)| New created project. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_resource_name_in_location** | **bool**| The flag to indicate whether to return the name of the resource in Location. When X-Resource-Name-In-Location is true, the Location will return the name of the resource. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Delete project by projectID

This endpoint is aimed to delete project by project ID.

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Delete project by projectID
    api_instance.delete_project(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
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

# **get_logs**
> list[AuditLog] get_logs(project_name, x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)

Get recent logs of the projects

Get recent logs of the projects

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    # Get recent logs of the projects
    api_response = api_instance.get_logs(project_name, x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]

### Return type

[**list[AuditLog]**](AuditLog.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Return specific project detail information

This endpoint returns specific project information by project ID.

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Return specific project detail information
    api_response = api_instance.get_project(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]

### Return type

[**Project**](Project.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_deletable**
> ProjectDeletable get_project_deletable(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Get the deletable status of the project

Get the deletable status of the project

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Get the deletable status of the project
    api_response = api_instance.get_project_deletable(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_deletable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]

### Return type

[**ProjectDeletable**](ProjectDeletable.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_summary**
> ProjectSummary get_project_summary(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Get summary of the project.

Get summary of the project.

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Get summary of the project.
    api_response = api_instance.get_project_summary(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]

### Return type

[**ProjectSummary**](ProjectSummary.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scanner_of_project**
> ScannerRegistration get_scanner_of_project(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Get project level scanner

Get the scanner registration of the specified project. If no scanner registration is configured for the specified project, the system default scanner registration will be returned.

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Get project level scanner
    api_response = api_instance.get_scanner_of_project(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_scanner_of_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]

### Return type

[**ScannerRegistration**](ScannerRegistration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_project**
> head_project(project_name, x_request_id=x_request_id)

Check if the project name user provided already exists.

This endpoint is used to check if the project name provided already exist.

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | Project name for checking exists.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Check if the project name user provided already exists.
    api_instance.head_project(project_name, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ProjectApi->head_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| Project name for checking exists. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> list[Project] list_projects(x_request_id=x_request_id, q=q, page=page, page_size=page_size, sort=sort, name=name, public=public, owner=owner, with_detail=with_detail)

List projects

This endpoint returns projects created by Harbor.

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
name = 'name_example' # str | The name of project. (optional)
public = true # bool | The project is public or private. (optional)
owner = 'owner_example' # str | The name of project owner. (optional)
with_detail = true # bool | Bool value indicating whether return detailed information of the project (optional) (default to true)

try:
    # List projects
    api_response = api_instance.list_projects(x_request_id=x_request_id, q=q, page=page, page_size=page_size, sort=sort, name=name, public=public, owner=owner, with_detail=with_detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **name** | **str**| The name of project. | [optional] 
 **public** | **bool**| The project is public or private. | [optional] 
 **owner** | **str**| The name of project owner. | [optional] 
 **with_detail** | **bool**| Bool value indicating whether return detailed information of the project | [optional] [default to true]

### Return type

[**list[Project]**](Project.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scanner_candidates_of_project**
> list[ScannerRegistration] list_scanner_candidates_of_project(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, q=q, sort=sort, page=page, page_size=page_size)

Get scanner registration candidates for configurating project level scanner

Retrieve the system configured scanner registrations as candidates of setting project level scanner.

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    # Get scanner registration candidates for configurating project level scanner
    api_response = api_instance.list_scanner_candidates_of_project(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, q=q, sort=sort, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_scanner_candidates_of_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]
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

# **set_scanner_of_project**
> set_scanner_of_project(project_name_or_id, payload, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Configure scanner for the specified project

Set one of the system configured scanner registration as the indepndent scanner of the specified project.

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
payload = harbor_client.ProjectScanner() # ProjectScanner | 
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Configure scanner for the specified project
    api_instance.set_scanner_of_project(project_name_or_id, payload, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
except ApiException as e:
    print("Exception when calling ProjectApi->set_scanner_of_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **payload** | [**ProjectScanner**](ProjectScanner.md)|  | 
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

# **update_project**
> update_project(project_name_or_id, project, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Update properties for a selected project.

This endpoint is aimed to update the properties of a project.

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
api_instance = harbor_client.ProjectApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
project = harbor_client.ProjectReq() # ProjectReq | Updates of project.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Update properties for a selected project.
    api_instance.update_project(project_name_or_id, project, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **project** | [**ProjectReq**](ProjectReq.md)| Updates of project. | 
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

