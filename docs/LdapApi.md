# harbor_client.LdapApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_ldap_user**](LdapApi.md#import_ldap_user) | **POST** /ldap/users/import | Import selected available ldap users.
[**ping_ldap**](LdapApi.md#ping_ldap) | **POST** /ldap/ping | Ping available ldap service.
[**search_ldap_group**](LdapApi.md#search_ldap_group) | **GET** /ldap/groups/search | Search available ldap groups.
[**search_ldap_user**](LdapApi.md#search_ldap_user) | **GET** /ldap/users/search | Search available ldap users.


# **import_ldap_user**
> import_ldap_user(ldap_import_users)

Import selected available ldap users.

This endpoint adds the selected available ldap users to harbor based on related configuration parameters from the system. System will try to guess the user email address and realname, add to harbor user information. If have errors when import user, will return the list of importing failed uid and the failed reason. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import ldap_api
from harbor_client.model.errors import Errors
from harbor_client.model.ldap_failed_import_user import LdapFailedImportUser
from harbor_client.model.ldap_import_users import LdapImportUsers
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
    api_instance = ldap_api.LdapApi(api_client)
    ldap_import_users = LdapImportUsers(
        ldap_uid_list=[
            "ldap_uid_list_example",
        ],
    ) # LdapImportUsers | The uid listed for importing. This list will check users validity of ldap service based on configuration from the system.

    # example passing only required values which don't have defaults set
    try:
        # Import selected available ldap users.
        api_instance.import_ldap_user(ldap_import_users)
    except harbor_client.ApiException as e:
        print("Exception when calling LdapApi->import_ldap_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_import_users** | [**LdapImportUsers**](LdapImportUsers.md)| The uid listed for importing. This list will check users validity of ldap service based on configuration from the system. |

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
**200** | Add ldap users successfully. |  -  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Failed import some users. |  -  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_ldap**
> LdapPingResult ping_ldap()

Ping available ldap service.

This endpoint ping the available ldap service for test related configuration parameters. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import ldap_api
from harbor_client.model.ldap_ping_result import LdapPingResult
from harbor_client.model.errors import Errors
from harbor_client.model.ldap_conf import LdapConf
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
    api_instance = ldap_api.LdapApi(api_client)
    ldap_conf = LdapConf(
        ldap_url="ldap_url_example",
        ldap_search_dn="ldap_search_dn_example",
        ldap_search_password="ldap_search_password_example",
        ldap_base_dn="ldap_base_dn_example",
        ldap_filter="ldap_filter_example",
        ldap_uid="ldap_uid_example",
        ldap_scope=1,
        ldap_connection_timeout=1,
        ldap_verify_cert=True,
    ) # LdapConf | ldap configuration. support input ldap service configuration. If it is a empty request, will load current configuration from the system. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ping available ldap service.
        api_response = api_instance.ping_ldap(ldap_conf=ldap_conf)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling LdapApi->ping_ldap: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_conf** | [**LdapConf**](LdapConf.md)| ldap configuration. support input ldap service configuration. If it is a empty request, will load current configuration from the system. | [optional]

### Return type

[**LdapPingResult**](LdapPingResult.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ping ldap service successfully. |  -  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ldap_group**
> [UserGroup] search_ldap_group()

Search available ldap groups.

This endpoint searches the available ldap groups based on related configuration parameters. support to search by groupname or groupdn. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import ldap_api
from harbor_client.model.user_group import UserGroup
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
    api_instance = ldap_api.LdapApi(api_client)
    groupname = "groupname_example" # str | Ldap group name (optional)
    groupdn = "groupdn_example" # str | The LDAP group DN (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search available ldap groups.
        api_response = api_instance.search_ldap_group(groupname=groupname, groupdn=groupdn)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling LdapApi->search_ldap_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupname** | **str**| Ldap group name | [optional]
 **groupdn** | **str**| The LDAP group DN | [optional]

### Return type

[**[UserGroup]**](UserGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search ldap group successfully. |  -  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ldap_user**
> [LdapUser] search_ldap_user()

Search available ldap users.

This endpoint searches the available ldap users based on related configuration parameters. Support searched by input ladp configuration, load configuration from the system and specific filter. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import ldap_api
from harbor_client.model.ldap_user import LdapUser
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
    api_instance = ldap_api.LdapApi(api_client)
    username = "username_example" # str | Registered user ID (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search available ldap users.
        api_response = api_instance.search_ldap_user(username=username)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling LdapApi->search_ldap_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Registered user ID | [optional]

### Return type

[**[LdapUser]**](LdapUser.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search ldap users successfully. |  -  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

