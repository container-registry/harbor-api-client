# harbor_client.ScannerApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scanner**](ScannerApi.md#create_scanner) | **POST** /scanners | Create a scanner registration
[**delete_scanner**](ScannerApi.md#delete_scanner) | **DELETE** /scanners/{registration_id} | Delete a scanner registration
[**get_scanner**](ScannerApi.md#get_scanner) | **GET** /scanners/{registration_id} | Get a scanner registration details
[**get_scanner_metadata**](ScannerApi.md#get_scanner_metadata) | **GET** /scanners/{registration_id}/metadata | Get the metadata of the specified scanner registration
[**list_scanners**](ScannerApi.md#list_scanners) | **GET** /scanners | List scanner registrations
[**ping_scanner**](ScannerApi.md#ping_scanner) | **POST** /scanners/ping | Tests scanner registration settings
[**set_scanner_as_default**](ScannerApi.md#set_scanner_as_default) | **PATCH** /scanners/{registration_id} | Set system default scanner registration
[**update_scanner**](ScannerApi.md#update_scanner) | **PUT** /scanners/{registration_id} | Update a scanner registration


# **create_scanner**
> create_scanner(scanner_registration_req)

Create a scanner registration

Creats a new scanner registration with the given data. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scanner_api
from harbor_client.model.errors import Errors
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

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scanner_api.ScannerApi(api_client)
    scanner_registration_req = ScannerRegistrationReq(
        name="Trivy",
        description='''A free-to-use tool that scans container images for package vulnerabilities.
''',
        url="http://harbor-scanner-trivy:8080",
        auth="Bearer",
        access_credential="Bearer: JWTTOKENGOESHERE",
        skip_cert_verify=False,
        use_internal_addr=False,
        disabled=False,
    ) # ScannerRegistrationReq | A scanner registration to be created.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a scanner registration
        api_instance.create_scanner(scanner_registration_req)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->create_scanner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a scanner registration
        api_instance.create_scanner(scanner_registration_req, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->create_scanner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scanner_registration_req** | [**ScannerRegistrationReq**](ScannerRegistrationReq.md)| A scanner registration to be created. |
 **x_request_id** | **str**| An unique ID for the request | [optional]

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
**201** | Created successfully |  * Location - The URL of the created resource <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scanner**
> ScannerRegistration delete_scanner(registration_id)

Delete a scanner registration

Deletes the specified scanner registration. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scanner_api
from harbor_client.model.scanner_registration import ScannerRegistration
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
    api_instance = scanner_api.ScannerApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifier.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a scanner registration
        api_response = api_instance.delete_scanner(registration_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->delete_scanner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a scanner registration
        api_response = api_instance.delete_scanner(registration_id, x_request_id=x_request_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->delete_scanner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. |
 **x_request_id** | **str**| An unique ID for the request | [optional]

### Return type

[**ScannerRegistration**](ScannerRegistration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted successfully and return the deleted registration |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scanner**
> ScannerRegistration get_scanner(registration_id)

Get a scanner registration details

Retruns the details of the specified scanner registration. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scanner_api
from harbor_client.model.scanner_registration import ScannerRegistration
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
    api_instance = scanner_api.ScannerApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifer.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a scanner registration details
        api_response = api_instance.get_scanner(registration_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->get_scanner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a scanner registration details
        api_response = api_instance.get_scanner(registration_id, x_request_id=x_request_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->get_scanner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifer. |
 **x_request_id** | **str**| An unique ID for the request | [optional]

### Return type

[**ScannerRegistration**](ScannerRegistration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the scanner registration. |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scanner_metadata**
> ScannerAdapterMetadata get_scanner_metadata(registration_id)

Get the metadata of the specified scanner registration

Get the metadata of the specified scanner registration, including the capabilities and customized properties. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scanner_api
from harbor_client.model.errors import Errors
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

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scanner_api.ScannerApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifier.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the metadata of the specified scanner registration
        api_response = api_instance.get_scanner_metadata(registration_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->get_scanner_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the metadata of the specified scanner registration
        api_response = api_instance.get_scanner_metadata(registration_id, x_request_id=x_request_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->get_scanner_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. |
 **x_request_id** | **str**| An unique ID for the request | [optional]

### Return type

[**ScannerAdapterMetadata**](ScannerAdapterMetadata.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata of the specified scanner adapter |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scanners**
> [ScannerRegistration] list_scanners()

List scanner registrations

Returns a list of currently configured scanner registrations. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scanner_api
from harbor_client.model.scanner_registration import ScannerRegistration
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
    api_instance = scanner_api.ScannerApi(api_client)
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    q = "q_example" # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
    sort = "sort_example" # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List scanner registrations
        api_response = api_instance.list_scanners(x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->list_scanners: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional]
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional]
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10

### Return type

[**[ScannerRegistration]**](ScannerRegistration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of scanner registrations. |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_scanner**
> ping_scanner(scanner_registration_settings)

Tests scanner registration settings

Pings scanner adapter to test endpoint URL and authorization settings. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scanner_api
from harbor_client.model.scanner_registration_settings import ScannerRegistrationSettings
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
    api_instance = scanner_api.ScannerApi(api_client)
    scanner_registration_settings = ScannerRegistrationSettings(
        name="Trivy",
        url="http://harbor-scanner-trivy:8080",
        auth="",
        access_credential="Bearer: JWTTOKENGOESHERE",
    ) # ScannerRegistrationSettings | A scanner registration settings to be tested.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Tests scanner registration settings
        api_instance.ping_scanner(scanner_registration_settings)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->ping_scanner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Tests scanner registration settings
        api_instance.ping_scanner(scanner_registration_settings, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->ping_scanner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scanner_registration_settings** | [**ScannerRegistrationSettings**](ScannerRegistrationSettings.md)| A scanner registration settings to be tested. |
 **x_request_id** | **str**| An unique ID for the request | [optional]

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
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_scanner_as_default**
> set_scanner_as_default(registration_id, is_default)

Set system default scanner registration

Set the specified scanner registration as the system default one. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scanner_api
from harbor_client.model.is_default import IsDefault
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
    api_instance = scanner_api.ScannerApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifier.
    is_default = IsDefault(
        is_default=True,
    ) # IsDefault | 

    # example passing only required values which don't have defaults set
    try:
        # Set system default scanner registration
        api_instance.set_scanner_as_default(registration_id, is_default)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->set_scanner_as_default: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. |
 **is_default** | [**IsDefault**](IsDefault.md)|  |

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
**200** | Successfully set the specified scanner registration as system default |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scanner**
> update_scanner(registration_id, scanner_registration_req)

Update a scanner registration

Updates the specified scanner registration. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scanner_api
from harbor_client.model.errors import Errors
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

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scanner_api.ScannerApi(api_client)
    registration_id = "registration_id_example" # str | The scanner registration identifier.
    scanner_registration_req = ScannerRegistrationReq(
        name="Trivy",
        description='''A free-to-use tool that scans container images for package vulnerabilities.
''',
        url="http://harbor-scanner-trivy:8080",
        auth="Bearer",
        access_credential="Bearer: JWTTOKENGOESHERE",
        skip_cert_verify=False,
        use_internal_addr=False,
        disabled=False,
    ) # ScannerRegistrationReq | A scanner registraiton to be updated.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a scanner registration
        api_instance.update_scanner(registration_id, scanner_registration_req)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->update_scanner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a scanner registration
        api_instance.update_scanner(registration_id, scanner_registration_req, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ScannerApi->update_scanner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. |
 **scanner_registration_req** | [**ScannerRegistrationReq**](ScannerRegistrationReq.md)| A scanner registraiton to be updated. |
 **x_request_id** | **str**| An unique ID for the request | [optional]

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
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

