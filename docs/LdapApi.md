# harbor_client.LdapApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_ldap_user**](LdapApi.md#import_ldap_user) | **POST** /ldap/users/import | Import selected available ldap users.
[**ping_ldap**](LdapApi.md#ping_ldap) | **POST** /ldap/ping | Ping available ldap service.
[**search_ldap_group**](LdapApi.md#search_ldap_group) | **GET** /ldap/groups/search | Search available ldap groups.
[**search_ldap_user**](LdapApi.md#search_ldap_user) | **GET** /ldap/users/search | Search available ldap users.


# **import_ldap_user**
> import_ldap_user(uid_list, x_request_id=x_request_id)

Import selected available ldap users.

This endpoint adds the selected available ldap users to harbor based on related configuration parameters from the system. System will try to guess the user email address and realname, add to harbor user information. If have errors when import user, will return the list of importing failed uid and the failed reason. 

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
api_instance = harbor_client.LdapApi(harbor_client.ApiClient(configuration))
uid_list = harbor_client.LdapImportUsers() # LdapImportUsers | The uid listed for importing. This list will check users validity of ldap service based on configuration from the system.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Import selected available ldap users.
    api_instance.import_ldap_user(uid_list, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling LdapApi->import_ldap_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid_list** | [**LdapImportUsers**](LdapImportUsers.md)| The uid listed for importing. This list will check users validity of ldap service based on configuration from the system. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_ldap**
> LdapPingResult ping_ldap(x_request_id=x_request_id, ldapconf=ldapconf)

Ping available ldap service.

This endpoint ping the available ldap service for test related configuration parameters. 

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
api_instance = harbor_client.LdapApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
ldapconf = harbor_client.LdapConf() # LdapConf | ldap configuration. support input ldap service configuration. If it is a empty request, will load current configuration from the system. (optional)

try:
    # Ping available ldap service.
    api_response = api_instance.ping_ldap(x_request_id=x_request_id, ldapconf=ldapconf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LdapApi->ping_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **ldapconf** | [**LdapConf**](LdapConf.md)| ldap configuration. support input ldap service configuration. If it is a empty request, will load current configuration from the system. | [optional] 

### Return type

[**LdapPingResult**](LdapPingResult.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ldap_group**
> list[UserGroup] search_ldap_group(x_request_id=x_request_id, groupname=groupname, groupdn=groupdn)

Search available ldap groups.

This endpoint searches the available ldap groups based on related configuration parameters. support to search by groupname or groupdn. 

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
api_instance = harbor_client.LdapApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
groupname = 'groupname_example' # str | Ldap group name (optional)
groupdn = 'groupdn_example' # str | The LDAP group DN (optional)

try:
    # Search available ldap groups.
    api_response = api_instance.search_ldap_group(x_request_id=x_request_id, groupname=groupname, groupdn=groupdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LdapApi->search_ldap_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **groupname** | **str**| Ldap group name | [optional] 
 **groupdn** | **str**| The LDAP group DN | [optional] 

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ldap_user**
> list[LdapUser] search_ldap_user(x_request_id=x_request_id, username=username)

Search available ldap users.

This endpoint searches the available ldap users based on related configuration parameters. Support searched by input ladp configuration, load configuration from the system and specific filter. 

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
api_instance = harbor_client.LdapApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
username = 'username_example' # str | Registered user ID (optional)

try:
    # Search available ldap users.
    api_response = api_instance.search_ldap_user(x_request_id=x_request_id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LdapApi->search_ldap_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **username** | **str**| Registered user ID | [optional] 

### Return type

[**list[LdapUser]**](LdapUser.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

