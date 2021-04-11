# harbor_client.ChartRepositoryApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_attahced_labels_of_chart**](ChartRepositoryApi.md#list_attahced_labels_of_chart) | **GET** /chartrepo/{repo}/charts/{name}/{version}/labels | Return the attahced labels of chart.
[**mark_label_to_chart**](ChartRepositoryApi.md#mark_label_to_chart) | **POST** /chartrepo/{repo}/charts/{name}/{version}/labels | Mark label to chart.
[**remove_label_from_chart**](ChartRepositoryApi.md#remove_label_from_chart) | **DELETE** /chartrepo/{repo}/charts/{name}/{version}/labels/{id} | Remove label from chart.


# **list_attahced_labels_of_chart**
> list_attahced_labels_of_chart(repo, name, version)

Return the attahced labels of chart.

Return the attahced labels of the specified chart version.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import chart_repository_api
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
    api_instance = chart_repository_api.ChartRepositoryApi(api_client)
    repo = "repo_example" # str | The project name
    name = "name_example" # str | The chart name
    version = "version_example" # str | The chart version

    # example passing only required values which don't have defaults set
    try:
        # Return the attahced labels of chart.
        api_instance.list_attahced_labels_of_chart(repo, name, version)
    except harbor_client.ApiException as e:
        print("Exception when calling ChartRepositoryApi->list_attahced_labels_of_chart: %s\n" % e)
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

# **mark_label_to_chart**
> mark_label_to_chart(repo, name, version, label)

Mark label to chart.

Mark label to the specified chart version.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import chart_repository_api
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
    api_instance = chart_repository_api.ChartRepositoryApi(api_client)
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
        api_instance.mark_label_to_chart(repo, name, version, label)
    except harbor_client.ApiException as e:
        print("Exception when calling ChartRepositoryApi->mark_label_to_chart: %s\n" % e)
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

# **remove_label_from_chart**
> remove_label_from_chart(repo, name, version, id)

Remove label from chart.

Remove label from the specified chart version.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import chart_repository_api
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
    api_instance = chart_repository_api.ChartRepositoryApi(api_client)
    repo = "repo_example" # str | The project name
    name = "name_example" # str | The chart name
    version = "version_example" # str | The chart version
    id = 1 # int | The label ID

    # example passing only required values which don't have defaults set
    try:
        # Remove label from chart.
        api_instance.remove_label_from_chart(repo, name, version, id)
    except harbor_client.ApiException as e:
        print("Exception when calling ChartRepositoryApi->remove_label_from_chart: %s\n" % e)
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

