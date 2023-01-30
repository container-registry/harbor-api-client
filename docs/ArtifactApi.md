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
[**list_accessories**](ArtifactApi.md#list_accessories) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/accessories | List accessories
[**list_artifacts**](ArtifactApi.md#list_artifacts) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts | List artifacts
[**list_tags**](ArtifactApi.md#list_tags) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags | List tags
[**remove_label**](ArtifactApi.md#remove_label) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/labels/{label_id} | Remove label from artifact


# **add_label**
> add_label(project_name, repository_name, reference, label, x_request_id=x_request_id)

Add label to artifact

Add label to the specified artiact.

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
label = harbor_client.Label() # Label | The label that added to the artifact. Only the ID property is needed.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Add label to artifact
    api_instance.add_label(project_name, repository_name, reference, label, x_request_id=x_request_id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_artifact**
> copy_artifact(project_name, repository_name, _from, x_request_id=x_request_id)

Copy artifact

Copy the artifact specified in the \"from\" parameter to the repository.

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
_from = '_from_example' # str | The artifact from which the new artifact is copied from, the format should be \"project/repository:tag\" or \"project/repository@digest\".
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Copy artifact
    api_instance.copy_artifact(project_name, repository_name, _from, x_request_id=x_request_id)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag**
> create_tag(project_name, repository_name, reference, tag, x_request_id=x_request_id)

Create tag

Create a tag for the specified artifact

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
tag = harbor_client.Tag() # Tag | The JSON object of tag.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create tag
    api_instance.create_tag(project_name, repository_name, reference, tag, x_request_id=x_request_id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact**
> delete_artifact(project_name, repository_name, reference, x_request_id=x_request_id)

Delete the specific artifact

Delete the artifact specified by the reference under the project and repository. The reference can be digest or tag

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete the specific artifact
    api_instance.delete_artifact(project_name, repository_name, reference, x_request_id=x_request_id)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(project_name, repository_name, reference, tag_name, x_request_id=x_request_id)

Delete tag

Delete the tag of the specified artifact

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
tag_name = 'tag_name_example' # str | The name of the tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete tag
    api_instance.delete_tag(project_name, repository_name, reference, tag_name, x_request_id=x_request_id)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addition**
> str get_addition(project_name, repository_name, reference, addition, x_request_id=x_request_id)

Get the addition of the specific artifact

Get the addition of the artifact specified by the reference under the project and repository.

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
addition = 'addition_example' # str | The type of addition.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the addition of the specific artifact
    api_response = api_instance.get_addition(project_name, repository_name, reference, addition, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact**
> Artifact get_artifact(project_name, repository_name, reference, x_request_id=x_request_id, page=page, page_size=page_size, x_accept_vulnerabilities=x_accept_vulnerabilities, with_tag=with_tag, with_label=with_label, with_scan_overview=with_scan_overview, with_accessory=with_accessory, with_signature=with_signature, with_immutable_status=with_immutable_status)

Get the specific artifact

Get the artifact specified by the reference under the project and repository. The reference can be digest or tag.

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
x_accept_vulnerabilities = 'application/vnd.security.vulnerability.report; version=1.1, application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0' # str | A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports 'application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0' and 'application/vnd.security.vulnerability.report; version=1.1' (optional) (default to application/vnd.security.vulnerability.report; version=1.1, application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0)
with_tag = true # bool | Specify whether the tags are inclued inside the returning artifacts (optional) (default to true)
with_label = false # bool | Specify whether the labels are inclued inside the returning artifacts (optional) (default to false)
with_scan_overview = false # bool | Specify whether the scan overview is inclued inside the returning artifacts (optional) (default to false)
with_accessory = false # bool | Specify whether the accessories are included of the returning artifacts. (optional) (default to false)
with_signature = false # bool | Specify whether the signature is inclued inside the returning artifacts (optional) (default to false)
with_immutable_status = false # bool | Specify whether the immutable status is inclued inside the tags of the returning artifacts. (optional) (default to false)

try:
    # Get the specific artifact
    api_response = api_instance.get_artifact(project_name, repository_name, reference, x_request_id=x_request_id, page=page, page_size=page_size, x_accept_vulnerabilities=x_accept_vulnerabilities, with_tag=with_tag, with_label=with_label, with_scan_overview=with_scan_overview, with_accessory=with_accessory, with_signature=with_signature, with_immutable_status=with_immutable_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactApi->get_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb | 
 **reference** | **str**| The reference of the artifact, can be digest or tag | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **x_accept_vulnerabilities** | **str**| A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports &#39;application/vnd.scanner.adapter.vuln.report.harbor+json; version&#x3D;1.0&#39; and &#39;application/vnd.security.vulnerability.report; version&#x3D;1.1&#39; | [optional] [default to application/vnd.security.vulnerability.report; version&#x3D;1.1, application/vnd.scanner.adapter.vuln.report.harbor+json; version&#x3D;1.0]
 **with_tag** | **bool**| Specify whether the tags are inclued inside the returning artifacts | [optional] [default to true]
 **with_label** | **bool**| Specify whether the labels are inclued inside the returning artifacts | [optional] [default to false]
 **with_scan_overview** | **bool**| Specify whether the scan overview is inclued inside the returning artifacts | [optional] [default to false]
 **with_accessory** | **bool**| Specify whether the accessories are included of the returning artifacts. | [optional] [default to false]
 **with_signature** | **bool**| Specify whether the signature is inclued inside the returning artifacts | [optional] [default to false]
 **with_immutable_status** | **bool**| Specify whether the immutable status is inclued inside the tags of the returning artifacts. | [optional] [default to false]

### Return type

[**Artifact**](Artifact.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vulnerabilities_addition**
> str get_vulnerabilities_addition(project_name, repository_name, reference, x_request_id=x_request_id, x_accept_vulnerabilities=x_accept_vulnerabilities)

Get the vulnerabilities addition of the specific artifact

Get the vulnerabilities addition of the artifact specified by the reference under the project and repository.

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
x_accept_vulnerabilities = 'application/vnd.security.vulnerability.report; version=1.1, application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0' # str | A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports 'application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0' and 'application/vnd.security.vulnerability.report; version=1.1' (optional) (default to application/vnd.security.vulnerability.report; version=1.1, application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0)

try:
    # Get the vulnerabilities addition of the specific artifact
    api_response = api_instance.get_vulnerabilities_addition(project_name, repository_name, reference, x_request_id=x_request_id, x_accept_vulnerabilities=x_accept_vulnerabilities)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactApi->get_vulnerabilities_addition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb | 
 **reference** | **str**| The reference of the artifact, can be digest or tag | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **x_accept_vulnerabilities** | **str**| A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports &#39;application/vnd.scanner.adapter.vuln.report.harbor+json; version&#x3D;1.0&#39; and &#39;application/vnd.security.vulnerability.report; version&#x3D;1.1&#39; | [optional] [default to application/vnd.security.vulnerability.report; version&#x3D;1.1, application/vnd.scanner.adapter.vuln.report.harbor+json; version&#x3D;1.0]

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accessories**
> list[Accessory] list_accessories(project_name, repository_name, reference, x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)

List accessories

List accessories of the specific artifact

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    # List accessories
    api_response = api_instance.list_accessories(project_name, repository_name, reference, x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactApi->list_accessories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb | 
 **reference** | **str**| The reference of the artifact, can be digest or tag | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]

### Return type

[**list[Accessory]**](Accessory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_artifacts**
> list[Artifact] list_artifacts(project_name, repository_name, x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size, x_accept_vulnerabilities=x_accept_vulnerabilities, with_tag=with_tag, with_label=with_label, with_scan_overview=with_scan_overview, with_signature=with_signature, with_immutable_status=with_immutable_status, with_accessory=with_accessory)

List artifacts

List artifacts under the specific project and repository. Except the basic properties, the other supported queries in \"q\" includes \"tags=*\" to list only tagged artifacts, \"tags=nil\" to list only untagged artifacts, \"tags=~v\" to list artifacts whose tag fuzzy matches \"v\", \"tags=v\" to list artifact whose tag exactly matches \"v\", \"labels=(id1, id2)\" to list artifacts that both labels with id1 and id2 are added to

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
x_accept_vulnerabilities = 'application/vnd.security.vulnerability.report; version=1.1, application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0' # str | A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports 'application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0' and 'application/vnd.security.vulnerability.report; version=1.1' (optional) (default to application/vnd.security.vulnerability.report; version=1.1, application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0)
with_tag = true # bool | Specify whether the tags are included inside the returning artifacts (optional) (default to true)
with_label = false # bool | Specify whether the labels are included inside the returning artifacts (optional) (default to false)
with_scan_overview = false # bool | Specify whether the scan overview is included inside the returning artifacts (optional) (default to false)
with_signature = false # bool | Specify whether the signature is included inside the tags of the returning artifacts. Only works when setting \"with_tag=true\" (optional) (default to false)
with_immutable_status = false # bool | Specify whether the immutable status is included inside the tags of the returning artifacts. Only works when setting \"with_immutable_status=true\" (optional) (default to false)
with_accessory = false # bool | Specify whether the accessories are included of the returning artifacts. Only works when setting \"with_accessory=true\" (optional) (default to false)

try:
    # List artifacts
    api_response = api_instance.list_artifacts(project_name, repository_name, x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size, x_accept_vulnerabilities=x_accept_vulnerabilities, with_tag=with_tag, with_label=with_label, with_scan_overview=with_scan_overview, with_signature=with_signature, with_immutable_status=with_immutable_status, with_accessory=with_accessory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactApi->list_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **repository_name** | **str**| The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -&gt; a%252Fb | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **x_accept_vulnerabilities** | **str**| A comma-separated lists of MIME types for the scan report or scan summary. The first mime type will be used when the report found for it. Currently the mime type supports &#39;application/vnd.scanner.adapter.vuln.report.harbor+json; version&#x3D;1.0&#39; and &#39;application/vnd.security.vulnerability.report; version&#x3D;1.1&#39; | [optional] [default to application/vnd.security.vulnerability.report; version&#x3D;1.1, application/vnd.scanner.adapter.vuln.report.harbor+json; version&#x3D;1.0]
 **with_tag** | **bool**| Specify whether the tags are included inside the returning artifacts | [optional] [default to true]
 **with_label** | **bool**| Specify whether the labels are included inside the returning artifacts | [optional] [default to false]
 **with_scan_overview** | **bool**| Specify whether the scan overview is included inside the returning artifacts | [optional] [default to false]
 **with_signature** | **bool**| Specify whether the signature is included inside the tags of the returning artifacts. Only works when setting \&quot;with_tag&#x3D;true\&quot; | [optional] [default to false]
 **with_immutable_status** | **bool**| Specify whether the immutable status is included inside the tags of the returning artifacts. Only works when setting \&quot;with_immutable_status&#x3D;true\&quot; | [optional] [default to false]
 **with_accessory** | **bool**| Specify whether the accessories are included of the returning artifacts. Only works when setting \&quot;with_accessory&#x3D;true\&quot; | [optional] [default to false]

### Return type

[**list[Artifact]**](Artifact.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> list[Tag] list_tags(project_name, repository_name, reference, x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size, with_signature=with_signature, with_immutable_status=with_immutable_status)

List tags

List tags of the specific artifact

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
sort = 'sort_example' # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
with_signature = false # bool | Specify whether the signature is included inside the returning tags (optional) (default to false)
with_immutable_status = false # bool | Specify whether the immutable status is included inside the returning tags (optional) (default to false)

try:
    # List tags
    api_response = api_instance.list_tags(project_name, repository_name, reference, x_request_id=x_request_id, q=q, sort=sort, page=page, page_size=page_size, with_signature=with_signature, with_immutable_status=with_immutable_status)
    pprint(api_response)
except ApiException as e:
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
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **with_signature** | **bool**| Specify whether the signature is included inside the returning tags | [optional] [default to false]
 **with_immutable_status** | **bool**| Specify whether the immutable status is included inside the returning tags | [optional] [default to false]

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_label**
> remove_label(project_name, repository_name, reference, label_id, x_request_id=x_request_id)

Remove label from artifact

Remove the label from the specified artiact.

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
api_instance = harbor_client.ArtifactApi(harbor_client.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
label_id = 789 # int | The ID of the label that removed from the artifact.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Remove label from artifact
    api_instance.remove_label(project_name, repository_name, reference, label_id, x_request_id=x_request_id)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

