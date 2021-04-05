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
[**ldap_groups_search_get**](ProductsApi.md#ldap_groups_search_get) | **GET** /ldap/groups/search | Search available ldap groups.
[**ldap_ping_post**](ProductsApi.md#ldap_ping_post) | **POST** /ldap/ping | Ping available ldap service.
[**ldap_users_import_post**](ProductsApi.md#ldap_users_import_post) | **POST** /ldap/users/import | Import selected available ldap users.
[**ldap_users_search_get**](ProductsApi.md#ldap_users_search_get) | **GET** /ldap/users/search | Search available ldap users.
[**projects_project_id_immutabletagrules_get**](ProductsApi.md#projects_project_id_immutabletagrules_get) | **GET** /projects/{project_id}/immutabletagrules | List all immutable tag rules of current project
[**projects_project_id_immutabletagrules_id_delete**](ProductsApi.md#projects_project_id_immutabletagrules_id_delete) | **DELETE** /projects/{project_id}/immutabletagrules/{id} | Delete the immutable tag rule.
[**projects_project_id_immutabletagrules_id_put**](ProductsApi.md#projects_project_id_immutabletagrules_id_put) | **PUT** /projects/{project_id}/immutabletagrules/{id} | Update the immutable tag rule or enable or disable the rule
[**projects_project_id_immutabletagrules_post**](ProductsApi.md#projects_project_id_immutabletagrules_post) | **POST** /projects/{project_id}/immutabletagrules | Add an immutable tag rule to current project
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
[**projects_project_id_scanner_candidates_get**](ProductsApi.md#projects_project_id_scanner_candidates_get) | **GET** /projects/{project_id}/scanner/candidates | Get scanner registration candidates for configurating project level scanner
[**projects_project_id_scanner_get**](ProductsApi.md#projects_project_id_scanner_get) | **GET** /projects/{project_id}/scanner | Get project level scanner
[**projects_project_id_webhook_events_get**](ProductsApi.md#projects_project_id_webhook_events_get) | **GET** /projects/{project_id}/webhook/events | Get supported event types and notify types.
[**projects_project_id_webhook_jobs_get**](ProductsApi.md#projects_project_id_webhook_jobs_get) | **GET** /projects/{project_id}/webhook/jobs | List project webhook jobs
[**projects_project_id_webhook_lasttrigger_get**](ProductsApi.md#projects_project_id_webhook_lasttrigger_get) | **GET** /projects/{project_id}/webhook/lasttrigger | Get project webhook policy last trigger info
[**projects_project_id_webhook_policies_get**](ProductsApi.md#projects_project_id_webhook_policies_get) | **GET** /projects/{project_id}/webhook/policies | List project webhook policies.
[**projects_project_id_webhook_policies_policy_id_delete**](ProductsApi.md#projects_project_id_webhook_policies_policy_id_delete) | **DELETE** /projects/{project_id}/webhook/policies/{policy_id} | Delete webhook policy of a project
[**projects_project_id_webhook_policies_policy_id_get**](ProductsApi.md#projects_project_id_webhook_policies_policy_id_get) | **GET** /projects/{project_id}/webhook/policies/{policy_id} | Get project webhook policy
[**projects_project_id_webhook_policies_policy_id_put**](ProductsApi.md#projects_project_id_webhook_policies_policy_id_put) | **PUT** /projects/{project_id}/webhook/policies/{policy_id} | Update webhook policy of a project.
[**projects_project_id_webhook_policies_post**](ProductsApi.md#projects_project_id_webhook_policies_post) | **POST** /projects/{project_id}/webhook/policies | Create project webhook policy.
[**projects_project_id_webhook_policies_test_post**](ProductsApi.md#projects_project_id_webhook_policies_test_post) | **POST** /projects/{project_id}/webhook/policies/test | Test project webhook connection
[**quotas_get**](ProductsApi.md#quotas_get) | **GET** /quotas | List quotas
[**quotas_id_get**](ProductsApi.md#quotas_id_get) | **GET** /quotas/{id} | Get the specified quota
[**quotas_id_put**](ProductsApi.md#quotas_id_put) | **PUT** /quotas/{id} | Update the specified quota
[**registries_get**](ProductsApi.md#registries_get) | **GET** /registries | List registries.
[**registries_id_delete**](ProductsApi.md#registries_id_delete) | **DELETE** /registries/{id} | Delete specific registry.
[**registries_id_get**](ProductsApi.md#registries_id_get) | **GET** /registries/{id} | Get registry.
[**registries_id_info_get**](ProductsApi.md#registries_id_info_get) | **GET** /registries/{id}/info | Get registry info.
[**registries_id_namespace_get**](ProductsApi.md#registries_id_namespace_get) | **GET** /registries/{id}/namespace | List namespaces of registry
[**registries_id_put**](ProductsApi.md#registries_id_put) | **PUT** /registries/{id} | Update a given registry.
[**registries_ping_post**](ProductsApi.md#registries_ping_post) | **POST** /registries/ping | Ping status of a registry.
[**registries_post**](ProductsApi.md#registries_post) | **POST** /registries | Create a new registry.
[**replication_adapters_get**](ProductsApi.md#replication_adapters_get) | **GET** /replication/adapters | List supported adapters.
[**replication_policies_get**](ProductsApi.md#replication_policies_get) | **GET** /replication/policies | List replication policies
[**replication_policies_id_delete**](ProductsApi.md#replication_policies_id_delete) | **DELETE** /replication/policies/{id} | Delete the replication policy specified by ID.
[**replication_policies_id_get**](ProductsApi.md#replication_policies_id_get) | **GET** /replication/policies/{id} | Get replication policy.
[**replication_policies_id_put**](ProductsApi.md#replication_policies_id_put) | **PUT** /replication/policies/{id} | Update the replication policy
[**replication_policies_post**](ProductsApi.md#replication_policies_post) | **POST** /replication/policies | Create a replication policy
[**scanners_get**](ProductsApi.md#scanners_get) | **GET** /scanners | List scanner registrations
[**scanners_ping_post**](ProductsApi.md#scanners_ping_post) | **POST** /scanners/ping | Tests scanner registration settings
[**scanners_registration_id_get**](ProductsApi.md#scanners_registration_id_get) | **GET** /scanners/{registration_id} | Get a scanner registration details
[**scanners_registration_id_metadata_get**](ProductsApi.md#scanners_registration_id_metadata_get) | **GET** /scanners/{registration_id}/metadata | Get the metadata of the specified scanner registration
[**search_get**](ProductsApi.md#search_get) | **GET** /search | Search for projects, repositories and helm charts
[**statistics_get**](ProductsApi.md#statistics_get) | **GET** /statistics | Get projects number and repositories number relevant to the user
[**system_cve_allowlist_get**](ProductsApi.md#system_cve_allowlist_get) | **GET** /system/CVEAllowlist | Get the system level allowlist of CVE.
[**system_cve_allowlist_put**](ProductsApi.md#system_cve_allowlist_put) | **PUT** /system/CVEAllowlist | Update the system level allowlist of CVE.
[**system_oidc_ping_post**](ProductsApi.md#system_oidc_ping_post) | **POST** /system/oidc/ping | Test the OIDC endpoint.
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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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
        update_time="update_time_example",
        description="description_example",
        color="color_example",
        creation_time="creation_time_example",
        deleted=True,
        scope="scope_example",
        project_id=1,
        id=1,
        name="name_example",
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    configurations = Configurations(
        oidc_verify_cert=True,
        email_identity="email_identity_example",
        ldap_group_search_filter="ldap_group_search_filter_example",
        auth_mode="auth_mode_example",
        self_registration=True,
        oidc_scope="oidc_scope_example",
        ldap_search_dn="ldap_search_dn_example",
        storage_per_project="storage_per_project_example",
        scan_all_policy=ConfigurationsResponseScanAllPolicy(
            type="type_example",
            parameter=ConfigurationsResponseScanAllPolicyParameter(
                daily_time=1,
            ),
        ),
        verify_remote_cert=True,
        ldap_timeout=1,
        ldap_base_dn="ldap_base_dn_example",
        ldap_filter="ldap_filter_example",
        read_only=True,
        quota_per_project_enable=True,
        ldap_url="ldap_url_example",
        oidc_name="oidc_name_example",
        project_creation_restriction="project_creation_restriction_example",
        ldap_uid="ldap_uid_example",
        oidc_client_id="oidc_client_id_example",
        ldap_group_base_dn="ldap_group_base_dn_example",
        ldap_group_attribute_name="ldap_group_attribute_name_example",
        email_insecure=True,
        ldap_group_admin_dn="ldap_group_admin_dn_example",
        email_username="email_username_example",
        oidc_endpoint="oidc_endpoint_example",
        oidc_client_secret="oidc_client_secret_example",
        ldap_scope=1,
        count_per_project="count_per_project_example",
        token_expiration=1,
        ldap_group_search_scope=1,
        email_ssl=True,
        email_port=1,
        email_host="email_host_example",
        email_from="email_from_example",
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    email_server_setting = EmailServerSetting(
        email_ssl=True,
        email_password="email_password_example",
        email_identity="email_identity_example",
        email_port=1,
        email_username="email_username_example",
        email_host="email_host_example",
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

[basicAuth](../README.md#basicAuth)

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
**415** | The Media Type of the request is not supported, it has to be \&quot;application/json\&quot; |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_get**
> OverallHealthStatus health_get()

Health check API

The endpoint returns the health stauts of the system. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get successfully. |  * X-Total-Count - The total count of access logs <br>  * Link - Link refers to the previous page and next page <br>  |
**400** | Invalid parameters. |  -  |
**401** | User need to log in first. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_delete**
> labels_id_delete(id)

Delete the label specified by ID.

Delete the label specified by ID. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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
        update_time="update_time_example",
        description="description_example",
        color="color_example",
        creation_time="creation_time_example",
        deleted=True,
        scope="scope_example",
        project_id=1,
        id=1,
        name="name_example",
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    label = Label(
        update_time="update_time_example",
        description="description_example",
        color="color_example",
        creation_time="creation_time_example",
        deleted=True,
        scope="scope_example",
        project_id=1,
        id=1,
        name="name_example",
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

[basicAuth](../README.md#basicAuth)

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
**415** | The Media Type of the request is not supported, it has to be \&quot;application/json\&quot; |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_groups_search_get**
> [UserGroup] ldap_groups_search_get()

Search available ldap groups.

This endpoint searches the available ldap groups based on related configuration parameters. support to search by groupname or groupdn. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    groupname = "groupname_example" # str | Ldap group name (optional)
    groupdn = "groupdn_example" # str | The LDAP group DN (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search available ldap groups.
        api_response = api_instance.ldap_groups_search_get(groupname=groupname, groupdn=groupdn)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->ldap_groups_search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupname** | **str**| Ldap group name | [optional]
 **groupdn** | **str**| The LDAP group DN | [optional]

### Return type

[**[UserGroup]**](UserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search ldap group successfully. |  -  |
**400** | The Ldap group DN is invalid. |  -  |
**404** | No ldap group found. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_ping_post**
> ldap_ping_post()

Ping available ldap service.

This endpoint ping the available ldap service for test related configuration parameters. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    ldap_conf = LdapConf(
        ldap_url="ldap_url_example",
        ldap_uid="ldap_uid_example",
        ldap_search_dn="ldap_search_dn_example",
        ldap_connection_timeout=1,
        ldap_search_password="ldap_search_password_example",
        ldap_scope=1,
        ldap_base_dn="ldap_base_dn_example",
        ldap_filter="ldap_filter_example",
    ) # LdapConf | ldap configuration. support input ldap service configuration. If it's a empty request, will load current configuration from the system. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ping available ldap service.
        api_instance.ldap_ping_post(ldap_conf=ldap_conf)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->ldap_ping_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_conf** | [**LdapConf**](LdapConf.md)| ldap configuration. support input ldap service configuration. If it&#39;s a empty request, will load current configuration from the system. | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ping ldap service successfully. |  -  |
**400** | Inviald ldap configuration parameters. |  -  |
**401** | User need to login first. |  -  |
**403** | Only admin has this authority. |  -  |
**415** | The Media Type of the request is not supported, it has to be \&quot;application/json\&quot; |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_users_import_post**
> ldap_users_import_post(ldap_import_users)

Import selected available ldap users.

This endpoint adds the selected available ldap users to harbor based on related configuration parameters from the system. System will try to guess the user email address and realname, add to harbor user information. If have errors when import user, will return the list of importing failed uid and the failed reason. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.ldap_failed_import_users import LdapFailedImportUsers
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    ldap_import_users = LdapImportUsers(
        ldap_uid_list=[
            "ldap_uid_list_example",
        ],
    ) # LdapImportUsers | The uid listed for importing. This list will check users validity of ldap service based on configuration from the system.

    # example passing only required values which don't have defaults set
    try:
        # Import selected available ldap users.
        api_instance.ldap_users_import_post(ldap_import_users)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->ldap_users_import_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_import_users** | [**LdapImportUsers**](LdapImportUsers.md)| The uid listed for importing. This list will check users validity of ldap service based on configuration from the system. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add ldap users successfully. |  -  |
**401** | User need to login first. |  -  |
**403** | Only admin has this authority. |  -  |
**404** | Failed import some users. |  -  |
**415** | The Media Type of the request is not supported, it has to be \&quot;application/json\&quot; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_users_search_get**
> [LdapUsers] ldap_users_search_get()

Search available ldap users.

This endpoint searches the available ldap users based on related configuration parameters. Support searched by input ladp configuration, load configuration from the system and specific filter. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.ldap_users import LdapUsers
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    username = "username_example" # str | Registered user ID (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search available ldap users.
        api_response = api_instance.ldap_users_search_get(username=username)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->ldap_users_search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Registered user ID | [optional]

### Return type

[**[LdapUsers]**](LdapUsers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search ldap users successfully. |  -  |
**401** | User need to login first. |  -  |
**403** | Only admin has this authority. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_immutabletagrules_get**
> [ImmutableRule] projects_project_id_immutabletagrules_get(project_id)

List all immutable tag rules of current project

This endpoint returns the immutable tag rules of a project 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.immutable_rule import ImmutableRule
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.

    # example passing only required values which don't have defaults set
    try:
        # List all immutable tag rules of current project
        api_response = api_instance.projects_project_id_immutabletagrules_get(project_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_immutabletagrules_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |

### Return type

[**[ImmutableRule]**](ImmutableRule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List project immutable tag rules successfully. |  -  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to list immutable tag rules of the project. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_immutabletagrules_id_delete**
> projects_project_id_immutabletagrules_id_delete(project_id, id)

Delete the immutable tag rule.

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    id = 1 # int | Immutable tag rule ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete the immutable tag rule.
        api_instance.projects_project_id_immutabletagrules_id_delete(project_id, id)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_immutabletagrules_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **id** | **int**| Immutable tag rule ID. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete the immutable tag rule successfully. |  -  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to delete immutable tags of the project. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_immutabletagrules_id_put**
> projects_project_id_immutabletagrules_id_put(project_id, id, immutable_rule)

Update the immutable tag rule or enable or disable the rule

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.immutable_rule import ImmutableRule
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    id = 1 # int | Immutable tag rule ID.
    immutable_rule = ImmutableRule(
        priority=1,
        scope_selectors={
            "key": [
                ImmutableSelector(
                    decoration="decoration_example",
                    pattern="pattern_example",
                    kind="kind_example",
                    extras="extras_example",
                ),
            ],
        },
        disabled=True,
        params={
            "key": {},
        },
        template="template_example",
        action="action_example",
        tag_selectors=[],
        id=1,
    ) # ImmutableRule | 

    # example passing only required values which don't have defaults set
    try:
        # Update the immutable tag rule or enable or disable the rule
        api_instance.projects_project_id_immutabletagrules_id_put(project_id, id, immutable_rule)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_immutabletagrules_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **id** | **int**| Immutable tag rule ID. |
 **immutable_rule** | [**ImmutableRule**](ImmutableRule.md)|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update the immutable tag rule successfully. |  -  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to update the immutable tag rule of the project. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_immutabletagrules_post**
> projects_project_id_immutabletagrules_post(project_id, immutable_rule)

Add an immutable tag rule to current project

This endpoint add an immutable tag rule to the project 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.immutable_rule import ImmutableRule
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    immutable_rule = ImmutableRule(
        priority=1,
        scope_selectors={
            "key": [
                ImmutableSelector(
                    decoration="decoration_example",
                    pattern="pattern_example",
                    kind="kind_example",
                    extras="extras_example",
                ),
            ],
        },
        disabled=True,
        params={
            "key": {},
        },
        template="template_example",
        action="action_example",
        tag_selectors=[
            ImmutableSelector(
                decoration="decoration_example",
                pattern="pattern_example",
                kind="kind_example",
                extras="extras_example",
            ),
        ],
        id=1,
    ) # ImmutableRule | 

    # example passing only required values which don't have defaults set
    try:
        # Add an immutable tag rule to current project
        api_instance.projects_project_id_immutabletagrules_post(project_id, immutable_rule)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_immutabletagrules_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **immutable_rule** | [**ImmutableRule**](ImmutableRule.md)|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add the immutable tag rule successfully. |  -  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to get immutable tag rule of the project. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_get**
> [ProjectMemberEntity] projects_project_id_members_get(project_id)

Get all project member information

Get all project member information

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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
        member_group=UserGroup(
            group_name="group_name_example",
            ldap_group_dn="ldap_group_dn_example",
            group_type=1,
            id=1,
        ),
        member_user=UserEntity(
            username="username_example",
            user_id=1,
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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
        enable_content_trust="enable_content_trust_example",
        auto_scan="auto_scan_example",
        severity="severity_example",
        public="public_example",
        reuse_sys_cve_allowlist="reuse_sys_cve_allowlist_example",
        prevent_vul="prevent_vul_example",
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

[basicAuth](../README.md#basicAuth)

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
**415** | The Media Type of the request is not supported, it has to be \&quot;application/json\&quot; |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_scanner_candidates_get**
> [ScannerRegistration] projects_project_id_scanner_candidates_get(project_id)

Get scanner registration candidates for configurating project level scanner

Retrieve the system configured scanner registrations as candidates of setting project level scanner. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.scanner_registration import ScannerRegistration
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | The project identifier.
    page = 1 # int | The page number. (optional)
    page_size = 1 # int | The size of per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get scanner registration candidates for configurating project level scanner
        api_response = api_instance.projects_project_id_scanner_candidates_get(project_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_scanner_candidates_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get scanner registration candidates for configurating project level scanner
        api_response = api_instance.projects_project_id_scanner_candidates_get(project_id, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_scanner_candidates_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project identifier. |
 **page** | **int**| The page number. | [optional]
 **page_size** | **int**| The size of per page. | [optional]

### Return type

[**[ScannerRegistration]**](ScannerRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of scanner registrations. |  * X-Total-Count - The total count of access logs <br>  * Link - Link refers to the previous page and next page <br>  |
**400** | Bad project ID or query parameters |  -  |
**401** | Unauthorized request |  -  |
**403** | Request is not allowed |  -  |
**500** | Internal server error happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_scanner_get**
> ScannerRegistration projects_project_id_scanner_get(project_id)

Get project level scanner

Get the scanner registration of the specified project. If no scanner registration is configured for the specified project, the system default scanner registration will be returned.

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.scanner_registration import ScannerRegistration
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | The project identifier.

    # example passing only required values which don't have defaults set
    try:
        # Get project level scanner
        api_response = api_instance.projects_project_id_scanner_get(project_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_scanner_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project identifier. |

### Return type

[**ScannerRegistration**](ScannerRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the scanner registration. |  -  |
**400** | Bad project ID |  -  |
**401** | Unauthorized request |  -  |
**403** | Request is not allowed |  -  |
**404** | The requested object is not found |  -  |
**500** | Internal server error happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_events_get**
> SupportedWebhookEventTypes projects_project_id_webhook_events_get(project_id)

Get supported event types and notify types.

Get supportted event types and notify types.

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.supported_webhook_event_types import SupportedWebhookEventTypes
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.

    # example passing only required values which don't have defaults set
    try:
        # Get supported event types and notify types.
        api_response = api_instance.projects_project_id_webhook_events_get(project_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_webhook_events_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |

### Return type

[**SupportedWebhookEventTypes**](SupportedWebhookEventTypes.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to list webhook jobs of the project. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_jobs_get**
> [WebhookJob] projects_project_id_webhook_jobs_get(project_id, policy_id)

List project webhook jobs

This endpoint returns webhook jobs of a project. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.webhook_job import WebhookJob
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    policy_id = 1 # int | The policy ID.

    # example passing only required values which don't have defaults set
    try:
        # List project webhook jobs
        api_response = api_instance.projects_project_id_webhook_jobs_get(project_id, policy_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_webhook_jobs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **policy_id** | **int**| The policy ID. |

### Return type

[**[WebhookJob]**](WebhookJob.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List project webhook jobs successfully. |  * X-Total-Count - The total count of access logs <br>  * Link - Link refers to the previous page and next page <br>  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to list webhook jobs of the project. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_lasttrigger_get**
> [WebhookLastTrigger] projects_project_id_webhook_lasttrigger_get(project_id)

Get project webhook policy last trigger info

This endpoint returns last trigger information of project webhook policy. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.webhook_last_trigger import WebhookLastTrigger
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.

    # example passing only required values which don't have defaults set
    try:
        # Get project webhook policy last trigger info
        api_response = api_instance.projects_project_id_webhook_lasttrigger_get(project_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_webhook_lasttrigger_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |

### Return type

[**[WebhookLastTrigger]**](WebhookLastTrigger.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test webhook connection successfully. |  -  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to get webhook policy of the project. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_get**
> [WebhookPolicy] projects_project_id_webhook_policies_get(project_id)

List project webhook policies.

This endpoint returns webhook policies of a project. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.webhook_policy import WebhookPolicy
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.

    # example passing only required values which don't have defaults set
    try:
        # List project webhook policies.
        api_response = api_instance.projects_project_id_webhook_policies_get(project_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_webhook_policies_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |

### Return type

[**[WebhookPolicy]**](WebhookPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List project webhook policies successfully. |  -  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to list webhook policies of the project. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_policy_id_delete**
> projects_project_id_webhook_policies_policy_id_delete(project_id, policy_id)

Delete webhook policy of a project

This endpoint is aimed to delete webhookpolicy of a project. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    policy_id = 1 # int | The id of webhook policy.

    # example passing only required values which don't have defaults set
    try:
        # Delete webhook policy of a project
        api_instance.projects_project_id_webhook_policies_policy_id_delete(project_id, policy_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_webhook_policies_policy_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **policy_id** | **int**| The id of webhook policy. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete webhook policy successfully. |  -  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to delete webhook policy of the project. |  -  |
**404** | Webhook policy ID does not exist. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_policy_id_get**
> WebhookPolicy projects_project_id_webhook_policies_policy_id_get(project_id, policy_id)

Get project webhook policy

This endpoint returns specified webhook policy of a project. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.webhook_policy import WebhookPolicy
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    policy_id = 1 # int | The id of webhook policy.

    # example passing only required values which don't have defaults set
    try:
        # Get project webhook policy
        api_response = api_instance.projects_project_id_webhook_policies_policy_id_get(project_id, policy_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_webhook_policies_policy_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **policy_id** | **int**| The id of webhook policy. |

### Return type

[**WebhookPolicy**](WebhookPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get webhook policy successfully. |  -  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to get webhook policy of the project. |  -  |
**404** | Webhook policy ID does not exist. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_policy_id_put**
> projects_project_id_webhook_policies_policy_id_put(project_id, policy_id, webhook_policy)

Update webhook policy of a project.

This endpoint is aimed to update the webhook policy of a project. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.webhook_policy import WebhookPolicy
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    policy_id = 1 # int | The id of webhook policy.
    webhook_policy = WebhookPolicy(
        update_time="update_time_example",
        description="description_example",
        creator="creator_example",
        creation_time="creation_time_example",
        enabled=True,
        targets=[
            WebhookTargetObject(
                type="type_example",
                auth_header="auth_header_example",
                skip_cert_verify=True,
                address="address_example",
            ),
        ],
        event_types=[
            "event_types_example",
        ],
        project_id=1,
        id=1,
        name="name_example",
    ) # WebhookPolicy | All properties needed except \"id\", \"project_id\", \"creation_time\", \"update_time\".

    # example passing only required values which don't have defaults set
    try:
        # Update webhook policy of a project.
        api_instance.projects_project_id_webhook_policies_policy_id_put(project_id, policy_id, webhook_policy)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_webhook_policies_policy_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **policy_id** | **int**| The id of webhook policy. |
 **webhook_policy** | [**WebhookPolicy**](WebhookPolicy.md)| All properties needed except \&quot;id\&quot;, \&quot;project_id\&quot;, \&quot;creation_time\&quot;, \&quot;update_time\&quot;. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update webhook policy successfully. |  -  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to update webhook policy of the project. |  -  |
**404** | Webhook policy ID does not exist. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_post**
> projects_project_id_webhook_policies_post(project_id, webhook_policy)

Create project webhook policy.

This endpoint create a webhook policy if the project does not have one. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.webhook_policy import WebhookPolicy
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID
    webhook_policy = WebhookPolicy(
        update_time="update_time_example",
        description="description_example",
        creator="creator_example",
        creation_time="creation_time_example",
        enabled=True,
        targets=[
            WebhookTargetObject(
                type="type_example",
                auth_header="auth_header_example",
                skip_cert_verify=True,
                address="address_example",
            ),
        ],
        event_types=[
            "event_types_example",
        ],
        project_id=1,
        id=1,
        name="name_example",
    ) # WebhookPolicy | Properties \"targets\" and \"event_types\" needed.

    # example passing only required values which don't have defaults set
    try:
        # Create project webhook policy.
        api_instance.projects_project_id_webhook_policies_post(project_id, webhook_policy)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_webhook_policies_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID |
 **webhook_policy** | [**WebhookPolicy**](WebhookPolicy.md)| Properties \&quot;targets\&quot; and \&quot;event_types\&quot; needed. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Project webhook policy create successfully. |  * Location - The URL of the created resource <br>  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to create webhook policy of the project. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_test_post**
> projects_project_id_webhook_policies_test_post(project_id, webhook_policy)

Test project webhook connection

This endpoint tests webhook connection of a project. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.webhook_policy import WebhookPolicy
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    project_id = 1 # int | Relevant project ID.
    webhook_policy = WebhookPolicy(
        update_time="update_time_example",
        description="description_example",
        creator="creator_example",
        creation_time="creation_time_example",
        enabled=True,
        targets=[
            WebhookTargetObject(
                type="type_example",
                auth_header="auth_header_example",
                skip_cert_verify=True,
                address="address_example",
            ),
        ],
        event_types=[
            "event_types_example",
        ],
        project_id=1,
        id=1,
        name="name_example",
    ) # WebhookPolicy | Only property \"targets\" needed.

    # example passing only required values which don't have defaults set
    try:
        # Test project webhook connection
        api_instance.projects_project_id_webhook_policies_test_post(project_id, webhook_policy)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->projects_project_id_webhook_policies_test_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. |
 **webhook_policy** | [**WebhookPolicy**](WebhookPolicy.md)| Only property \&quot;targets\&quot; needed. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test webhook connection successfully. |  -  |
**400** | Illegal format of provided ID value. |  -  |
**401** | User need to log in first. |  -  |
**403** | User have no permission to get webhook policy of the project. |  -  |
**500** | Internal server errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_get**
> [Quota] quotas_get()

List quotas

List quotas

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.quota import Quota
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    reference = "reference_example" # str | The reference type of quota. (optional)
    reference_id = "reference_id_example" # str | The reference id of quota. (optional)
    sort = "sort_example" # str | Sort method, valid values include: 'hard.resource_name', '-hard.resource_name', 'used.resource_name', '-used.resource_name'. Here '-' stands for descending order, resource_name should be the real resource name of the quota.  (optional)
    page = 1 # int | The page number, default is 1. (optional)
    page_size = 1 # int | The size of per page, default is 10, maximum is 100. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List quotas
        api_response = api_instance.quotas_get(reference=reference, reference_id=reference_id, sort=sort, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->quotas_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference** | **str**| The reference type of quota. | [optional]
 **reference_id** | **str**| The reference id of quota. | [optional]
 **sort** | **str**| Sort method, valid values include: &#39;hard.resource_name&#39;, &#39;-hard.resource_name&#39;, &#39;used.resource_name&#39;, &#39;-used.resource_name&#39;. Here &#39;-&#39; stands for descending order, resource_name should be the real resource name of the quota.  | [optional]
 **page** | **int**| The page number, default is 1. | [optional]
 **page_size** | **int**| The size of per page, default is 10, maximum is 100. | [optional]

### Return type

[**[Quota]**](Quota.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the quotas. |  * X-Total-Count - The total count of access logs <br>  * Link - Link refers to the previous page and next page <br>  |
**401** | User is not authenticated. |  -  |
**403** | User does not have permission to call this API. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_id_get**
> Quota quotas_id_get(id)

Get the specified quota

Get the specified quota

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.quota import Quota
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | Quota ID

    # example passing only required values which don't have defaults set
    try:
        # Get the specified quota
        api_response = api_instance.quotas_id_get(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->quotas_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Quota ID |

### Return type

[**Quota**](Quota.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the quota. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission to call this API |  -  |
**404** | Quota does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_id_put**
> quotas_id_put(id, quota_update_req)

Update the specified quota

Update hard limits of the specified quota

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.quota_update_req import QuotaUpdateReq
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | Quota ID
    quota_update_req = QuotaUpdateReq(
        hard=ResourceList(
            key=1,
        ),
    ) # QuotaUpdateReq | The new hard limits for the quota

    # example passing only required values which don't have defaults set
    try:
        # Update the specified quota
        api_instance.quotas_id_put(id, quota_update_req)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->quotas_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Quota ID |
 **quota_update_req** | [**QuotaUpdateReq**](QuotaUpdateReq.md)| The new hard limits for the quota |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated quota hard limits successfully. |  -  |
**400** | Illegal format of quota update request. |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission to the quota. |  -  |
**404** | Quota ID does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_get**
> [Registry] registries_get()

List registries.

List registries according to the query. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.registry import Registry
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    name = "name_example" # str | Deprecated, use `q` instead. (optional)
    q = "q_example" # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List registries.
        api_response = api_instance.registries_get(name=name, q=q)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->registries_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Deprecated, use &#x60;q&#x60; instead. | [optional]
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional]

### Return type

[**[Registry]**](Registry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List registries successfully. |  -  |
**401** | User need to log in first. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_id_delete**
> registries_id_delete(id)

Delete specific registry.

This endpoint is for to delete specific registry. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | The registry's ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete specific registry.
        api_instance.registries_id_delete(id)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->registries_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The registry&#39;s ID. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Registry deleted successfully. |  -  |
**400** | Registry&#39;s ID is invalid or the registry is used by policies. |  -  |
**401** | Only admin has this authority. |  -  |
**404** | Registry does not exist. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_id_get**
> Registry registries_id_get(id)

Get registry.

This endpoint is for get specific registry.

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.registry import Registry
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | The registry ID.

    # example passing only required values which don't have defaults set
    try:
        # Get registry.
        api_response = api_instance.registries_id_get(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->registries_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The registry ID. |

### Return type

[**Registry**](Registry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get registry successfully. |  -  |
**401** | User need to log in first. |  -  |
**404** | Registry not found |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_id_info_get**
> RegistryInfo registries_id_info_get(id)

Get registry info.

Get the info of one specific registry.

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.registry_info import RegistryInfo
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | The registry ID.

    # example passing only required values which don't have defaults set
    try:
        # Get registry info.
        api_response = api_instance.registries_id_info_get(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->registries_id_info_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The registry ID. |

### Return type

[**RegistryInfo**](RegistryInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get registry successfully. |  -  |
**401** | User need to log in first. |  -  |
**404** | Registry not found |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_id_namespace_get**
> [Namespace] registries_id_namespace_get(id)

List namespaces of registry

This endpoint let user list namespaces of registry according to query. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.namespace import Namespace
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | The registry ID.
    name = "name_example" # str | The name of namespace. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List namespaces of registry
        api_response = api_instance.registries_id_namespace_get(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->registries_id_namespace_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List namespaces of registry
        api_response = api_instance.registries_id_namespace_get(id, name=name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->registries_id_namespace_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The registry ID. |
 **name** | **str**| The name of namespace. | [optional]

### Return type

[**[Namespace]**](Namespace.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | User need to login first. |  -  |
**403** | User has no privilege for the operation. |  -  |
**404** | No registry found. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_id_put**
> registries_id_put(id, put_registry)

Update a given registry.

This endpoint is for update a given registry. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.put_registry import PutRegistry
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | The registry's ID.
    put_registry = PutRegistry(
        access_key="access_key_example",
        credential_type="credential_type_example",
        name="name_example",
        access_secret="access_secret_example",
        url="url_example",
        insecure=True,
        description="description_example",
    ) # PutRegistry | Updates registry.

    # example passing only required values which don't have defaults set
    try:
        # Update a given registry.
        api_instance.registries_id_put(id, put_registry)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->registries_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The registry&#39;s ID. |
 **put_registry** | [**PutRegistry**](PutRegistry.md)| Updates registry. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated registry successfully. |  -  |
**400** | The registry is associated with policy which is enabled. |  -  |
**401** | User need to log in first. |  -  |
**404** | Registry does not exist. |  -  |
**409** | Registry name is already used. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_ping_post**
> registries_ping_post(registry)

Ping status of a registry.

This endpoint checks status of a registry, the registry can be given by ID or URL (together with credential) 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.registry import Registry
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    registry = Registry(
        status="status_example",
        credential=RegistryCredential(
            access_key="access_key_example",
            access_secret="access_secret_example",
            type="type_example",
        ),
        update_time="update_time_example",
        name="name_example",
        url="url_example",
        insecure=True,
        creation_time="creation_time_example",
        type="type_example",
        id=1,
        description="description_example",
    ) # Registry | Registry to ping.

    # example passing only required values which don't have defaults set
    try:
        # Ping status of a registry.
        api_instance.registries_ping_post(registry)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->registries_ping_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | [**Registry**](Registry.md)| Registry to ping. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Registry is healthy. |  -  |
**400** | No proper registry information provided. |  -  |
**401** | User need to log in first. |  -  |
**404** | Registry not found (when registry is provided by ID). |  -  |
**415** | The Media Type of the request is not supported, it has to be \&quot;application/json\&quot; |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_post**
> registries_post(registry)

Create a new registry.

This endpoint is for user to create a new registry. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.registry import Registry
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    registry = Registry(
        status="status_example",
        credential=RegistryCredential(
            access_key="access_key_example",
            access_secret="access_secret_example",
            type="type_example",
        ),
        update_time="update_time_example",
        name="name_example",
        url="url_example",
        insecure=True,
        creation_time="creation_time_example",
        type="type_example",
        id=1,
        description="description_example",
    ) # Registry | New created registry.

    # example passing only required values which don't have defaults set
    try:
        # Create a new registry.
        api_instance.registries_post(registry)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->registries_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | [**Registry**](Registry.md)| New created registry. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Registry created successfully. |  * Location - The URL of the created resource <br>  |
**400** | Unsatisfied with constraints of the registry creation. |  -  |
**401** | User need to log in first. |  -  |
**409** | Registry name already exists. |  -  |
**415** | The Media Type of the request is not supported, it has to be \&quot;application/json\&quot; |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_adapters_get**
> [str] replication_adapters_get()

List supported adapters.

This endpoint let user list supported adapters. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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
        # List supported adapters.
        api_response = api_instance.replication_adapters_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->replication_adapters_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_policies_get**
> [ReplicationPolicy] replication_policies_get()

List replication policies

This endpoint let user list replication policies 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.replication_policy import ReplicationPolicy
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    name = "name_example" # str | The replication policy name. (optional)
    page = 1 # int | The page number. (optional)
    page_size = 1 # int | The size of per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List replication policies
        api_response = api_instance.replication_policies_get(name=name, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->replication_policies_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The replication policy name. | [optional]
 **page** | **int**| The page number. | [optional]
 **page_size** | **int**| The size of per page. | [optional]

### Return type

[**[ReplicationPolicy]**](ReplicationPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get policy successfully. |  * X-Total-Count - The total count of access logs <br>  * Link - Link refers to the previous page and next page <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_policies_id_delete**
> replication_policies_id_delete(id)

Delete the replication policy specified by ID.

Delete the replication policy specified by ID. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | Replication policy ID

    # example passing only required values which don't have defaults set
    try:
        # Delete the replication policy specified by ID.
        api_instance.replication_policies_id_delete(id)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->replication_policies_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Replication policy ID |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_policies_id_get**
> ReplicationPolicy replication_policies_id_get(id)

Get replication policy.

This endpoint let user get replication policy by specific ID. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.replication_policy import ReplicationPolicy
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | policy ID

    # example passing only required values which don't have defaults set
    try:
        # Get replication policy.
        api_response = api_instance.replication_policies_id_get(id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->replication_policies_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| policy ID |

### Return type

[**ReplicationPolicy**](ReplicationPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the replication policy successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_policies_id_put**
> replication_policies_id_put(id, replication_policy)

Update the replication policy

This endpoint let user update policy. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.replication_policy import ReplicationPolicy
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    id = 1 # int | policy ID
    replication_policy = ReplicationPolicy(
        update_time="update_time_example",
        description="description_example",
        enabled=True,
        filters=[
            ReplicationFilter(
                type="type_example",
                value="value_example",
            ),
        ],
        dest_registry=Registry(
            status="status_example",
            credential=RegistryCredential(
                access_key="access_key_example",
                access_secret="access_secret_example",
                type="type_example",
            ),
            update_time="update_time_example",
            name="name_example",
            url="url_example",
            insecure=True,
            creation_time="creation_time_example",
            type="type_example",
            id=1,
            description="description_example",
        ),
        creation_time="creation_time_example",
        src_registry=Registry(
            status="status_example",
            credential=RegistryCredential(
                access_key="access_key_example",
                access_secret="access_secret_example",
                type="type_example",
            ),
            update_time="update_time_example",
            name="name_example",
            url="url_example",
            insecure=True,
            creation_time="creation_time_example",
            type="type_example",
            id=1,
            description="description_example",
        ),
        dest_namespace="dest_namespace_example",
        trigger=ReplicationTrigger(
            type="type_example",
            trigger_settings=TriggerSettings(
                cron="cron_example",
            ),
        ),
        deletion=True,
        override=True,
        id=1,
        name="name_example",
    ) # ReplicationPolicy | The replication policy model.

    # example passing only required values which don't have defaults set
    try:
        # Update the replication policy
        api_instance.replication_policies_id_put(id, replication_policy)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->replication_policies_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| policy ID |
 **replication_policy** | [**ReplicationPolicy**](ReplicationPolicy.md)| The replication policy model. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_policies_post**
> replication_policies_post(replication_policy)

Create a replication policy

This endpoint let user create a replication policy 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.replication_policy import ReplicationPolicy
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    replication_policy = ReplicationPolicy(
        update_time="update_time_example",
        description="description_example",
        enabled=True,
        filters=[
            ReplicationFilter(
                type="type_example",
                value="value_example",
            ),
        ],
        dest_registry=Registry(
            status="status_example",
            credential=RegistryCredential(
                access_key="access_key_example",
                access_secret="access_secret_example",
                type="type_example",
            ),
            update_time="update_time_example",
            name="name_example",
            url="url_example",
            insecure=True,
            creation_time="creation_time_example",
            type="type_example",
            id=1,
            description="description_example",
        ),
        creation_time="creation_time_example",
        src_registry=Registry(
            status="status_example",
            credential=RegistryCredential(
                access_key="access_key_example",
                access_secret="access_secret_example",
                type="type_example",
            ),
            update_time="update_time_example",
            name="name_example",
            url="url_example",
            insecure=True,
            creation_time="creation_time_example",
            type="type_example",
            id=1,
            description="description_example",
        ),
        dest_namespace="dest_namespace_example",
        trigger=ReplicationTrigger(
            type="type_example",
            trigger_settings=TriggerSettings(
                cron="cron_example",
            ),
        ),
        deletion=True,
        override=True,
        id=1,
        name="name_example",
    ) # ReplicationPolicy | The policy model.

    # example passing only required values which don't have defaults set
    try:
        # Create a replication policy
        api_instance.replication_policies_post(replication_policy)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->replication_policies_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replication_policy** | [**ReplicationPolicy**](ReplicationPolicy.md)| The policy model. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The URL of the created resource <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**415** | The Media Type of the request is not supported, it has to be \&quot;application/json\&quot; |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_get**
> [ScannerRegistration] scanners_get()

List scanner registrations

Returns a list of currently configured scanner registrations. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.scanner_registration import ScannerRegistration
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    page = 1 # int | The page number. (optional)
    page_size = 1 # int | The size of per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List scanner registrations
        api_response = api_instance.scanners_get(page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->scanners_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number. | [optional]
 **page_size** | **int**| The size of per page. | [optional]

### Return type

[**[ScannerRegistration]**](ScannerRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of scanner registrations. |  * X-Total-Count - The total count of access logs <br>  * Link - Link refers to the previous page and next page <br>  |
**400** | Bad query paramters |  -  |
**401** | Unauthorized request |  -  |
**403** | Request is not allowed, system role required |  -  |
**500** | Internal server error happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_ping_post**
> scanners_ping_post(scanner_registration_settings)

Tests scanner registration settings

Pings scanner adapter to test endpoint URL and authorization settings. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.scanner_registration_settings import ScannerRegistrationSettings
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    scanner_registration_settings = ScannerRegistrationSettings(
        url="http://harbor-scanner-clair:8080",
        access_credential="Bearer: JWTTOKENGOESHERE",
        name="Clair",
        auth="",
    ) # ScannerRegistrationSettings | A scanner registration settings to be tested.

    # example passing only required values which don't have defaults set
    try:
        # Tests scanner registration settings
        api_instance.scanners_ping_post(scanner_registration_settings)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->scanners_ping_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scanner_registration_settings** | [**ScannerRegistrationSettings**](ScannerRegistrationSettings.md)| A scanner registration settings to be tested. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test succeeded |  -  |
**400** | Bad registration settings |  -  |
**401** | Unauthorized request |  -  |
**403** | Request is not allowed, system role required |  -  |
**500** | Internal server error happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_registration_id_get**
> ScannerRegistration scanners_registration_id_get(registration_id)

Get a scanner registration details

Retruns the details of the specified scanner registration. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.scanner_registration import ScannerRegistration
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifer.

    # example passing only required values which don't have defaults set
    try:
        # Get a scanner registration details
        api_response = api_instance.scanners_registration_id_get(registration_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->scanners_registration_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifer. |

### Return type

[**ScannerRegistration**](ScannerRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the scanner registration. |  -  |
**401** | Unauthorized request |  -  |
**403** | Request is not allowed, system role required |  -  |
**404** | The requested object is not found |  -  |
**500** | Internal server error happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_registration_id_metadata_get**
> ScannerAdapterMetadata scanners_registration_id_metadata_get(registration_id)

Get the metadata of the specified scanner registration

Get the metadata of the specified scanner registration, including the capabilities and customzied properties. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.scanner_adapter_metadata import ScannerAdapterMetadata
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifier.

    # example passing only required values which don't have defaults set
    try:
        # Get the metadata of the specified scanner registration
        api_response = api_instance.scanners_registration_id_metadata_get(registration_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->scanners_registration_id_metadata_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. |

### Return type

[**ScannerAdapterMetadata**](ScannerAdapterMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata of the specified scanner adapter |  -  |
**401** | Unauthorized request |  -  |
**403** | Request is not allowed |  -  |
**500** | Internal server error happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_get**
> [Search] search_get(q)

Search for projects, repositories and helm charts

The Search endpoint returns information about the projects ,repositories  and helm charts offered at public status or related to the current logged in user. The response includes the project, repository list and charts in a proper display order. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.search import Search
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    q = "q_example" # str | Search parameter for project and repository name.

    # example passing only required values which don't have defaults set
    try:
        # Search for projects, repositories and helm charts
        api_response = api_instance.search_get(q)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search parameter for project and repository name. |

### Return type

[**[Search]**](Search.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of search results |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_get**
> StatisticMap statistics_get()

Get projects number and repositories number relevant to the user

This endpoint is aimed to statistic all of the projects number and repositories number relevant to the logined user, also the public projects number and repositories number. If the user is admin, he can also get total projects number and total repositories number. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

# **system_cve_allowlist_get**
> CVEAllowlist system_cve_allowlist_get()

Get the system level allowlist of CVE.

Get the system level allowlist of CVE.  This API can be called by all authenticated users.

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.cve_allowlist import CVEAllowlist
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

# Configure HTTP basic authorization: basicAuth
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
        # Get the system level allowlist of CVE.
        api_response = api_instance.system_cve_allowlist_get()
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->system_cve_allowlist_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CVEAllowlist**](CVEAllowlist.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the CVE allowlist. |  -  |
**401** | User is not authenticated. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_cve_allowlist_put**
> system_cve_allowlist_put()

Update the system level allowlist of CVE.

This API overwrites the system level allowlist of CVE with the list in request body.  Only system Admin has permission to call this API.

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.cve_allowlist import CVEAllowlist
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    cve_allowlist = CVEAllowlist(
        items=[
            CVEAllowlistItem(
                cve_id="cve_id_example",
            ),
        ],
        project_id=1,
        id=1,
        expires_at=1,
    ) # CVEAllowlist | The allowlist with new content (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the system level allowlist of CVE.
        api_instance.system_cve_allowlist_put(cve_allowlist=cve_allowlist)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->system_cve_allowlist_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_allowlist** | [**CVEAllowlist**](CVEAllowlist.md)| The allowlist with new content | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the CVE allowlist. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User does not have permission to call this API. |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_oidc_ping_post**
> system_oidc_ping_post(inline_object1)

Test the OIDC endpoint.

Test the OIDC endpoint, the setting of the endpoint is provided in the request.  This API can only be called by system admin.

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import products_api
from harbor_client.model.inline_object1 import InlineObject1
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    inline_object1 = InlineObject1(
        url="url_example",
        verify_cert=True,
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Test the OIDC endpoint.
        api_instance.system_oidc_ping_post(inline_object1)
    except harbor_client.ApiException as e:
        print("Exception when calling ProductsApi->system_oidc_ping_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ping succeeded.  The OIDC endpoint is valid. |  -  |
**400** | The ping failed |  -  |
**401** | User need to log in first. |  -  |
**403** | User does not have permission to call this API |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_get**
> [UserGroup] usergroups_get()

Get all user groups information

Get all user groups information

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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
        group_name="group_name_example",
        ldap_group_dn="ldap_group_dn_example",
        group_type=1,
        id=1,
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    user_group = UserGroup(
        group_name="group_name_example",
        ldap_group_dn="ldap_group_dn_example",
        group_type=1,
        id=1,
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Searched for users of Harbor successfully. |  * X-Total-Count - The total count of access logs <br>  * Link - Link refers to the previous page and next page <br>  |
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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = products_api.ProductsApi(api_client)
    user = User(
        username="username_example",
        comment="comment_example",
        update_time="update_time_example",
        password="password_example",
        user_id=1,
        realname="realname_example",
        deleted=True,
        creation_time="creation_time_example",
        admin_role_in_auth=True,
        role_id=1,
        sysadmin_flag=True,
        role_name="role_name_example",
        reset_uuid="reset_uuid_example",
        salt="salt_example",
        email="email_example",
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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User created successfully. |  * Location - The URL of the created resource <br>  |
**400** | Unsatisfied with constraints of the user creation. |  -  |
**403** | User registration can only be used by admin role user when self-registration is off. |  -  |
**415** | The Media Type of the request is not supported, it has to be \&quot;application/json\&quot; |  -  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_search_get**
> [UserSearch] users_search_get(username)

Search users by username

This endpoint is to search the users by username. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search users by username, email successfully. |  * X-Total-Count - The total count of access logs <br>  * Link - Link refers to the previous page and next page <br>  |
**500** | Unexpected internal errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_cli_secret_put**
> users_user_id_cli_secret_put(user_id, inline_object)

Set CLI secret for a user.

This endpoint let user generate a new CLI secret for himself.  This API only works when auth mode is set to 'OIDC'. Once this API returns with successful status, the old secret will be invalid, as there will be only one CLI secret for a user. 

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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
        new_password="new_password_example",
        old_password="old_password_example",
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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
        comment="comment_example",
        email="email_example",
        realname="realname_example",
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

[basicAuth](../README.md#basicAuth)

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

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
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

[basicAuth](../README.md#basicAuth)

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

