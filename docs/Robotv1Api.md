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
> RobotCreated create_robot_v1(project_name_or_id, robot, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Create a robot account

Create a robot account

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
api_instance = harbor_client.Robotv1Api(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
robot = harbor_client.RobotCreateV1() # RobotCreateV1 | The JSON object of a robot account.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Create a robot account
    api_response = api_instance.create_robot_v1(project_name_or_id, robot, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Robotv1Api->create_robot_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **robot** | [**RobotCreateV1**](RobotCreateV1.md)| The JSON object of a robot account. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]

### Return type

[**RobotCreated**](RobotCreated.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_robot_v1**
> delete_robot_v1(project_name_or_id, robot_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Delete a robot account

This endpoint deletes specific robot account information by robot ID.

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
api_instance = harbor_client.Robotv1Api(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
robot_id = 56 # int | Robot ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Delete a robot account
    api_instance.delete_robot_v1(project_name_or_id, robot_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
except ApiException as e:
    print("Exception when calling Robotv1Api->delete_robot_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **robot_id** | **int**| Robot ID | 
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

# **get_robot_by_idv1**
> Robot get_robot_by_idv1(project_name_or_id, robot_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Get a robot account

This endpoint returns specific robot account information by robot ID.

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
api_instance = harbor_client.Robotv1Api(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
robot_id = 56 # int | Robot ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Get a robot account
    api_response = api_instance.get_robot_by_idv1(project_name_or_id, robot_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Robotv1Api->get_robot_by_idv1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **robot_id** | **int**| Robot ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]

### Return type

[**Robot**](Robot.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_robot_v1**
> list[Robot] list_robot_v1(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, page=page, page_size=page_size, q=q, sort=sort)

Get all robot accounts of specified project

Get all robot accounts of specified project

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
api_instance = harbor_client.Robotv1Api(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)

try:
    # Get all robot accounts of specified project
    api_response = api_instance.list_robot_v1(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, page=page, page_size=page_size, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Robotv1Api->list_robot_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 

### Return type

[**list[Robot]**](Robot.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_robot_v1**
> update_robot_v1(project_name_or_id, robot_id, robot, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Update status of robot account.

Used to disable/enable a specified robot account.

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
api_instance = harbor_client.Robotv1Api(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
robot_id = 56 # int | Robot ID
robot = harbor_client.Robot() # Robot | The JSON object of a robot account.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Update status of robot account.
    api_instance.update_robot_v1(project_name_or_id, robot_id, robot, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
except ApiException as e:
    print("Exception when calling Robotv1Api->update_robot_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **robot_id** | **int**| Robot ID | 
 **robot** | [**Robot**](Robot.md)| The JSON object of a robot account. | 
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

