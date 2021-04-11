# harbor_client.SearchApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /search | Search for projects, repositories and helm charts


# **search**
> Search search(q)

Search for projects, repositories and helm charts

The Search endpoint returns information about the projects, repositories and helm charts offered at public status or related to the current logged in user. The response includes the project, repository list and charts in a proper display order.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import search_api
from harbor_client.model.search import Search
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
    api_instance = search_api.SearchApi(api_client)
    q = "q_example" # str | Search parameter for project and repository name.

    # example passing only required values which don't have defaults set
    try:
        # Search for projects, repositories and helm charts
        api_response = api_instance.search(q)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search parameter for project and repository name. |

### Return type

[**Search**](Search.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of search results |  -  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

