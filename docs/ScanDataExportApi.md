# harbor_client.ScanDataExportApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_scan_data**](ScanDataExportApi.md#download_scan_data) | **GET** /export/cve/download/{execution_id} | Download the scan data export file
[**export_scan_data**](ScanDataExportApi.md#export_scan_data) | **POST** /export/cve | Export scan data for selected projects
[**get_scan_data_export_execution**](ScanDataExportApi.md#get_scan_data_export_execution) | **GET** /export/cve/execution/{execution_id} | Get the specific scan data export execution
[**get_scan_data_export_execution_list**](ScanDataExportApi.md#get_scan_data_export_execution_list) | **GET** /export/cve/executions | Get a list of specific scan data export execution jobs for a specified user


# **download_scan_data**
> file download_scan_data(execution_id, x_request_id=x_request_id, format=format)

Download the scan data export file

Download the scan data report. Default format is CSV

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
api_instance = harbor_client.ScanDataExportApi(harbor_client.ApiClient(configuration))
execution_id = 56 # int | Execution ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
format = 'format_example' # str | The format of the data to be exported. e.g. CSV or PDF (optional)

try:
    # Download the scan data export file
    api_response = api_instance.download_scan_data(execution_id, x_request_id=x_request_id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanDataExportApi->download_scan_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **int**| Execution ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **format** | **str**| The format of the data to be exported. e.g. CSV or PDF | [optional] 

### Return type

[**file**](file.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_scan_data**
> ScanDataExportJob export_scan_data(x_scan_data_type, criteria, x_request_id=x_request_id)

Export scan data for selected projects

Export scan data for selected projects

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
api_instance = harbor_client.ScanDataExportApi(harbor_client.ApiClient(configuration))
x_scan_data_type = 'x_scan_data_type_example' # str | The type of scan data to export
criteria = harbor_client.ScanDataExportRequest() # ScanDataExportRequest | The criteria for the export
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Export scan data for selected projects
    api_response = api_instance.export_scan_data(x_scan_data_type, criteria, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanDataExportApi->export_scan_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_scan_data_type** | **str**| The type of scan data to export | 
 **criteria** | [**ScanDataExportRequest**](ScanDataExportRequest.md)| The criteria for the export | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ScanDataExportJob**](ScanDataExportJob.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scan_data_export_execution**
> ScanDataExportExecution get_scan_data_export_execution(execution_id, x_request_id=x_request_id)

Get the specific scan data export execution

Get the scan data export execution specified by ID

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
api_instance = harbor_client.ScanDataExportApi(harbor_client.ApiClient(configuration))
execution_id = 56 # int | Execution ID
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the specific scan data export execution
    api_response = api_instance.get_scan_data_export_execution(execution_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanDataExportApi->get_scan_data_export_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **int**| Execution ID | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ScanDataExportExecution**](ScanDataExportExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scan_data_export_execution_list**
> ScanDataExportExecutionList get_scan_data_export_execution_list(x_request_id=x_request_id)

Get a list of specific scan data export execution jobs for a specified user

Get a list of specific scan data export execution jobs for a specified user

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
api_instance = harbor_client.ScanDataExportApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get a list of specific scan data export execution jobs for a specified user
    api_response = api_instance.get_scan_data_export_execution_list(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanDataExportApi->get_scan_data_export_execution_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ScanDataExportExecutionList**](ScanDataExportExecutionList.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

