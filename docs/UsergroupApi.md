# harbor_client.UsergroupApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_group**](UsergroupApi.md#create_user_group) | **POST** /usergroups | Create user group
[**delete_user_group**](UsergroupApi.md#delete_user_group) | **DELETE** /usergroups/{group_id} | Delete user group
[**get_user_group**](UsergroupApi.md#get_user_group) | **GET** /usergroups/{group_id} | Get user group information
[**list_user_groups**](UsergroupApi.md#list_user_groups) | **GET** /usergroups | Get all user groups information
[**search_user_groups**](UsergroupApi.md#search_user_groups) | **GET** /usergroups/search | Search groups by groupname
[**update_user_group**](UsergroupApi.md#update_user_group) | **PUT** /usergroups/{group_id} | Update group information


# **create_user_group**
> create_user_group(x_request_id=x_request_id, usergroup=usergroup)

Create user group

Create user group information

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
api_instance = harbor_client.UsergroupApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
usergroup = harbor_client.UserGroup() # UserGroup |  (optional)

try:
    # Create user group
    api_instance.create_user_group(x_request_id=x_request_id, usergroup=usergroup)
except ApiException as e:
    print("Exception when calling UsergroupApi->create_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **usergroup** | [**UserGroup**](UserGroup.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_group**
> delete_user_group(group_id, x_request_id=x_request_id)

Delete user group

Delete user group

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
api_instance = harbor_client.UsergroupApi(harbor_client.ApiClient(configuration))
group_id = 56 # int | 
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete user group
    api_instance.delete_user_group(group_id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling UsergroupApi->delete_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group**
> UserGroup get_user_group(group_id, x_request_id=x_request_id)

Get user group information

Get user group information

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
api_instance = harbor_client.UsergroupApi(harbor_client.ApiClient(configuration))
group_id = 789 # int | Group ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get user group information
    api_response = api_instance.get_user_group(group_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupApi->get_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_groups**
> list[UserGroup] list_user_groups(x_request_id=x_request_id, page=page, page_size=page_size, ldap_group_dn=ldap_group_dn, group_name=group_name)

Get all user groups information

Get all user groups information, it is open for system admin

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
api_instance = harbor_client.UsergroupApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
ldap_group_dn = 'ldap_group_dn_example' # str | search with ldap group DN (optional)
group_name = 'group_name_example' # str | group name need to search, fuzzy matches (optional)

try:
    # Get all user groups information
    api_response = api_instance.list_user_groups(x_request_id=x_request_id, page=page, page_size=page_size, ldap_group_dn=ldap_group_dn, group_name=group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupApi->list_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **ldap_group_dn** | **str**| search with ldap group DN | [optional] 
 **group_name** | **str**| group name need to search, fuzzy matches | [optional] 

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_groups**
> list[UserGroupSearchItem] search_user_groups(groupname, x_request_id=x_request_id, page=page, page_size=page_size)

Search groups by groupname

This endpoint is to search groups by group name.  It's open for all authenticated requests. 

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
api_instance = harbor_client.UsergroupApi(harbor_client.ApiClient(configuration))
groupname = 'groupname_example' # str | Group name for filtering results.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    # Search groups by groupname
    api_response = api_instance.search_user_groups(groupname, x_request_id=x_request_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupApi->search_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupname** | **str**| Group name for filtering results. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]

### Return type

[**list[UserGroupSearchItem]**](UserGroupSearchItem.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_group**
> update_user_group(group_id, x_request_id=x_request_id, usergroup=usergroup)

Update group information

Update user group information

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
api_instance = harbor_client.UsergroupApi(harbor_client.ApiClient(configuration))
group_id = 789 # int | Group ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
usergroup = harbor_client.UserGroup() # UserGroup |  (optional)

try:
    # Update group information
    api_instance.update_user_group(group_id, x_request_id=x_request_id, usergroup=usergroup)
except ApiException as e:
    print("Exception when calling UsergroupApi->update_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **usergroup** | [**UserGroup**](UserGroup.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

