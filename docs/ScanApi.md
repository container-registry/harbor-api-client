# harbor_client.ScanApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_log**](ScanApi.md#get_report_log) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/scan/{report_id}/log | Get the log of the scan report
[**scan_artifact**](ScanApi.md#scan_artifact) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/scan | Scan the artifact


# **get_report_log**
> str get_report_log(project_name, repository_name, reference, report_id)

Get the log of the scan report

Get the log of the scan report

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scan_api
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
    api_instance = scan_api.ScanApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    reference = "reference_example" # str | The reference of the artifact, can be digest or tag
    report_id = "report_id_example" # str | The report id to get the log
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the log of the scan report
        api_response = api_instance.get_report_log(project_name, repository_name, reference, report_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScanApi->get_report_log: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the log of the scan report
        api_response = api_instance.get_report_log(project_name, repository_name, reference, report_id, x_request_id=x_request_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ScanApi->get_report_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **reference** | **str**| The reference of the artifact, can be digest or tag |
 **report_id** | **str**| The report id to get the log |
 **x_request_id** | **str**| An unique ID for the request | [optional]

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully get scan log file |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_artifact**
> scan_artifact(project_name, repository_name, reference)

Scan the artifact

Scan the specified artifact

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import scan_api
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
    api_instance = scan_api.ScanApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    reference = "reference_example" # str | The reference of the artifact, can be digest or tag
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Scan the artifact
        api_instance.scan_artifact(project_name, repository_name, reference)
    except harbor_client.ApiException as e:
        print("Exception when calling ScanApi->scan_artifact: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Scan the artifact
        api_instance.scan_artifact(project_name, repository_name, reference, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ScanApi->scan_artifact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **reference** | **str**| The reference of the artifact, can be digest or tag |
 **x_request_id** | **str**| An unique ID for the request | [optional]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

