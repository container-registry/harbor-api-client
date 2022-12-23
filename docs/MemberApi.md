# harbor_client.MemberApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_member**](MemberApi.md#create_project_member) | **POST** /projects/{project_name_or_id}/members | Create project member
[**delete_project_member**](MemberApi.md#delete_project_member) | **DELETE** /projects/{project_name_or_id}/members/{mid} | Delete project member
[**get_project_member**](MemberApi.md#get_project_member) | **GET** /projects/{project_name_or_id}/members/{mid} | Get the project member information
[**list_project_members**](MemberApi.md#list_project_members) | **GET** /projects/{project_name_or_id}/members | Get all project member information
[**update_project_member**](MemberApi.md#update_project_member) | **PUT** /projects/{project_name_or_id}/members/{mid} | Update project member


# **create_project_member**
> create_project_member(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, project_member=project_member)

Create project member

Create project member relationship, the member can be one of the user_member and group_member,  The user_member need to specify user_id or username. If the user already exist in harbor DB, specify the user_id,  If does not exist in harbor DB, it will SearchAndOnBoard the user. The group_member need to specify id or ldap_group_dn. If the group already exist in harbor DB. specify the user group's id,  If does not exist, it will SearchAndOnBoard the group. 

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
api_instance = harbor_client.MemberApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)
project_member = harbor_client.ProjectMember() # ProjectMember |  (optional)

try:
    # Create project member
    api_instance.create_project_member(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, project_member=project_member)
except ApiException as e:
    print("Exception when calling MemberApi->create_project_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]
 **project_member** | [**ProjectMember**](ProjectMember.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_member**
> delete_project_member(project_name_or_id, mid, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Delete project member

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
api_instance = harbor_client.MemberApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
mid = 789 # int | Member ID.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Delete project member
    api_instance.delete_project_member(project_name_or_id, mid, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
except ApiException as e:
    print("Exception when calling MemberApi->delete_project_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **mid** | **int**| Member ID. | 
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

# **get_project_member**
> ProjectMemberEntity get_project_member(project_name_or_id, mid, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)

Get the project member information

Get the project member information

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
api_instance = harbor_client.MemberApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
mid = 789 # int | The member ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)

try:
    # Get the project member information
    api_response = api_instance.get_project_member(project_name_or_id, mid, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemberApi->get_project_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **mid** | **int**| The member ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]

### Return type

[**ProjectMemberEntity**](ProjectMemberEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_members**
> list[ProjectMemberEntity] list_project_members(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, page=page, page_size=page_size, entityname=entityname)

Get all project member information

Get all project member information

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
api_instance = harbor_client.MemberApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
entityname = 'entityname_example' # str | The entity name to search. (optional)

try:
    # Get all project member information
    api_response = api_instance.list_project_members(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, page=page, page_size=page_size, entityname=entityname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemberApi->list_project_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **entityname** | **str**| The entity name to search. | [optional] 

### Return type

[**list[ProjectMemberEntity]**](ProjectMemberEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_member**
> update_project_member(project_name_or_id, mid, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, role=role)

Update project member

Update project member relationship

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
api_instance = harbor_client.MemberApi(harbor_client.ApiClient(configuration))
project_name_or_id = 'project_name_or_id_example' # str | The name or id of the project
mid = 789 # int | Member ID.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_is_resource_name = false # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) (default to false)
role = harbor_client.RoleRequest() # RoleRequest |  (optional)

try:
    # Update project member
    api_instance.update_project_member(project_name_or_id, mid, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, role=role)
except ApiException as e:
    print("Exception when calling MemberApi->update_project_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project | 
 **mid** | **int**| Member ID. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] [default to false]
 **role** | [**RoleRequest**](RoleRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

