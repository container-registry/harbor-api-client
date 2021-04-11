# harbor_client.WebhookApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_policy_of_project**](WebhookApi.md#create_webhook_policy_of_project) | **POST** /projects/{project_name_or_id}/webhook/policies | Create project webhook policy.
[**delete_webhook_policy_of_project**](WebhookApi.md#delete_webhook_policy_of_project) | **DELETE** /projects/{project_name_or_id}/webhook/policies/{webhook_policy_id} | Delete webhook policy of a project
[**get_supported_event_types**](WebhookApi.md#get_supported_event_types) | **GET** /projects/{project_name_or_id}/webhook/events | Get supported event types and notify types.
[**get_webhook_policy_of_project**](WebhookApi.md#get_webhook_policy_of_project) | **GET** /projects/{project_name_or_id}/webhook/policies/{webhook_policy_id} | Get project webhook policy
[**last_trigger**](WebhookApi.md#last_trigger) | **GET** /projects/{project_name_or_id}/webhook/lasttrigger | Get project webhook policy last trigger info
[**list_webhook_policies_of_project**](WebhookApi.md#list_webhook_policies_of_project) | **GET** /projects/{project_name_or_id}/webhook/policies | List project webhook policies.
[**update_webhook_policy_of_project**](WebhookApi.md#update_webhook_policy_of_project) | **PUT** /projects/{project_name_or_id}/webhook/policies/{webhook_policy_id} | Update webhook policy of a project.


# **create_webhook_policy_of_project**
> create_webhook_policy_of_project(project_name_or_id, webhook_policy)

Create project webhook policy.

This endpoint create a webhook policy if the project does not have one. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import webhook_api
from harbor_client.model.webhook_policy import WebhookPolicy
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
    api_instance = webhook_api.WebhookApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    webhook_policy = WebhookPolicy(
        id=1,
        name="name_example",
        description="description_example",
        project_id=1,
        targets=[
            WebhookTargetObject(
                type="type_example",
                address="address_example",
                auth_header="auth_header_example",
                skip_cert_verify=True,
            ),
        ],
        event_types=[
            "event_types_example",
        ],
        creator="creator_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        enabled=True,
    ) # WebhookPolicy | Properties \"targets\" and \"event_types\" needed.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Create project webhook policy.
        api_instance.create_webhook_policy_of_project(project_name_or_id, webhook_policy)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->create_webhook_policy_of_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create project webhook policy.
        api_instance.create_webhook_policy_of_project(project_name_or_id, webhook_policy, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->create_webhook_policy_of_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **webhook_policy** | [**WebhookPolicy**](WebhookPolicy.md)| Properties \&quot;targets\&quot; and \&quot;event_types\&quot; needed. |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

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
**201** | Project webhook policy create successfully. |  * X-Request-Id - The ID of the corresponding request for the response <br>  * Location - The URL of the created resource <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_policy_of_project**
> delete_webhook_policy_of_project(project_name_or_id, webhook_policy_id)

Delete webhook policy of a project

This endpoint is aimed to delete webhookpolicy of a project. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import webhook_api
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
    api_instance = webhook_api.WebhookApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    webhook_policy_id = 1 # int | The ID of the webhook policy
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete webhook policy of a project
        api_instance.delete_webhook_policy_of_project(project_name_or_id, webhook_policy_id)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->delete_webhook_policy_of_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete webhook policy of a project
        api_instance.delete_webhook_policy_of_project(project_name_or_id, webhook_policy_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->delete_webhook_policy_of_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **webhook_policy_id** | **int**| The ID of the webhook policy |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

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
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_event_types**
> SupportedWebhookEventTypes get_supported_event_types(project_name_or_id)

Get supported event types and notify types.

Get supportted event types and notify types.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import webhook_api
from harbor_client.model.supported_webhook_event_types import SupportedWebhookEventTypes
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
    api_instance = webhook_api.WebhookApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get supported event types and notify types.
        api_response = api_instance.get_supported_event_types(project_name_or_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->get_supported_event_types: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get supported event types and notify types.
        api_response = api_instance.get_supported_event_types(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->get_supported_event_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

[**SupportedWebhookEventTypes**](SupportedWebhookEventTypes.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_policy_of_project**
> WebhookPolicy get_webhook_policy_of_project(project_name_or_id, webhook_policy_id)

Get project webhook policy

This endpoint returns specified webhook policy of a project. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import webhook_api
from harbor_client.model.webhook_policy import WebhookPolicy
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
    api_instance = webhook_api.WebhookApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    webhook_policy_id = 1 # int | The ID of the webhook policy
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get project webhook policy
        api_response = api_instance.get_webhook_policy_of_project(project_name_or_id, webhook_policy_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->get_webhook_policy_of_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get project webhook policy
        api_response = api_instance.get_webhook_policy_of_project(project_name_or_id, webhook_policy_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->get_webhook_policy_of_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **webhook_policy_id** | **int**| The ID of the webhook policy |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

[**WebhookPolicy**](WebhookPolicy.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get webhook policy successfully. |  -  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **last_trigger**
> [WebhookLastTrigger] last_trigger(project_name_or_id)

Get project webhook policy last trigger info

This endpoint returns last trigger information of project webhook policy. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import webhook_api
from harbor_client.model.errors import Errors
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

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get project webhook policy last trigger info
        api_response = api_instance.last_trigger(project_name_or_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->last_trigger: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get project webhook policy last trigger info
        api_response = api_instance.last_trigger(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->last_trigger: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

[**[WebhookLastTrigger]**](WebhookLastTrigger.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test webhook connection successfully. |  -  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_policies_of_project**
> [WebhookPolicy] list_webhook_policies_of_project(project_name_or_id)

List project webhook policies.

This endpoint returns webhook policies of a project. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import webhook_api
from harbor_client.model.webhook_policy import WebhookPolicy
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
    api_instance = webhook_api.WebhookApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False
    sort = "sort_example" # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
    q = "q_example" # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # List project webhook policies.
        api_response = api_instance.list_webhook_policies_of_project(project_name_or_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->list_webhook_policies_of_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List project webhook policies.
        api_response = api_instance.list_webhook_policies_of_project(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, sort=sort, q=q, page=page, page_size=page_size)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->list_webhook_policies_of_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional]
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional]
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10

### Return type

[**[WebhookPolicy]**](WebhookPolicy.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_policy_of_project**
> update_webhook_policy_of_project(project_name_or_id, webhook_policy_id, webhook_policy)

Update webhook policy of a project.

This endpoint is aimed to update the webhook policy of a project. 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import webhook_api
from harbor_client.model.webhook_policy import WebhookPolicy
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
    api_instance = webhook_api.WebhookApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    webhook_policy_id = 1 # int | The ID of the webhook policy
    webhook_policy = WebhookPolicy(
        id=1,
        name="name_example",
        description="description_example",
        project_id=1,
        targets=[
            WebhookTargetObject(
                type="type_example",
                address="address_example",
                auth_header="auth_header_example",
                skip_cert_verify=True,
            ),
        ],
        event_types=[
            "event_types_example",
        ],
        creator="creator_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        enabled=True,
    ) # WebhookPolicy | All properties needed except \"id\", \"project_id\", \"creation_time\", \"update_time\".
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update webhook policy of a project.
        api_instance.update_webhook_policy_of_project(project_name_or_id, webhook_policy_id, webhook_policy)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->update_webhook_policy_of_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update webhook policy of a project.
        api_instance.update_webhook_policy_of_project(project_name_or_id, webhook_policy_id, webhook_policy, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    except harbor_client.ApiException as e:
        print("Exception when calling WebhookApi->update_webhook_policy_of_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **webhook_policy_id** | **int**| The ID of the webhook policy |
 **webhook_policy** | [**WebhookPolicy**](WebhookPolicy.md)| All properties needed except \&quot;id\&quot;, \&quot;project_id\&quot;, \&quot;creation_time\&quot;, \&quot;update_time\&quot;. |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

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
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

