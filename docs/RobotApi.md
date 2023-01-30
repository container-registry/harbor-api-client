# harbor_client.RobotApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_robot**](RobotApi.md#create_robot) | **POST** /robots | Create a robot account
[**delete_robot**](RobotApi.md#delete_robot) | **DELETE** /robots/{robot_id} | Delete a robot account
[**get_robot_by_id**](RobotApi.md#get_robot_by_id) | **GET** /robots/{robot_id} | Get a robot account
[**list_robot**](RobotApi.md#list_robot) | **GET** /robots | Get robot account
[**refresh_sec**](RobotApi.md#refresh_sec) | **PATCH** /robots/{robot_id} | Refresh the robot secret
[**update_robot**](RobotApi.md#update_robot) | **PUT** /robots/{robot_id} | Update a robot account


# **create_robot**
> RobotCreated create_robot(robot, x_request_id=x_request_id)

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
api_instance = harbor_client.RobotApi(harbor_client.ApiClient(configuration))
robot = harbor_client.RobotCreate() # RobotCreate | The JSON object of a robot account.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create a robot account
    api_response = api_instance.create_robot(robot, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->create_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot** | [**RobotCreate**](RobotCreate.md)| The JSON object of a robot account. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**RobotCreated**](RobotCreated.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_robot**
> delete_robot(robot_id, x_request_id=x_request_id)

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
api_instance = harbor_client.RobotApi(harbor_client.ApiClient(configuration))
robot_id = 56 # int | Robot ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete a robot account
    api_instance.delete_robot(robot_id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling RobotApi->delete_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_id** | **int**| Robot ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_robot_by_id**
> Robot get_robot_by_id(robot_id, x_request_id=x_request_id)

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
api_instance = harbor_client.RobotApi(harbor_client.ApiClient(configuration))
robot_id = 56 # int | Robot ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get a robot account
    api_response = api_instance.get_robot_by_id(robot_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_robot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_id** | **int**| Robot ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**Robot**](Robot.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_robot**
> list[Robot] list_robot(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)

Get robot account

List the robot accounts with the specified level and project.

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
api_instance = harbor_client.RobotApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    # Get robot account
    api_response = api_instance.list_robot(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->list_robot: %s\n" % e)
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

[**list[Robot]**](Robot.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_sec**
> RobotSec refresh_sec(robot_id, robot_sec, x_request_id=x_request_id)

Refresh the robot secret

Refresh the robot secret

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
api_instance = harbor_client.RobotApi(harbor_client.ApiClient(configuration))
robot_id = 56 # int | Robot ID
robot_sec = harbor_client.RobotSec() # RobotSec | The JSON object of a robot account.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Refresh the robot secret
    api_response = api_instance.refresh_sec(robot_id, robot_sec, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->refresh_sec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_id** | **int**| Robot ID | 
 **robot_sec** | [**RobotSec**](RobotSec.md)| The JSON object of a robot account. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**RobotSec**](RobotSec.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_robot**
> update_robot(robot_id, robot, x_request_id=x_request_id)

Update a robot account

This endpoint updates specific robot account information by robot ID.

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
api_instance = harbor_client.RobotApi(harbor_client.ApiClient(configuration))
robot_id = 56 # int | Robot ID
robot = harbor_client.Robot() # Robot | The JSON object of a robot account.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update a robot account
    api_instance.update_robot(robot_id, robot, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling RobotApi->update_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_id** | **int**| Robot ID | 
 **robot** | [**Robot**](Robot.md)| The JSON object of a robot account. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

