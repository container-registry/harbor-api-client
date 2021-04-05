# harbor_client.ScannersApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_scanner_candidates_get**](ScannersApi.md#projects_project_id_scanner_candidates_get) | **GET** /projects/{project_id}/scanner/candidates | Get scanner registration candidates for configurating project level scanner
[**projects_project_id_scanner_get**](ScannersApi.md#projects_project_id_scanner_get) | **GET** /projects/{project_id}/scanner | Get project level scanner
[**projects_project_id_scanner_put**](ScannersApi.md#projects_project_id_scanner_put) | **PUT** /projects/{project_id}/scanner | Configure scanner for the specified project
[**scanners_get**](ScannersApi.md#scanners_get) | **GET** /scanners | List scanner registrations
[**scanners_ping_post**](ScannersApi.md#scanners_ping_post) | **POST** /scanners/ping | Tests scanner registration settings
[**scanners_post**](ScannersApi.md#scanners_post) | **POST** /scanners | Create a scanner registration
[**scanners_registration_id_delete**](ScannersApi.md#scanners_registration_id_delete) | **DELETE** /scanners/{registration_id} | Delete a scanner registration
[**scanners_registration_id_get**](ScannersApi.md#scanners_registration_id_get) | **GET** /scanners/{registration_id} | Get a scanner registration details
[**scanners_registration_id_metadata_get**](ScannersApi.md#scanners_registration_id_metadata_get) | **GET** /scanners/{registration_id}/metadata | Get the metadata of the specified scanner registration
[**scanners_registration_id_patch**](ScannersApi.md#scanners_registration_id_patch) | **PATCH** /scanners/{registration_id} | Set system default scanner registration
[**scanners_registration_id_put**](ScannersApi.md#scanners_registration_id_put) | **PUT** /scanners/{registration_id} | Update a scanner registration


# **projects_project_id_scanner_candidates_get**
> [ScannerRegistration] projects_project_id_scanner_candidates_get(project_id)

Get scanner registration candidates for configurating project level scanner

Retrieve the system configured scanner registrations as candidates of setting project level scanner. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import scanners_api
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
    api_instance = scanners_api.ScannersApi(api_client)
    project_id = 1 # int | The project identifier.
    page = 1 # int | The page number. (optional)
    page_size = 1 # int | The size of per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get scanner registration candidates for configurating project level scanner
        api_response = api_instance.projects_project_id_scanner_candidates_get(project_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannersApi->projects_project_id_scanner_candidates_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get scanner registration candidates for configurating project level scanner
        api_response = api_instance.projects_project_id_scanner_candidates_get(project_id, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannersApi->projects_project_id_scanner_candidates_get: %s\n" % e)
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
from harbor_client.api import scanners_api
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
    api_instance = scanners_api.ScannersApi(api_client)
    project_id = 1 # int | The project identifier.

    # example passing only required values which don't have defaults set
    try:
        # Get project level scanner
        api_response = api_instance.projects_project_id_scanner_get(project_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannersApi->projects_project_id_scanner_get: %s\n" % e)
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

# **projects_project_id_scanner_put**
> projects_project_id_scanner_put(project_id, project_scanner)

Configure scanner for the specified project

Set one of the system configured scanner registration as the indepndent scanner of the specified project.

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import scanners_api
from harbor_client.model.project_scanner import ProjectScanner
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
    api_instance = scanners_api.ScannersApi(api_client)
    project_id = 1 # int | The project identifier.
    project_scanner = ProjectScanner(
        uuid="uuid_example",
    ) # ProjectScanner | 

    # example passing only required values which don't have defaults set
    try:
        # Configure scanner for the specified project
        api_instance.projects_project_id_scanner_put(project_id, project_scanner)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannersApi->projects_project_id_scanner_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project identifier. |
 **project_scanner** | [**ProjectScanner**](ProjectScanner.md)|  |

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
**200** | Successfully set the project level scanner |  -  |
**400** | Bad project ID |  -  |
**401** | Unauthorized request |  -  |
**403** | Request is not allowed |  -  |
**404** | The requested object is not found |  -  |
**500** | Internal server error happened |  -  |

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
from harbor_client.api import scanners_api
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
    api_instance = scanners_api.ScannersApi(api_client)
    page = 1 # int | The page number. (optional)
    page_size = 1 # int | The size of per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List scanner registrations
        api_response = api_instance.scanners_get(page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannersApi->scanners_get: %s\n" % e)
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
from harbor_client.api import scanners_api
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
    api_instance = scanners_api.ScannersApi(api_client)
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
        print("Exception when calling ScannersApi->scanners_ping_post: %s\n" % e)
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

# **scanners_post**
> scanners_post(scanner_registration_req)

Create a scanner registration

Creats a new scanner registration with the given data. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import scanners_api
from harbor_client.model.scanner_registration_req import ScannerRegistrationReq
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
    api_instance = scanners_api.ScannersApi(api_client)
    scanner_registration_req = ScannerRegistrationReq(
        name="Clair",
        url="http://harbor-scanner-clair:8080",
        access_credential="Bearer: JWTTOKENGOESHERE",
        auth="Bearer",
        disabled=False,
        use_internal_addr=False,
        skip_cert_verify=False,
        description='''A free-to-use tool that scans container images for package vulnerabilities.
''',
    ) # ScannerRegistrationReq | A scanner registration to be created.

    # example passing only required values which don't have defaults set
    try:
        # Create a scanner registration
        api_instance.scanners_post(scanner_registration_req)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannersApi->scanners_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scanner_registration_req** | [**ScannerRegistrationReq**](ScannerRegistrationReq.md)| A scanner registration to be created. |

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
**201** | Created successfully |  * Location - The URL of the created resource <br>  |
**400** | Bad registration request |  -  |
**401** | Unauthorized request |  -  |
**403** | Request is not allowed, system role required |  -  |
**500** | Internal server error happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_registration_id_delete**
> ScannerRegistration scanners_registration_id_delete(registration_id)

Delete a scanner registration

Deletes the specified scanner registration. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import scanners_api
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
    api_instance = scanners_api.ScannersApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifier.

    # example passing only required values which don't have defaults set
    try:
        # Delete a scanner registration
        api_response = api_instance.scanners_registration_id_delete(registration_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannersApi->scanners_registration_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. |

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
**200** | Deleted successfully and return the deleted registration |  -  |
**401** | Unauthorized request |  -  |
**403** | Request is not allowed, system role required or registration is immutable |  -  |
**404** | The requested object is not found |  -  |
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
from harbor_client.api import scanners_api
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
    api_instance = scanners_api.ScannersApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifer.

    # example passing only required values which don't have defaults set
    try:
        # Get a scanner registration details
        api_response = api_instance.scanners_registration_id_get(registration_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannersApi->scanners_registration_id_get: %s\n" % e)
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
from harbor_client.api import scanners_api
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
    api_instance = scanners_api.ScannersApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifier.

    # example passing only required values which don't have defaults set
    try:
        # Get the metadata of the specified scanner registration
        api_response = api_instance.scanners_registration_id_metadata_get(registration_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannersApi->scanners_registration_id_metadata_get: %s\n" % e)
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

# **scanners_registration_id_patch**
> scanners_registration_id_patch(registration_id, is_default)

Set system default scanner registration

Set the specified scanner registration as the system default one. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import scanners_api
from harbor_client.model.is_default import IsDefault
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
    api_instance = scanners_api.ScannersApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifier.
    is_default = IsDefault(
        is_default=True,
    ) # IsDefault | 

    # example passing only required values which don't have defaults set
    try:
        # Set system default scanner registration
        api_instance.scanners_registration_id_patch(registration_id, is_default)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannersApi->scanners_registration_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. |
 **is_default** | [**IsDefault**](IsDefault.md)|  |

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
**200** | Successfully set the specified scanner registration as system default |  -  |
**401** | Unauthorized request |  -  |
**403** | Request is not allowed |  -  |
**500** | Internal server error happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_registration_id_put**
> scanners_registration_id_put(registration_id, scanner_registration_req)

Update a scanner registration

Updates the specified scanner registration. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import harbor_client
from harbor_client.api import scanners_api
from harbor_client.model.scanner_registration_req import ScannerRegistrationReq
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
    api_instance = scanners_api.ScannersApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifier.
    scanner_registration_req = ScannerRegistrationReq(
        name="Clair",
        url="http://harbor-scanner-clair:8080",
        access_credential="Bearer: JWTTOKENGOESHERE",
        auth="Bearer",
        disabled=False,
        use_internal_addr=False,
        skip_cert_verify=False,
        description='''A free-to-use tool that scans container images for package vulnerabilities.
''',
    ) # ScannerRegistrationReq | A scanner registraiton to be updated.

    # example passing only required values which don't have defaults set
    try:
        # Update a scanner registration
        api_instance.scanners_registration_id_put(registration_id, scanner_registration_req)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannersApi->scanners_registration_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. |
 **scanner_registration_req** | [**ScannerRegistrationReq**](ScannerRegistrationReq.md)| A scanner registraiton to be updated. |

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
**200** | Updated successfully |  -  |
**401** | Unauthorized request |  -  |
**403** | Request is not allowed, system role required |  -  |
**404** | The requested object is not found |  -  |
**500** | Internal server error happened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

