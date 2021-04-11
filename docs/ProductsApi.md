# harbor_client.ProductsApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartrepo_repo_charts_name_version_labels_get**](ProductsApi.md#chartrepo_repo_charts_name_version_labels_get) | **GET** /chartrepo/{repo}/charts/{name}/{version}/labels | Return the attahced labels of chart.
[**chartrepo_repo_charts_name_version_labels_id_delete**](ProductsApi.md#chartrepo_repo_charts_name_version_labels_id_delete) | **DELETE** /chartrepo/{repo}/charts/{name}/{version}/labels/{id} | Remove label from chart.
[**chartrepo_repo_charts_name_version_labels_post**](ProductsApi.md#chartrepo_repo_charts_name_version_labels_post) | **POST** /chartrepo/{repo}/charts/{name}/{version}/labels | Mark label to chart.
[**configurations_get**](ProductsApi.md#configurations_get) | **GET** /configurations | Get system configurations.
[**configurations_put**](ProductsApi.md#configurations_put) | **PUT** /configurations | Modify system configurations.
[**email_ping_post**](ProductsApi.md#email_ping_post) | **POST** /email/ping | Test connection and authentication with email server.
[**health_get**](ProductsApi.md#health_get) | **GET** /health | Health check API
[**labels_get**](ProductsApi.md#labels_get) | **GET** /labels | List labels according to the query strings.
[**labels_id_delete**](ProductsApi.md#labels_id_delete) | **DELETE** /labels/{id} | Delete the label specified by ID.
[**labels_id_get**](ProductsApi.md#labels_id_get) | **GET** /labels/{id} | Get the label specified by ID.
[**labels_id_put**](ProductsApi.md#labels_id_put) | **PUT** /labels/{id} | Update the label properties.
[**labels_post**](ProductsApi.md#labels_post) | **POST** /labels | Post creates a label
[**projects_project_id_members_get**](ProductsApi.md#projects_project_id_members_get) | **GET** /projects/{project_id}/members | Get all project member information
[**projects_project_id_members_mid_delete**](ProductsApi.md#projects_project_id_members_mid_delete) | **DELETE** /projects/{project_id}/members/{mid} | Delete project member
[**projects_project_id_members_mid_get**](ProductsApi.md#projects_project_id_members_mid_get) | **GET** /projects/{project_id}/members/{mid} | Get the project member information
[**projects_project_id_members_mid_put**](ProductsApi.md#projects_project_id_members_mid_put) | **PUT** /projects/{project_id}/members/{mid} | Update project member
[**projects_project_id_members_post**](ProductsApi.md#projects_project_id_members_post) | **POST** /projects/{project_id}/members | Create project member
[**projects_project_id_metadatas_get**](ProductsApi.md#projects_project_id_metadatas_get) | **GET** /projects/{project_id}/metadatas | Get project metadata.
[**projects_project_id_metadatas_meta_name_delete**](ProductsApi.md#projects_project_id_metadatas_meta_name_delete) | **DELETE** /projects/{project_id}/metadatas/{meta_name} | Delete metadata of a project
[**projects_project_id_metadatas_meta_name_get**](ProductsApi.md#projects_project_id_metadatas_meta_name_get) | **GET** /projects/{project_id}/metadatas/{meta_name} | Get project metadata
[**projects_project_id_metadatas_meta_name_put**](ProductsApi.md#projects_project_id_metadatas_meta_name_put) | **PUT** /projects/{project_id}/metadatas/{meta_name} | Update metadata of a project.
[**projects_project_id_metadatas_post**](ProductsApi.md#projects_project_id_metadatas_post) | **POST** /projects/{project_id}/metadatas | Add metadata for the project.
[**statistics_get**](ProductsApi.md#statistics_get) | **GET** /statistics | Get projects number and repositories number relevant to the user
[**usergroups_get**](ProductsApi.md#usergroups_get) | **GET** /usergroups | Get all user groups information
[**usergroups_group_id_delete**](ProductsApi.md#usergroups_group_id_delete) | **DELETE** /usergroups/{group_id} | Delete user group
[**usergroups_group_id_get**](ProductsApi.md#usergroups_group_id_get) | **GET** /usergroups/{group_id} | Get user group information
[**usergroups_group_id_put**](ProductsApi.md#usergroups_group_id_put) | **PUT** /usergroups/{group_id} | Update group information
[**usergroups_post**](ProductsApi.md#usergroups_post) | **POST** /usergroups | Create user group
[**users_current_get**](ProductsApi.md#users_current_get) | **GET** /users/current | Get current user info.
[**users_current_permissions_get**](ProductsApi.md#users_current_permissions_get) | **GET** /users/current/permissions | Get current user permissions.
[**users_get**](ProductsApi.md#users_get) | **GET** /users | Get registered users of Harbor.
[**users_post**](ProductsApi.md#users_post) | **POST** /users | Creates a new user account.
[**users_search_get**](ProductsApi.md#users_search_get) | **GET** /users/search | Search users by username
[**users_user_id_cli_secret_put**](ProductsApi.md#users_user_id_cli_secret_put) | **PUT** /users/{user_id}/cli_secret | Set CLI secret for a user.
[**users_user_id_delete**](ProductsApi.md#users_user_id_delete) | **DELETE** /users/{user_id} | Mark a registered user as be removed.
[**users_user_id_get**](ProductsApi.md#users_user_id_get) | **GET** /users/{user_id} | Get a user&#39;s profile.
[**users_user_id_password_put**](ProductsApi.md#users_user_id_password_put) | **PUT** /users/{user_id}/password | Change the password on a user that already exists.
[**users_user_id_put**](ProductsApi.md#users_user_id_put) | **PUT** /users/{user_id} | Update a registered user to change his profile.
[**users_user_id_sysadmin_put**](ProductsApi.md#users_user_id_sysadmin_put) | **PUT** /users/{user_id}/sysadmin | Update a registered user to change to be an administrator of Harbor.


# **chartrepo_repo_charts_name_version_labels_get**
> chartrepo_repo_charts_name_version_labels_get(repo, name, version)

Return the attahced labels of chart.

Return the attahced labels of the specified chart version.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    repo = "repo_example" # str | The project name
    name = "name_example" # str | The chart name
    version = "version_example" # str | The chart version

    # example passing only required values which don't have defaults set
    try:
        # Return the attahced labels of chart.
        api_instance.chartrepo_repo_charts_name_version_labels_get(repo, name, version)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->chartrepo_repo_charts_name_version_labels_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name |
 **name** | **str**| The chart name |
 **version** | **str**| The chart version |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_version_labels_id_delete**
> chartrepo_repo_charts_name_version_labels_id_delete(repo, name, version, id)

Remove label from chart.

Remove label from the specified chart version.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    repo = "repo_example" # str | The project name
    name = "name_example" # str | The chart name
    version = "version_example" # str | The chart version
    id = 1 # int | The label ID

    # example passing only required values which don't have defaults set
    try:
        # Remove label from chart.
        api_instance.chartrepo_repo_charts_name_version_labels_id_delete(repo, name, version, id)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->chartrepo_repo_charts_name_version_labels_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name |
 **name** | **str**| The chart name |
 **version** | **str**| The chart version |
 **id** | **int**| The label ID |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The label is successfully unmarked from the chart version. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_version_labels_post**
> chartrepo_repo_charts_name_version_labels_post(repo, name, version, label)

Mark label to chart.

Mark label to the specified chart version.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.label import Label
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
    api_instance = products_api.ProductsApi(api_client)
    repo = "repo_example" # str | The project name
    name = "name_example" # str | The chart name
    version = "version_example" # str | The chart version
    label = Label(
        id=1,
        name="name_example",
        description="description_example",
        color="color_example",
        scope="scope_example",
        project_id=1,
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Label | The label being marked to the chart version

    # example passing only required values which don't have defaults set
    try:
        # Mark label to chart.
        api_instance.chartrepo_repo_charts_name_version_labels_post(repo, name, version, label)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->chartrepo_repo_charts_name_version_labels_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name |
 **name** | **str**| The chart name |
 **version** | **str**| The chart version |
 **label** | [**Label**](Label.md)| The label being marked to the chart version |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The label is successfully marked to the chart version. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurations_get**
> ConfigurationsResponse configurations_get()

Get system configurations.

This endpoint is for retrieving system configurations that only provides for admin user. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.configurations_response import ConfigurationsResponse
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
    api_instance = products_api.ProductsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get system configurations.
        api_response = api_instance.configurations_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->configurations_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationsResponse**](ConfigurationsResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get system configurations successfully. The response body is a map. |  -  |
**401** | User need to log in first.ß |  -  |
**403** | User does not have permission of admin role. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurations_put**
> configurations_put(configurations)

Modify system configurations.

This endpoint is for modifying system configurations that only provides for admin user. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.configurations import Configurations
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
    api_instance = products_api.ProductsApi(api_client)
    configurations = Configurations(
        auth_mode="auth_mode_example",
        count_per_project="count_per_project_example",
        email_from="email_from_example",
        email_host="email_host_example",
        email_port=1,
        email_identity="email_identity_example",
        email_username="email_username_example",
        email_ssl=True,
        email_insecure=True,
        ldap_url="ldap_url_example",
        ldap_base_dn="ldap_base_dn_example",
        ldap_filter="ldap_filter_example",
        ldap_scope=1,
        ldap_uid="ldap_uid_example",
        ldap_search_dn="ldap_search_dn_example",
        ldap_timeout=1,
        ldap_group_attribute_name="ldap_group_attribute_name_example",
        ldap_group_base_dn="ldap_group_base_dn_example",
        ldap_group_search_filter="ldap_group_search_filter_example",
        ldap_group_search_scope=1,
        ldap_group_admin_dn="ldap_group_admin_dn_example",
        oidc_client_id="oidc_client_id_example",
        oidc_client_secret="oidc_client_secret_example",
        oidc_endpoint="oidc_endpoint_example",
        oidc_name="oidc_name_example",
        oidc_scope="oidc_scope_example",
        oidc_verify_cert=True,
        project_creation_restriction="project_creation_restriction_example",
        quota_per_project_enable=True,
        read_only=True,
        self_registration=True,
        storage_per_project="storage_per_project_example",
        token_expiration=1,
        verify_remote_cert=True,
        scan_all_policy=ConfigurationsScanAllPolicy(
            type="type_example",
            parameter=ConfigurationsScanAllPolicyParameter(
                daily_time=1,
            ),
        ),
    ) # Configurations | The configuration map can contain a subset of the attributes of the schema, which are to be updated.

    # example passing only required values which don't have defaults set
    try:
        # Modify system configurations.
        api_instance.configurations_put(configurations)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->configurations_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configurations** | [**Configurations**](Configurations.md)| The configuration map can contain a subset of the attributes of the schema, which are to be updated. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modify system configurations successfully. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission of admin role. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_ping_post**
> email_ping_post()

Test connection and authentication with email server.

Test connection and authentication with email server. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.email_server_setting import EmailServerSetting
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
    api_instance = products_api.ProductsApi(api_client)
    email_server_setting = EmailServerSetting(
        email_host="email_host_example",
        email_port=1,
        email_username="email_username_example",
        email_password="email_password_example",
        email_ssl=True,
        email_identity="email_identity_example",
    ) # EmailServerSetting | Email server settings, if some of the settings are not assigned, they will be read from system configuration. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Test connection and authentication with email server.
        api_instance.email_ping_post(email_server_setting=email_server_setting)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->email_ping_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_server_setting** | [**EmailServerSetting**](EmailServerSetting.md)| Email server settings, if some of the settings are not assigned, they will be read from system configuration. | [optional]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ping email server successfully. |  -  |
**400** | Inviald email server settings. |  -  |
**401** | User need to login first. |  -  |
**403** | Only admin has this authority. |  -  |
**415** |  |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_get**
> OverallHealthStatus health_get()

Health check API

The endpoint returns the health stauts of the system. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.overall_health_status import OverallHealthStatus
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
    api_instance = products_api.ProductsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Health check API
        api_response = api_instance.health_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->health_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OverallHealthStatus**](OverallHealthStatus.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The system health status. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_get**
> [Label] labels_get(scope)

List labels according to the query strings.

This endpoint let user list labels by name, scope and project_id 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.label import Label
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
    api_instance = products_api.ProductsApi(api_client)
    scope = "scope_example" # str | The label scope. Valid values are g and p. g for global labels and p for project labels.
    name = "name_example" # str | The label name. (optional)
    project_id = 1 # int | Relevant project ID, required when scope is p. (optional)
    page = 1 # int | The page number. (optional)
    page_size = 1 # int | The size of per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List labels according to the query strings.
        api_response = api_instance.labels_get(scope)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->labels_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List labels according to the query strings.
        api_response = api_instance.labels_get(scope, name=name, project_id=project_id, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->labels_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The label scope. Valid values are g and p. g for global labels and p for project labels. |
 **name** | **str**| The label name. | [optional]
 **project_id** | **int**| Relevant project ID, required when scope is p. | [optional]
 **page** | **int**| The page number. | [optional]
 **page_size** | **int**| The size of per page. | [optional]

### Return type

[**[Label]**](Label.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get successfully. |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
**400** | Invalid parameters. |  -  |
**401** | User need to log in first. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_delete**
> labels_id_delete(id)

Delete the label specified by ID.

Delete the label specified by ID. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | Label ID

    # example passing only required values which don't have defaults set
    try:
        # Delete the label specified by ID.
        api_instance.labels_id_delete(id)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->labels_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Label ID |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete successfully. |  -  |
**400** | Invalid parameters. |  -  |
**401** | User need to log in first. |  -  |
**404** | The resource does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_get**
> Label labels_id_get(id)

Get the label specified by ID.

This endpoint let user get the label by specific ID. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.label import Label
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
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | Label ID

    # example passing only required values which don't have defaults set
    try:
        # Get the label specified by ID.
        api_response = api_instance.labels_id_get(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->labels_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Label ID |

### Return type

[**Label**](Label.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get successfully. |  -  |
**401** | User need to log in first. |  -  |
**404** | The resource does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_put**
> labels_id_put(id, label)

Update the label properties.

This endpoint let user update label properties. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.label import Label
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
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | Label ID
    label = Label(
        id=1,
        name="name_example",
        description="description_example",
        color="color_example",
        scope="scope_example",
        project_id=1,
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Label | The updated label json object.

    # example passing only required values which don't have defaults set
    try:
        # Update the label properties.
        api_instance.labels_id_put(id, label)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->labels_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Label ID |
 **label** | [**Label**](Label.md)| The updated label json object. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update successfully. |  -  |
**400** | Invalid parameters. |  -  |
**401** | User need to log in first. |  -  |
**404** | The resource does not exist. |  -  |
**409** | The label with the same name already exists. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_post**
> labels_post(label)

Post creates a label

This endpoint let user creates a label. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.label import Label
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
    api_instance = products_api.ProductsApi(api_client)
    label = Label(
        id=1,
        name="name_example",
        description="description_example",
        color="color_example",
        scope="scope_example",
        project_id=1,
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Label | The json object of label.

    # example passing only required values which don't have defaults set
    try:
        # Post creates a label
        api_instance.labels_post(label)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->labels_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | [**Label**](Label.md)| The json object of label. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create successfully. |  * Location - The URL of the created resource <br>  |
**400** | Invalid parameters. |  -  |
**401** | User need to log in first. |  -  |
**409** | Label with the same name and same scope already exists. |  -  |
**415** |  |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_get**
> [ProjectMemberEntity] projects_project_id_members_get(project_id)

Get all project member information

Get all project member information

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.project_member_entity import ProjectMemberEntity
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
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    entityname = "entityname_example" # str | The entity name to search. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all project member information
        api_response = api_instance.projects_project_id_members_get(project_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_members_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all project member information
        api_response = api_instance.projects_project_id_members_get(project_id, entityname=entityname)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_members_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **entityname** | **str**| The entity name to search. | [optional]

### Return type

[**[ProjectMemberEntity]**](ProjectMemberEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get project members successfully. |  -  |
**400** | The project id is invalid. |  -  |
**401** | User need to log in first. |  -  |
**403** | User in session does not have permission to the project. |  -  |
**404** | Project ID does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_mid_delete**
> projects_project_id_members_mid_delete(project_id, mid)

Delete project member

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    mid = 1 # int | Member ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete project member
        api_instance.projects_project_id_members_mid_delete(project_id, mid)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_members_mid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **mid** | **int**| Member ID. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project member deleted successfully. |  -  |
**400** | The project id or project member id is invalid. |  -  |
**401** | User need to log in first. |  -  |
**403** | User in session does not have permission to the project. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_mid_get**
> ProjectMemberEntity projects_project_id_members_mid_get(project_id, mid)

Get the project member information

Get the project member information

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.project_member_entity import ProjectMemberEntity
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
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    mid = 1 # int | The member ID

    # example passing only required values which don't have defaults set
    try:
        # Get the project member information
        api_response = api_instance.projects_project_id_members_mid_get(project_id, mid)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_members_mid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **mid** | **int**| The member ID |

### Return type

[**ProjectMemberEntity**](ProjectMemberEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project member retrieved successfully. |  -  |
**400** | Illegal format of project member or invalid project id, member id. |  -  |
**401** | User need to log in first. |  -  |
**403** | User in session does not have permission to the project. |  -  |
**404** | Project or projet member does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_mid_put**
> projects_project_id_members_mid_put(project_id, mid)

Update project member

Update project member relationship

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.role_request import RoleRequest
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
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    mid = 1 # int | Member ID.
    role_request = RoleRequest(
        role_id=1,
    ) # RoleRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update project member
        api_instance.projects_project_id_members_mid_put(project_id, mid)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_members_mid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update project member
        api_instance.projects_project_id_members_mid_put(project_id, mid, role_request=role_request)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_members_mid_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **mid** | **int**| Member ID. |
 **role_request** | [**RoleRequest**](RoleRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project member updated successfully. |  -  |
**400** | Invalid role id, it should be 1,2 or 3, or invalid project id, or invalid member id. |  -  |
**401** | User need to log in first. |  -  |
**403** | User in session does not have permission to the project. |  -  |
**404** | project or project member does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_post**
> projects_project_id_members_post(project_id)

Create project member

Create project member relationship, the member can be one of the user_member and group_member,  The user_member need to specify user_id or username. If the user already exist in harbor DB, specify the user_id,  If does not exist in harbor DB, it will SearchAndOnBoard the user. The group_member need to specify id or ldap_group_dn. If the group already exist in harbor DB. specify the user group's id,  If does not exist, it will SearchAndOnBoard the group.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.project_member import ProjectMember
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
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    project_member = ProjectMember(
        role_id=1,
        member_user=UserEntity(
            user_id=1,
            username="username_example",
        ),
        member_group=UserGroup(
            id=1,
            group_name="group_name_example",
            group_type=1,
            ldap_group_dn="ldap_group_dn_example",
        ),
    ) # ProjectMember |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create project member
        api_instance.projects_project_id_members_post(project_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_members_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create project member
        api_instance.projects_project_id_members_post(project_id, project_member=project_member)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_members_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **project_member** | [**ProjectMember**](ProjectMember.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Project member created successfully. |  * Location - The URL of the created resource <br>  |
**400** | Illegal format of project member or project id is invalid, or LDAP DN is invalid. |  -  |
**401** | User need to log in first. |  -  |
**403** | User in session does not have permission to the project. |  -  |
**409** | A user group with same group name already exist or an LDAP user group with same DN already exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_metadatas_get**
> ProjectMetadata projects_project_id_metadatas_get(project_id)

Get project metadata.

This endpoint returns metadata of the project specified by project ID. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.project_metadata import ProjectMetadata
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
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | The ID of project.

    # example passing only required values which don't have defaults set
    try:
        # Get project metadata.
        api_response = api_instance.projects_project_id_metadatas_get(project_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_metadatas_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of project. |

### Return type

[**ProjectMetadata**](ProjectMetadata.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get metadata successfully. |  -  |
**401** | User need to login first. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_metadatas_meta_name_delete**
> projects_project_id_metadatas_meta_name_delete(project_id, meta_name)

Delete metadata of a project

This endpoint is aimed to delete metadata of a project. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | The ID of project.
    meta_name = "meta_name_example" # str | The name of metadat.

    # example passing only required values which don't have defaults set
    try:
        # Delete metadata of a project
        api_instance.projects_project_id_metadatas_meta_name_delete(project_id, meta_name)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_metadatas_meta_name_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of project. |
 **meta_name** | **str**| The name of metadat. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata is deleted successfully. |  -  |
**400** | Invalid requst. |  -  |
**403** | User need to log in first. |  -  |
**404** | Project or metadata does not exist. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_metadatas_meta_name_get**
> ProjectMetadata projects_project_id_metadatas_meta_name_get(project_id, meta_name)

Get project metadata

This endpoint returns specified metadata of a project. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.project_metadata import ProjectMetadata
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
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Project ID for filtering results.
    meta_name = "meta_name_example" # str | The name of metadat.

    # example passing only required values which don't have defaults set
    try:
        # Get project metadata
        api_response = api_instance.projects_project_id_metadatas_meta_name_get(project_id, meta_name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_metadatas_meta_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID for filtering results. |
 **meta_name** | **str**| The name of metadat. |

### Return type

[**ProjectMetadata**](ProjectMetadata.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get metadata successfully. |  -  |
**401** | User need to log in first. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_metadatas_meta_name_put**
> projects_project_id_metadatas_meta_name_put(project_id, meta_name)

Update metadata of a project.

This endpoint is aimed to update the metadata of a project. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | The ID of project.
    meta_name = "meta_name_example" # str | The name of metadat.

    # example passing only required values which don't have defaults set
    try:
        # Update metadata of a project.
        api_instance.projects_project_id_metadatas_meta_name_put(project_id, meta_name)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_metadatas_meta_name_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of project. |
 **meta_name** | **str**| The name of metadat. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated metadata successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission to the project. |  -  |
**404** | Project or metadata does not exist. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_metadatas_post**
> projects_project_id_metadatas_post(project_id, project_metadata)

Add metadata for the project.

This endpoint is aimed to add metadata of a project. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.project_metadata import ProjectMetadata
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
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Selected project ID.
    project_metadata = ProjectMetadata(
        public="public_example",
        enable_content_trust="enable_content_trust_example",
        prevent_vul="prevent_vul_example",
        severity="severity_example",
        auto_scan="auto_scan_example",
        reuse_sys_cve_allowlist="reuse_sys_cve_allowlist_example",
        retention_id="retention_id_example",
    ) # ProjectMetadata | The metadata of project.

    # example passing only required values which don't have defaults set
    try:
        # Add metadata for the project.
        api_instance.projects_project_id_metadatas_post(project_id, project_metadata)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_metadatas_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Selected project ID. |
 **project_metadata** | [**ProjectMetadata**](ProjectMetadata.md)| The metadata of project. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add metadata successfully. |  -  |
**400** | Invalid request. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission to the project. |  -  |
**404** | Project ID does not exist. |  -  |
**415** |  |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_get**
> StatisticMap statistics_get()

Get projects number and repositories number relevant to the user

This endpoint is aimed to statistic all of the projects number and repositories number relevant to the logined user, also the public projects number and repositories number. If the user is admin, he can also get total projects number and total repositories number. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.statistic_map import StatisticMap
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
    api_instance = products_api.ProductsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get projects number and repositories number relevant to the user
        api_response = api_instance.statistics_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->statistics_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**StatisticMap**](StatisticMap.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the projects number and repositories number relevant to the user successfully. |  -  |
**401** | User need to log in first. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_get**
> [UserGroup] usergroups_get()

Get all user groups information

Get all user groups information

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.user_group import UserGroup
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
    api_instance = products_api.ProductsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all user groups information
        api_response = api_instance.usergroups_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->usergroups_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[UserGroup]**](UserGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get user group successfully. |  -  |
**401** | User need to log in first. |  -  |
**403** | User in session does not have permission to the user group. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_group_id_delete**
> usergroups_group_id_delete(group_id)

Delete user group

Delete user group

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    group_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete user group
        api_instance.usergroups_group_id_delete(group_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->usergroups_group_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User group deleted successfully. |  -  |
**400** | The user group id is invalid. |  -  |
**401** | User need to log in first. |  -  |
**403** | Only admin has this authority. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_group_id_get**
> UserGroup usergroups_group_id_get(group_id)

Get user group information

Get user group information

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.user_group import UserGroup
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
    api_instance = products_api.ProductsApi(api_client)
    group_id = 1 # int | Group ID

    # example passing only required values which don't have defaults set
    try:
        # Get user group information
        api_response = api_instance.usergroups_group_id_get(group_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->usergroups_group_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID |

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User group get successfully. |  -  |
**400** | The user group id is invalid. |  -  |
**401** | User need to log in first. |  -  |
**403** | User in session does not have permission to the user group. |  -  |
**404** | User group does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_group_id_put**
> usergroups_group_id_put(group_id)

Update group information

Update user group information

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.user_group import UserGroup
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
    api_instance = products_api.ProductsApi(api_client)
    group_id = 1 # int | Group ID
    user_group = UserGroup(
        id=1,
        group_name="group_name_example",
        group_type=1,
        ldap_group_dn="ldap_group_dn_example",
    ) # UserGroup |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update group information
        api_instance.usergroups_group_id_put(group_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->usergroups_group_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update group information
        api_instance.usergroups_group_id_put(group_id, user_group=user_group)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->usergroups_group_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID |
 **user_group** | [**UserGroup**](UserGroup.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User group updated successfully. |  -  |
**400** | The user group id is invalid. |  -  |
**401** | User need to log in first. |  -  |
**403** | Only admin has this authority. |  -  |
**404** | User group does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_post**
> usergroups_post()

Create user group

Create user group information

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.user_group import UserGroup
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
    api_instance = products_api.ProductsApi(api_client)
    user_group = UserGroup(
        id=1,
        group_name="group_name_example",
        group_type=1,
        ldap_group_dn="ldap_group_dn_example",
    ) # UserGroup |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create user group
        api_instance.usergroups_post(user_group=user_group)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->usergroups_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group** | [**UserGroup**](UserGroup.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User group created successfully. |  * Location - The URL of the created resource <br>  |
**400** | Invalid LDAP group DN. |  -  |
**401** | User need to log in first. |  -  |
**403** | User in session does not have permission to the user group. |  -  |
**409** | A user group with same group name already exist, or an LDAP user group with same DN already exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_current_get**
> User users_current_get()

Get current user info.

This endpoint is to get the current user information. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.user import User
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
    api_instance = products_api.ProductsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current user info.
        api_response = api_instance.users_current_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_current_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get current user information successfully. |  -  |
**401** | User need to log in first. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_current_permissions_get**
> [Permission] users_current_permissions_get()

Get current user permissions.

This endpoint is to get the current user permissions. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.permission import Permission
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
    api_instance = products_api.ProductsApi(api_client)
    scope = "scope_example" # str | Get permissions of the scope (optional)
    relative = True # bool | If true, the resources in the response are relative to the scope, eg for resource '/project/1/repository' if relative is 'true' then the resource in response will be 'repository'.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get current user permissions.
        api_response = api_instance.users_current_permissions_get(scope=scope, relative=relative)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_current_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Get permissions of the scope | [optional]
 **relative** | **bool**| If true, the resources in the response are relative to the scope, eg for resource &#39;/project/1/repository&#39; if relative is &#39;true&#39; then the resource in response will be &#39;repository&#39;.  | [optional]

### Return type

[**[Permission]**](Permission.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get current user permission successfully. |  -  |
**401** | User need to log in first. |  -  |
**500** | Internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> [User] users_get()

Get registered users of Harbor.

This endpoint is for user to search registered users, support for filtering results with username.Notice, by now this operation is only for administrator. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.user import User
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
    api_instance = products_api.ProductsApi(api_client)
    username = "username_example" # str | Username for filtering results. (optional)
    email = "email_example" # str | Email for filtering results. (optional)
    page = 1 # int | The page number, default is 1. (optional)
    page_size = 1 # int | The size of per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get registered users of Harbor.
        api_response = api_instance.users_get(username=username, email=email, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for filtering results. | [optional]
 **email** | **str**| Email for filtering results. | [optional]
 **page** | **int**| The page number, default is 1. | [optional]
 **page_size** | **int**| The size of per page. | [optional]

### Return type

[**[User]**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Searched for users of Harbor successfully. |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
**400** | Invalid user ID. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission of admin role. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> users_post(user)

Creates a new user account.

This endpoint is to create a user if the user does not already exist. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.user import User
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
    api_instance = products_api.ProductsApi(api_client)
    user = User(
        user_id=1,
        username="username_example",
        email="email_example",
        password="password_example",
        realname="realname_example",
        comment="comment_example",
        deleted=True,
        role_name="role_name_example",
        role_id=1,
        sysadmin_flag=True,
        admin_role_in_auth=True,
        reset_uuid="reset_uuid_example",
        salt="salt_example",
        creation_time="creation_time_example",
        update_time="update_time_example",
    ) # User | New created user.

    # example passing only required values which don't have defaults set
    try:
        # Creates a new user account.
        api_instance.users_post(user)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| New created user. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User created successfully. |  * Location - The URL of the created resource <br>  |
**400** | Unsatisfied with constraints of the user creation. |  -  |
**403** | User registration can only be used by admin role user when self-registration is off. |  -  |
**415** |  |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_search_get**
> [UserSearch] users_search_get(username)

Search users by username

This endpoint is to search the users by username. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.user_search import UserSearch
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
    api_instance = products_api.ProductsApi(api_client)
    username = "username_example" # str | Username for filtering results.
    page = 1 # int | The page number, default is 1. (optional)
    page_size = 1 # int | The size of per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search users by username
        api_response = api_instance.users_search_get(username)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_search_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search users by username
        api_response = api_instance.users_search_get(username, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for filtering results. |
 **page** | **int**| The page number, default is 1. | [optional]
 **page_size** | **int**| The size of per page. | [optional]

### Return type

[**[UserSearch]**](UserSearch.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search users by username, email successfully. |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_cli_secret_put**
> users_user_id_cli_secret_put(user_id, inline_object)

Set CLI secret for a user.

This endpoint let user generate a new CLI secret for himself.  This API only works when auth mode is set to 'OIDC'. Once this API returns with successful status, the old secret will be invalid, as there will be only one CLI secret for a user. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.inline_object import InlineObject
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
    api_instance = products_api.ProductsApi(api_client)
    user_id = 1 # int | User ID
    inline_object = InlineObject(
        secret="secret_example",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Set CLI secret for a user.
        api_instance.users_user_id_cli_secret_put(user_id, inline_object)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_user_id_cli_secret_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID |
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The secret is successfully updated |  -  |
**400** | Invalid user ID.  Or user is not onboarded via OIDC authentication. Or the secret does not meet the standard. |  -  |
**401** | User need to log in first. |  -  |
**403** | Non-admin user can only generate the cli secret of himself. |  -  |
**404** | User ID does not exist. |  -  |
**412** | The auth mode of the system is not \&quot;oidc_auth\&quot;, or the user is not onboarded via OIDC AuthN. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_delete**
> users_user_id_delete(user_id)

Mark a registered user as be removed.

This endpoint let administrator of Harbor mark a registered user as be removed.It actually won't be deleted from DB. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    user_id = 1 # int | User ID for marking as to be removed.

    # example passing only required values which don't have defaults set
    try:
        # Mark a registered user as be removed.
        api_instance.users_user_id_delete(user_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_user_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID for marking as to be removed. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marked user as be removed successfully. |  -  |
**400** | Invalid user ID. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission of admin role. |  -  |
**404** | User ID does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_get**
> User users_user_id_get(user_id)

Get a user's profile.

Get user's profile with user id. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.user import User
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
    api_instance = products_api.ProductsApi(api_client)
    user_id = 1 # int | Registered user ID

    # example passing only required values which don't have defaults set
    try:
        # Get a user's profile.
        api_response = api_instance.users_user_id_get(user_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_user_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Registered user ID |

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get user&#39;s profile successfully. |  -  |
**400** | Invalid user ID. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission of admin role. |  -  |
**404** | User ID does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_password_put**
> users_user_id_password_put(user_id, password)

Change the password on a user that already exists.

This endpoint is for user to update password. Users with the admin role can change any user's password. Guest users can change only their own password. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.password import Password
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
    api_instance = products_api.ProductsApi(api_client)
    user_id = 1 # int | Registered user ID.
    password = Password(
        old_password="old_password_example",
        new_password="new_password_example",
    ) # Password | Password to be updated, the attribute 'old_password' is optional when the API is called by the system administrator.

    # example passing only required values which don't have defaults set
    try:
        # Change the password on a user that already exists.
        api_instance.users_user_id_password_put(user_id, password)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_user_id_password_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Registered user ID. |
 **password** | [**Password**](Password.md)| Password to be updated, the attribute &#39;old_password&#39; is optional when the API is called by the system administrator. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated password successfully. |  -  |
**400** | Invalid user ID; Old password is blank; New password is blank. |  -  |
**401** | Don&#39;t have authority to change password. Please check login status. |  -  |
**403** | The caller does not have permission to update the password of the user with given ID, or the old password in request body is not correct. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_put**
> users_user_id_put(user_id, user_profile)

Update a registered user to change his profile.

This endpoint let a registered user change his profile. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.user_profile import UserProfile
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
    api_instance = products_api.ProductsApi(api_client)
    user_id = 1 # int | Registered user ID
    user_profile = UserProfile(
        email="email_example",
        realname="realname_example",
        comment="comment_example",
    ) # UserProfile | Only email, realname and comment can be modified.

    # example passing only required values which don't have defaults set
    try:
        # Update a registered user to change his profile.
        api_instance.users_user_id_put(user_id, user_profile)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_user_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Registered user ID |
 **user_profile** | [**UserProfile**](UserProfile.md)| Only email, realname and comment can be modified. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user&#39;s profile successfully. |  -  |
**400** | Invalid user ID. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission of admin role. |  -  |
**404** | User ID does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_sysadmin_put**
> users_user_id_sysadmin_put(user_id, sys_admin_flag)

Update a registered user to change to be an administrator of Harbor.

This endpoint let a registered user change to be an administrator of Harbor. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.sys_admin_flag import SysAdminFlag
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
    api_instance = products_api.ProductsApi(api_client)
    user_id = 1 # int | Registered user ID
    sys_admin_flag = SysAdminFlag(
        sysadmin_flag=True,
    ) # SysAdminFlag | Toggle a user to admin or not.

    # example passing only required values which don't have defaults set
    try:
        # Update a registered user to change to be an administrator of Harbor.
        api_instance.users_user_id_sysadmin_put(user_id, sys_admin_flag)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->users_user_id_sysadmin_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Registered user ID |
 **sys_admin_flag** | [**SysAdminFlag**](SysAdminFlag.md)| Toggle a user to admin or not. |

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user&#39;s admin role successfully. |  -  |
**400** | Invalid user ID. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission of admin role. |  -  |
**404** | User ID does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

