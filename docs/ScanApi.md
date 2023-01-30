# harbor_client.ScanApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_log**](ScanApi.md#get_report_log) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/scan/{report_id}/log | Get the log of the scan report
[**scan_artifact**](ScanApi.md#scan_artifact) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/scan | Scan the artifact
[**stop_scan_artifact**](ScanApi.md#stop_scan_artifact) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/scan/stop | Cancelling a scan job for a particular artifact


# **get_report_log**
> str get_report_log(project_name, repository_name, reference, report_id, x_request_id=x_request_id)

Get the log of the scan report

Get the log of the scan report

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
api_instance = harbor_client.ScanApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
report_id = 'report_id_example' # str | The report id to get the log
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the log of the scan report
    api_response = api_instance.get_report_log(project_name, repository_name, reference, report_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_artifact**
> scan_artifact(project_name, repository_name, reference, x_request_id=x_request_id)

Scan the artifact

Scan the specified artifact

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
api_instance = harbor_client.ScanApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Scan the artifact
    api_instance.scan_artifact(project_name, repository_name, reference, x_request_id=x_request_id)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_scan_artifact**
> stop_scan_artifact(project_name, repository_name, reference, x_request_id=x_request_id)

Cancelling a scan job for a particular artifact

Cancelling a scan job for a particular artifact

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
api_instance = harbor_client.ScanApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Cancelling a scan job for a particular artifact
    api_instance.stop_scan_artifact(project_name, repository_name, reference, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ScanApi->stop_scan_artifact: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

