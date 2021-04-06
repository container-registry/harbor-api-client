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
[**head_project**](ProjectApi.md#head_project) | **HEAD** /projects | Check if the project name user provided already exists.
[**list_projects**](ProjectApi.md#list_projects) | **GET** /projects | List projects
[**update_project**](ProjectApi.md#update_project) | **PUT** /projects/{project_name_or_id} | Update properties for a selected project.


# **create_project**
> create_project(project)

Create a new project.

This endpoint is for user to create a new project.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import project_api
from harbor_client.model.project_req import ProjectReq
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project = ProjectReq(
        project_name="project_name_example",
        cve_allowlist=CVEAllowlist(
            update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            items=[
                CVEAllowlistItem(
                    cve_id="cve_id_example",
                ),
            ],
            project_id=1,
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            id=1,
            expires_at=1,
        ),
        registry_id=1,
        public=True,
        storage_limit=1,
        metadata=ProjectMetadata(
            enable_content_trust="enable_content_trust_example",
            public="public_example",
            auto_scan="auto_scan_example",
            severity="severity_example",
            retention_id="retention_id_example",
            reuse_sys_cve_allowlist="reuse_sys_cve_allowlist_example",
            prevent_vul="prevent_vul_example",
        ),
    ) # ProjectReq | New created project.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_resource_name_in_location = False # bool | The flag to indicate whether to return the name of the resource in Location. When X-Resource-Name-In-Location is true, the Location will return the name of the resource. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Create a new project.
        api_instance.create_project(project)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new project.
        api_instance.create_project(project, x_request_id=x_request_id, x_resource_name_in_location=x_resource_name_in_location)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**ProjectReq**](ProjectReq.md)| New created project. |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_resource_name_in_location** | **bool**| The flag to indicate whether to return the name of the resource in Location. When X-Resource-Name-In-Location is true, the Location will return the name of the resource. | [optional] if omitted the server will use the default value of False

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-Request-Id - The ID of the corresponding request for the response <br>  * Location - The location of the resource <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**409** | Conflict |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_name_or_id)

Delete project by projectID

This endpoint is aimed to delete project by project ID.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import project_api
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete project by projectID
        api_instance.delete_project(project_name_or_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->delete_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete project by projectID
        api_instance.delete_project(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**412** | Precondition failed |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> [AuditLog] get_logs(project_name)

Get recent logs of the projects

Get recent logs of the projects

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import project_api
from harbor_client.model.audit_log import AuditLog
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    q = "q_example" # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get recent logs of the projects
        api_response = api_instance.get_logs(project_name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->get_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get recent logs of the projects
        api_response = api_instance.get_logs(project_name, x_request_id=x_request_id, q=q, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->get_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional]
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10

### Return type

[**[AuditLog]**](AuditLog.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Total-Count - The total count of tags <br>  * Link - Link refers to the previous page and next page <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_name_or_id)

Return specific project detail information

This endpoint returns specific project information by project ID.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import project_api
from harbor_client.model.project import Project
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Return specific project detail information
        api_response = api_instance.get_project(project_name_or_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return specific project detail information
        api_response = api_instance.get_project(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

[**Project**](Project.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return matched project information. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_deletable**
> ProjectDeletable get_project_deletable(project_name_or_id)

Get the deletable status of the project

Get the deletable status of the project

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import project_api
from harbor_client.model.errors import Errors
from harbor_client.model.project_deletable import ProjectDeletable
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get the deletable status of the project
        api_response = api_instance.get_project_deletable(project_name_or_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_deletable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the deletable status of the project
        api_response = api_instance.get_project_deletable(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_deletable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

[**ProjectDeletable**](ProjectDeletable.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return deletable status of the project. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_summary**
> ProjectSummary get_project_summary(project_name_or_id)

Get summary of the project.

Get summary of the project.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import project_api
from harbor_client.model.project_summary import ProjectSummary
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get summary of the project.
        api_response = api_instance.get_project_summary(project_name_or_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get summary of the project.
        api_response = api_instance.get_project_summary(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

[**ProjectSummary**](ProjectSummary.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get summary of the project successfully. |  -  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_project**
> head_project(project_name)

Check if the project name user provided already exists.

This endpoint is used to check if the project name provided already exist.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import project_api
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project_name = "project_name_example" # str | Project name for checking exists.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Check if the project name user provided already exists.
        api_instance.head_project(project_name)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->head_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check if the project name user provided already exists.
        api_instance.head_project(project_name, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> [Project] list_projects()

List projects

This endpoint returns projects created by Harbor.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import project_api
from harbor_client.model.project import Project
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10
    name = "name_example" # str | The name of project. (optional)
    public = True # bool | The project is public or private. (optional)
    owner = "owner_example" # str | The name of project owner. (optional)
    with_detail = True # bool | Bool value indicating whether return detailed information of the project (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List projects
        api_response = api_instance.list_projects(x_request_id=x_request_id, page=page, page_size=page_size, name=name, public=public, owner=owner, with_detail=with_detail)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->list_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10
 **name** | **str**| The name of project. | [optional]
 **public** | **bool**| The project is public or private. | [optional]
 **owner** | **str**| The name of project owner. | [optional]
 **with_detail** | **bool**| Bool value indicating whether return detailed information of the project | [optional] if omitted the server will use the default value of True

### Return type

[**[Project]**](Project.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return all matched projects. |  * X-Total-Count - The total count of tags <br>  * Link - Link refers to the previous page and next page <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> update_project(project_name_or_id, project)

Update properties for a selected project.

This endpoint is aimed to update the properties of a project.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import project_api
from harbor_client.model.project_req import ProjectReq
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    project = ProjectReq(
        project_name="project_name_example",
        cve_allowlist=CVEAllowlist(
            update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            items=[
                CVEAllowlistItem(
                    cve_id="cve_id_example",
                ),
            ],
            project_id=1,
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            id=1,
            expires_at=1,
        ),
        registry_id=1,
        public=True,
        storage_limit=1,
        metadata=ProjectMetadata(
            enable_content_trust="enable_content_trust_example",
            public="public_example",
            auto_scan="auto_scan_example",
            severity="severity_example",
            retention_id="retention_id_example",
            reuse_sys_cve_allowlist="reuse_sys_cve_allowlist_example",
            prevent_vul="prevent_vul_example",
        ),
    ) # ProjectReq | Updates of project.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update properties for a selected project.
        api_instance.update_project(project_name_or_id, project)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->update_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update properties for a selected project.
        api_instance.update_project(project_name_or_id, project, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    except harbor_client.ApiException as e:
        print("Exception when calling ProjectApi->update_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **project** | [**ProjectReq**](ProjectReq.md)| Updates of project. |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

