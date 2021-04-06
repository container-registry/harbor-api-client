# harbor_client.ArtifactApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_label**](ArtifactApi.md#add_label) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/labels | Add label to artifact
[**copy_artifact**](ArtifactApi.md#copy_artifact) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts | Copy artifact
[**create_tag**](ArtifactApi.md#create_tag) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags | Create tag
[**delete_artifact**](ArtifactApi.md#delete_artifact) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference} | Delete the specific artifact
[**delete_tag**](ArtifactApi.md#delete_tag) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags/{tag_name} | Delete tag
[**get_addition**](ArtifactApi.md#get_addition) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/additions/{addition} | Get the addition of the specific artifact
[**get_artifact**](ArtifactApi.md#get_artifact) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference} | Get the specific artifact
[**get_vulnerabilities_addition**](ArtifactApi.md#get_vulnerabilities_addition) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/additions/vulnerabilities | Get the vulnerabilities addition of the specific artifact
[**list_artifacts**](ArtifactApi.md#list_artifacts) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts | List artifacts
[**list_tags**](ArtifactApi.md#list_tags) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags | List tags
[**remove_label**](ArtifactApi.md#remove_label) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/labels/{label_id} | Remove label from artifact


# **add_label**
> add_label(project_name, repository_name, reference, label)

Add label to artifact

Add label to the specified artiact.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import artifact_api
from harbor_client.model.label import Label
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
    api_instance = artifact_api.ArtifactApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    reference = "reference_example" # str | The reference of the artifact, can be digest or tag
    label = Label(
        update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        description="description_example",
        color="color_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        scope="scope_example",
        project_id=1,
        id=1,
        name="name_example",
    ) # Label | The label that added to the artifact. Only the ID property is needed.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add label to artifact
        api_instance.add_label(project_name, repository_name, reference, label)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->add_label: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add label to artifact
        api_instance.add_label(project_name, repository_name, reference, label, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->add_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **reference** | **str**| The reference of the artifact, can be digest or tag |
 **label** | [**Label**](Label.md)| The label that added to the artifact. Only the ID property is needed. |
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
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**409** | Conflict |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_artifact**
> copy_artifact(project_name, repository_name, _from)

Copy artifact

Copy the artifact specified in the \"from\" parameter to the repository.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import artifact_api
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
    api_instance = artifact_api.ArtifactApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    _from = "from_example" # str | The artifact from which the new artifact is copied from, the format should be \"project/repository:tag\" or \"project/repository@digest\".
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Copy artifact
        api_instance.copy_artifact(project_name, repository_name, _from)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->copy_artifact: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Copy artifact
        api_instance.copy_artifact(project_name, repository_name, _from, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->copy_artifact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **_from** | **str**| The artifact from which the new artifact is copied from, the format should be \&quot;project/repository:tag\&quot; or \&quot;project/repository@digest\&quot;. |
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
**201** | Created |  * X-Request-Id - The ID of the corresponding request for the response <br>  * Location - The location of the resource <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**405** | Method not allowed |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag**
> create_tag(project_name, repository_name, reference, tag)

Create tag

Create a tag for the specified artifact

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import artifact_api
from harbor_client.model.errors import Errors
from harbor_client.model.tag import Tag
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
    api_instance = artifact_api.ArtifactApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    reference = "reference_example" # str | The reference of the artifact, can be digest or tag
    tag = Tag(
        repository_id=1,
        name="name_example",
        push_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        pull_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        signed=True,
        id=1,
        immutable=True,
        artifact_id=1,
    ) # Tag | The JSON object of tag.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create tag
        api_instance.create_tag(project_name, repository_name, reference, tag)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->create_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create tag
        api_instance.create_tag(project_name, repository_name, reference, tag, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->create_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **reference** | **str**| The reference of the artifact, can be digest or tag |
 **tag** | [**Tag**](Tag.md)| The JSON object of tag. |
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
**201** | Created |  * X-Request-Id - The ID of the corresponding request for the response <br>  * Location - The location of the resource <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**405** | Method not allowed |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**409** | Conflict |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact**
> delete_artifact(project_name, repository_name, reference)

Delete the specific artifact

Delete the artifact specified by the reference under the project and repository. The reference can be digest or tag

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import artifact_api
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
    api_instance = artifact_api.ArtifactApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    reference = "reference_example" # str | The reference of the artifact, can be digest or tag
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete the specific artifact
        api_instance.delete_artifact(project_name, repository_name, reference)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->delete_artifact: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete the specific artifact
        api_instance.delete_artifact(project_name, repository_name, reference, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->delete_artifact: %s\n" % e)
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
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(project_name, repository_name, reference, tag_name)

Delete tag

Delete the tag of the specified artifact

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import artifact_api
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
    api_instance = artifact_api.ArtifactApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    reference = "reference_example" # str | The reference of the artifact, can be digest or tag
    tag_name = "tag_name_example" # str | The name of the tag
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete tag
        api_instance.delete_tag(project_name, repository_name, reference, tag_name)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->delete_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete tag
        api_instance.delete_tag(project_name, repository_name, reference, tag_name, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->delete_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **reference** | **str**| The reference of the artifact, can be digest or tag |
 **tag_name** | **str**| The name of the tag |
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
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addition**
> str get_addition(project_name, repository_name, reference, addition)

Get the addition of the specific artifact

Get the addition of the artifact specified by the reference under the project and repository.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import artifact_api
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
    api_instance = artifact_api.ArtifactApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    reference = "reference_example" # str | The reference of the artifact, can be digest or tag
    addition = "build_history" # str | The type of addition.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the addition of the specific artifact
        api_response = api_instance.get_addition(project_name, repository_name, reference, addition)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->get_addition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the addition of the specific artifact
        api_response = api_instance.get_addition(project_name, repository_name, reference, addition, x_request_id=x_request_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->get_addition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **reference** | **str**| The reference of the artifact, can be digest or tag |
 **addition** | **str**| The type of addition. |
 **x_request_id** | **str**| An unique ID for the request | [optional]

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Type - The content type of the addition <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact**
> Artifact get_artifact(project_name, repository_name, reference)

Get the specific artifact

Get the artifact specified by the reference under the project and repository. The reference can be digest or tag.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import artifact_api
from harbor_client.model.artifact import Artifact
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
    api_instance = artifact_api.ArtifactApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    reference = "reference_example" # str | The reference of the artifact, can be digest or tag
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10
    x_accept_vulnerabilities = "application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0" # str | A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports 'application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0' and 'application/vnd.security.vulnerability.report; version=1.1' (optional) if omitted the server will use the default value of "application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0"
    with_tag = True # bool | Specify whether the tags are inclued inside the returning artifacts (optional) if omitted the server will use the default value of True
    with_label = False # bool | Specify whether the labels are inclued inside the returning artifacts (optional) if omitted the server will use the default value of False
    with_scan_overview = False # bool | Specify whether the scan overview is inclued inside the returning artifacts (optional) if omitted the server will use the default value of False
    with_signature = False # bool | Specify whether the signature is inclued inside the returning artifacts (optional) if omitted the server will use the default value of False
    with_immutable_status = False # bool | Specify whether the immutable status is inclued inside the tags of the returning artifacts. Only works when setting \"with_tag=true\" (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get the specific artifact
        api_response = api_instance.get_artifact(project_name, repository_name, reference)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->get_artifact: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the specific artifact
        api_response = api_instance.get_artifact(project_name, repository_name, reference, x_request_id=x_request_id, page=page, page_size=page_size, x_accept_vulnerabilities=x_accept_vulnerabilities, with_tag=with_tag, with_label=with_label, with_scan_overview=with_scan_overview, with_signature=with_signature, with_immutable_status=with_immutable_status)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->get_artifact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **reference** | **str**| The reference of the artifact, can be digest or tag |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10
 **x_accept_vulnerabilities** | **str**| A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports &#39;application/vnd.scanner.adapter.vuln.report.harbor+json; version&#x3D;1.0&#39; and &#39;application/vnd.security.vulnerability.report; version&#x3D;1.1&#39; | [optional] if omitted the server will use the default value of "application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0"
 **with_tag** | **bool**| Specify whether the tags are inclued inside the returning artifacts | [optional] if omitted the server will use the default value of True
 **with_label** | **bool**| Specify whether the labels are inclued inside the returning artifacts | [optional] if omitted the server will use the default value of False
 **with_scan_overview** | **bool**| Specify whether the scan overview is inclued inside the returning artifacts | [optional] if omitted the server will use the default value of False
 **with_signature** | **bool**| Specify whether the signature is inclued inside the returning artifacts | [optional] if omitted the server will use the default value of False
 **with_immutable_status** | **bool**| Specify whether the immutable status is inclued inside the tags of the returning artifacts. Only works when setting \&quot;with_tag&#x3D;true\&quot; | [optional] if omitted the server will use the default value of False

### Return type

[**Artifact**](Artifact.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vulnerabilities_addition**
> str get_vulnerabilities_addition(project_name, repository_name, reference)

Get the vulnerabilities addition of the specific artifact

Get the vulnerabilities addition of the artifact specified by the reference under the project and repository.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import artifact_api
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
    api_instance = artifact_api.ArtifactApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    reference = "reference_example" # str | The reference of the artifact, can be digest or tag
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_accept_vulnerabilities = "application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0" # str | A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports 'application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0' and 'application/vnd.security.vulnerability.report; version=1.1' (optional) if omitted the server will use the default value of "application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0"

    # example passing only required values which don't have defaults set
    try:
        # Get the vulnerabilities addition of the specific artifact
        api_response = api_instance.get_vulnerabilities_addition(project_name, repository_name, reference)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->get_vulnerabilities_addition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the vulnerabilities addition of the specific artifact
        api_response = api_instance.get_vulnerabilities_addition(project_name, repository_name, reference, x_request_id=x_request_id, x_accept_vulnerabilities=x_accept_vulnerabilities)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->get_vulnerabilities_addition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **reference** | **str**| The reference of the artifact, can be digest or tag |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_accept_vulnerabilities** | **str**| A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports &#39;application/vnd.scanner.adapter.vuln.report.harbor+json; version&#x3D;1.0&#39; and &#39;application/vnd.security.vulnerability.report; version&#x3D;1.1&#39; | [optional] if omitted the server will use the default value of "application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0"

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Type - The content type of the addition <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_artifacts**
> [Artifact] list_artifacts(project_name, repository_name)

List artifacts

List artifacts under the specific project and repository. Except the basic properties, the other supported queries in \"q\" includes \"tags=*\" to list only tagged artifacts, \"tags=nil\" to list only untagged artifacts, \"tags=~v\" to list artifacts whose tag fuzzy matches \"v\", \"tags=v\" to list artifact whose tag exactly matches \"v\", \"labels=(id1, id2)\" to list artifacts that both labels with id1 and id2 are added to

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import artifact_api
from harbor_client.model.artifact import Artifact
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
    api_instance = artifact_api.ArtifactApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    q = "q_example" # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10
    x_accept_vulnerabilities = "application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0" # str | A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports 'application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0' and 'application/vnd.security.vulnerability.report; version=1.1' (optional) if omitted the server will use the default value of "application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0"
    with_tag = True # bool | Specify whether the tags are included inside the returning artifacts (optional) if omitted the server will use the default value of True
    with_label = False # bool | Specify whether the labels are included inside the returning artifacts (optional) if omitted the server will use the default value of False
    with_scan_overview = False # bool | Specify whether the scan overview is included inside the returning artifacts (optional) if omitted the server will use the default value of False
    with_signature = False # bool | Specify whether the signature is included inside the tags of the returning artifacts. Only works when setting \"with_tag=true\" (optional) if omitted the server will use the default value of False
    with_immutable_status = False # bool | Specify whether the immutable status is included inside the tags of the returning artifacts. Only works when setting \"with_tag=true\" (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # List artifacts
        api_response = api_instance.list_artifacts(project_name, repository_name)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->list_artifacts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List artifacts
        api_response = api_instance.list_artifacts(project_name, repository_name, x_request_id=x_request_id, q=q, page=page, page_size=page_size, x_accept_vulnerabilities=x_accept_vulnerabilities, with_tag=with_tag, with_label=with_label, with_scan_overview=with_scan_overview, with_signature=with_signature, with_immutable_status=with_immutable_status)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->list_artifacts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional]
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10
 **x_accept_vulnerabilities** | **str**| A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports &#39;application/vnd.scanner.adapter.vuln.report.harbor+json; version&#x3D;1.0&#39; and &#39;application/vnd.security.vulnerability.report; version&#x3D;1.1&#39; | [optional] if omitted the server will use the default value of "application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0"
 **with_tag** | **bool**| Specify whether the tags are included inside the returning artifacts | [optional] if omitted the server will use the default value of True
 **with_label** | **bool**| Specify whether the labels are included inside the returning artifacts | [optional] if omitted the server will use the default value of False
 **with_scan_overview** | **bool**| Specify whether the scan overview is included inside the returning artifacts | [optional] if omitted the server will use the default value of False
 **with_signature** | **bool**| Specify whether the signature is included inside the tags of the returning artifacts. Only works when setting \&quot;with_tag&#x3D;true\&quot; | [optional] if omitted the server will use the default value of False
 **with_immutable_status** | **bool**| Specify whether the immutable status is included inside the tags of the returning artifacts. Only works when setting \&quot;with_tag&#x3D;true\&quot; | [optional] if omitted the server will use the default value of False

### Return type

[**[Artifact]**](Artifact.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Total-Count - The total count of tags <br>  * Link - Link refers to the previous page and next page <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> [Tag] list_tags(project_name, repository_name, reference)

List tags

List tags of the specific artifact

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import artifact_api
from harbor_client.model.errors import Errors
from harbor_client.model.tag import Tag
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
    api_instance = artifact_api.ArtifactApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    reference = "reference_example" # str | The reference of the artifact, can be digest or tag
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    q = "q_example" # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10
    with_signature = False # bool | Specify whether the signature is included inside the returning tags (optional) if omitted the server will use the default value of False
    with_immutable_status = False # bool | Specify whether the immutable status is included inside the returning tags (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # List tags
        api_response = api_instance.list_tags(project_name, repository_name, reference)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->list_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List tags
        api_response = api_instance.list_tags(project_name, repository_name, reference, x_request_id=x_request_id, q=q, page=page, page_size=page_size, with_signature=with_signature, with_immutable_status=with_immutable_status)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->list_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **reference** | **str**| The reference of the artifact, can be digest or tag |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional]
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10
 **with_signature** | **bool**| Specify whether the signature is included inside the returning tags | [optional] if omitted the server will use the default value of False
 **with_immutable_status** | **bool**| Specify whether the immutable status is included inside the returning tags | [optional] if omitted the server will use the default value of False

### Return type

[**[Tag]**](Tag.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Total-Count - The total count of tags <br>  * Link - Link refers to the previous page and next page <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_label**
> remove_label(project_name, repository_name, reference, label_id)

Remove label from artifact

Remove the label from the specified artiact.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import artifact_api
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
    api_instance = artifact_api.ArtifactApi(api_client)
    project_name = "project_name_example" # str | The name of the project
    repository_name = "repository_name_example" # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
    reference = "reference_example" # str | The reference of the artifact, can be digest or tag
    label_id = 1 # int | The ID of the label that removed from the artifact.
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove label from artifact
        api_instance.remove_label(project_name, repository_name, reference, label_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->remove_label: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove label from artifact
        api_instance.remove_label(project_name, repository_name, reference, label_id, x_request_id=x_request_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ArtifactApi->remove_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project |
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb |
 **reference** | **str**| The reference of the artifact, can be digest or tag |
 **label_id** | **int**| The ID of the label that removed from the artifact. |
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
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**409** | Conflict |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

