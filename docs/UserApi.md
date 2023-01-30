# harbor_client.UserApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /users | Create a local user.
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{user_id} | Mark a registered user as be removed.
[**get_current_user_info**](UserApi.md#get_current_user_info) | **GET** /users/current | Get current user info.
[**get_current_user_permissions**](UserApi.md#get_current_user_permissions) | **GET** /users/current/permissions | Get current user permissions.
[**get_user**](UserApi.md#get_user) | **GET** /users/{user_id} | Get a user&#39;s profile.
[**list_users**](UserApi.md#list_users) | **GET** /users | List users
[**search_users**](UserApi.md#search_users) | **GET** /users/search | Search users by username
[**set_cli_secret**](UserApi.md#set_cli_secret) | **PUT** /users/{user_id}/cli_secret | Set CLI secret for a user.
[**set_user_sys_admin**](UserApi.md#set_user_sys_admin) | **PUT** /users/{user_id}/sysadmin | Update a registered user to change to be an administrator of Harbor.
[**update_user_password**](UserApi.md#update_user_password) | **PUT** /users/{user_id}/password | Change the password on a user that already exists.
[**update_user_profile**](UserApi.md#update_user_profile) | **PUT** /users/{user_id} | Update user&#39;s profile.


# **create_user**
> create_user(user_req, x_request_id=x_request_id)

Create a local user.

This API can be used only when the authentication mode is for local DB.  When self registration is disabled.

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
api_instance = harbor_client.UserApi(harbor_client.ApiClient(configuration))
user_req = harbor_client.UserCreationReq() # UserCreationReq | The new user
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create a local user.
    api_instance.create_user(user_req, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_req** | [**UserCreationReq**](UserCreationReq.md)| The new user | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id, x_request_id=x_request_id)

Mark a registered user as be removed.

This endpoint let administrator of Harbor mark a registered user as removed.It actually won't be deleted from DB. 

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
api_instance = harbor_client.UserApi(harbor_client.ApiClient(configuration))
user_id = 56 # int | User ID for marking as to be removed.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Mark a registered user as be removed.
    api_instance.delete_user(user_id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID for marking as to be removed. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_info**
> UserResp get_current_user_info(x_request_id=x_request_id)

Get current user info.

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
api_instance = harbor_client.UserApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get current user info.
    api_response = api_instance.get_current_user_info(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_current_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**UserResp**](UserResp.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_permissions**
> list[Permission] get_current_user_permissions(x_request_id=x_request_id, scope=scope, relative=relative)

Get current user permissions.

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
api_instance = harbor_client.UserApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
scope = 'scope_example' # str | The scope for the permission (optional)
relative = true # bool | If true, the resources in the response are relative to the scope, eg for resource '/project/1/repository' if relative is 'true' then the resource in response will be 'repository'.  (optional)

try:
    # Get current user permissions.
    api_response = api_instance.get_current_user_permissions(x_request_id=x_request_id, scope=scope, relative=relative)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_current_user_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **scope** | **str**| The scope for the permission | [optional] 
 **relative** | **bool**| If true, the resources in the response are relative to the scope, eg for resource &#39;/project/1/repository&#39; if relative is &#39;true&#39; then the resource in response will be &#39;repository&#39;.  | [optional] 

### Return type

[**list[Permission]**](Permission.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResp get_user(user_id, x_request_id=x_request_id)

Get a user's profile.

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
api_instance = harbor_client.UserApi(harbor_client.ApiClient(configuration))
user_id = 56 # int | 
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get a user's profile.
    api_response = api_instance.get_user(user_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**UserResp**](UserResp.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> list[UserResp] list_users(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)

List users

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
api_instance = harbor_client.UserApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    # List users
    api_response = api_instance.list_users(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_users: %s\n" % e)
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

[**list[UserResp]**](UserResp.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> list[UserSearchRespItem] search_users(username, x_request_id=x_request_id, page=page, page_size=page_size)

Search users by username

This endpoint is to search the users by username.  It's open for all authenticated requests. 

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
api_instance = harbor_client.UserApi(harbor_client.ApiClient(configuration))
username = 'username_example' # str | Username for filtering results.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    # Search users by username
    api_response = api_instance.search_users(username, x_request_id=x_request_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for filtering results. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]

### Return type

[**list[UserSearchRespItem]**](UserSearchRespItem.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cli_secret**
> set_cli_secret(user_id, secret, x_request_id=x_request_id)

Set CLI secret for a user.

This endpoint let user generate a new CLI secret for himself.  This API only works when auth mode is set to 'OIDC'. Once this API returns with successful status, the old secret will be invalid, as there will be only one CLI secret for a user.

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
api_instance = harbor_client.UserApi(harbor_client.ApiClient(configuration))
user_id = 56 # int | User ID
secret = harbor_client.OIDCCliSecretReq() # OIDCCliSecretReq | 
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Set CLI secret for a user.
    api_instance.set_cli_secret(user_id, secret, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling UserApi->set_cli_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID | 
 **secret** | [**OIDCCliSecretReq**](OIDCCliSecretReq.md)|  | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_sys_admin**
> set_user_sys_admin(user_id, sysadmin_flag, x_request_id=x_request_id)

Update a registered user to change to be an administrator of Harbor.

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
api_instance = harbor_client.UserApi(harbor_client.ApiClient(configuration))
user_id = 56 # int | 
sysadmin_flag = harbor_client.UserSysAdminFlag() # UserSysAdminFlag | Toggle a user to admin or not.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update a registered user to change to be an administrator of Harbor.
    api_instance.set_user_sys_admin(user_id, sysadmin_flag, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling UserApi->set_user_sys_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **sysadmin_flag** | [**UserSysAdminFlag**](UserSysAdminFlag.md)| Toggle a user to admin or not. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_password**
> update_user_password(user_id, password, x_request_id=x_request_id)

Change the password on a user that already exists.

This endpoint is for user to update password. Users with the admin role can change any user's password. Regular users can change only their own password. 

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
api_instance = harbor_client.UserApi(harbor_client.ApiClient(configuration))
user_id = 56 # int | 
password = harbor_client.PasswordReq() # PasswordReq | Password to be updated, the attribute 'old_password' is optional when the API is called by the system administrator.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Change the password on a user that already exists.
    api_instance.update_user_password(user_id, password, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling UserApi->update_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **password** | [**PasswordReq**](PasswordReq.md)| Password to be updated, the attribute &#39;old_password&#39; is optional when the API is called by the system administrator. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_profile**
> update_user_profile(user_id, profile, x_request_id=x_request_id)

Update user's profile.

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
api_instance = harbor_client.UserApi(harbor_client.ApiClient(configuration))
user_id = 56 # int | Registered user ID
profile = harbor_client.UserProfile() # UserProfile | Only email, realname and comment can be modified.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update user's profile.
    api_instance.update_user_profile(user_id, profile, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling UserApi->update_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Registered user ID | 
 **profile** | [**UserProfile**](UserProfile.md)| Only email, realname and comment can be modified. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

