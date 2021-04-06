# harbor_client.Robotv1Api

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_robot_v1**](Robotv1Api.md#create_robot_v1) | **POST** /projects/{project_name_or_id}/robots | Create a robot account
[**delete_robot_v1**](Robotv1Api.md#delete_robot_v1) | **DELETE** /projects/{project_name_or_id}/robots/{robot_id} | Delete a robot account
[**get_robot_by_idv1**](Robotv1Api.md#get_robot_by_idv1) | **GET** /projects/{project_name_or_id}/robots/{robot_id} | Get a robot account
[**list_robot_v1**](Robotv1Api.md#list_robot_v1) | **GET** /projects/{project_name_or_id}/robots | Get all robot accounts of specified project
[**update_robot_v1**](Robotv1Api.md#update_robot_v1) | **PUT** /projects/{project_name_or_id}/robots/{robot_id} | Update status of robot account.


# **create_robot_v1**
> RobotCreated create_robot_v1(project_name_or_id, robot)

Create a robot account

Create a robot account

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import robotv1_api
from harbor_client.model.robot_created import RobotCreated
from harbor_client.model.robot_create_v1 import RobotCreateV1
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
    api_instance = robotv1_api.Robotv1Api(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    robot = RobotCreateV1(
        access=[
            Access(
                action="action_example",
                resource="resource_example",
                effect="effect_example",
            ),
        ],
        name="name_example",
        expires_at=1,
        description="description_example",
    ) # RobotCreateV1 | The JSON object of a robot account.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Create a robot account
        api_response = api_instance.create_robot_v1(project_name_or_id, robot)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling Robotv1Api->create_robot_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a robot account
        api_response = api_instance.create_robot_v1(project_name_or_id, robot, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling Robotv1Api->create_robot_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **robot** | [**RobotCreateV1**](RobotCreateV1.md)| The JSON object of a robot account. |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

[**RobotCreated**](RobotCreated.md)

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
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_robot_v1**
> delete_robot_v1(project_name_or_id, robot_id)

Delete a robot account

This endpoint deletes specific robot account information by robot ID.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import robotv1_api
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
    api_instance = robotv1_api.Robotv1Api(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    robot_id = 1 # int | Robot ID
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete a robot account
        api_instance.delete_robot_v1(project_name_or_id, robot_id)
    except harbor_client.ApiException as e:
        print("Exception when calling Robotv1Api->delete_robot_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a robot account
        api_instance.delete_robot_v1(project_name_or_id, robot_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    except harbor_client.ApiException as e:
        print("Exception when calling Robotv1Api->delete_robot_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **robot_id** | **int**| Robot ID |
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
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_robot_by_idv1**
> Robot get_robot_by_idv1(project_name_or_id, robot_id)

Get a robot account

This endpoint returns specific robot account information by robot ID.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import robotv1_api
from harbor_client.model.robot import Robot
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
    api_instance = robotv1_api.Robotv1Api(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    robot_id = 1 # int | Robot ID
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get a robot account
        api_response = api_instance.get_robot_by_idv1(project_name_or_id, robot_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling Robotv1Api->get_robot_by_idv1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a robot account
        api_response = api_instance.get_robot_by_idv1(project_name_or_id, robot_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling Robotv1Api->get_robot_by_idv1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **robot_id** | **int**| Robot ID |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

[**Robot**](Robot.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return matched robot information. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_robot_v1**
> [Robot] list_robot_v1(project_name_or_id)

Get all robot accounts of specified project

Get all robot accounts of specified project

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import robotv1_api
from harbor_client.model.robot import Robot
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
    api_instance = robotv1_api.Robotv1Api(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10
    q = "q_example" # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all robot accounts of specified project
        api_response = api_instance.list_robot_v1(project_name_or_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling Robotv1Api->list_robot_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all robot accounts of specified project
        api_response = api_instance.list_robot_v1(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, page=page, page_size=page_size, q=q)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling Robotv1Api->list_robot_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional]

### Return type

[**[Robot]**](Robot.md)

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
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_robot_v1**
> update_robot_v1(project_name_or_id, robot_id, robot)

Update status of robot account.

Used to disable/enable a specified robot account.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import robotv1_api
from harbor_client.model.robot import Robot
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
    api_instance = robotv1_api.Robotv1Api(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    robot_id = 1 # int | Robot ID
    robot = Robot(
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        description="description_example",
        level="level_example",
        editable=True,
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expires_at=1,
        name="name_example",
        secret="secret_example",
        disable=True,
        duration=1,
        id=1,
        permissions=[
            RobotPermission(
                access=[
                    Access(
                        action="action_example",
                        resource="resource_example",
                        effect="effect_example",
                    ),
                ],
                kind="kind_example",
                namespace="namespace_example",
            ),
        ],
    ) # Robot | The JSON object of a robot account.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update status of robot account.
        api_instance.update_robot_v1(project_name_or_id, robot_id, robot)
    except harbor_client.ApiException as e:
        print("Exception when calling Robotv1Api->update_robot_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update status of robot account.
        api_instance.update_robot_v1(project_name_or_id, robot_id, robot, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    except harbor_client.ApiException as e:
        print("Exception when calling Robotv1Api->update_robot_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **robot_id** | **int**| Robot ID |
 **robot** | [**Robot**](Robot.md)| The JSON object of a robot account. |
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
**409** | Conflict |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

