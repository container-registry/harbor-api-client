# harbor_client.JobserviceApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_pending_jobs**](JobserviceApi.md#action_pending_jobs) | **PUT** /jobservice/queues/{job_type} | stop and clean, pause, resume pending jobs in the queue
[**get_worker_pools**](JobserviceApi.md#get_worker_pools) | **GET** /jobservice/pools | Get worker pools
[**get_workers**](JobserviceApi.md#get_workers) | **GET** /jobservice/pools/{pool_id}/workers | Get workers
[**list_job_queues**](JobserviceApi.md#list_job_queues) | **GET** /jobservice/queues | list job queues
[**stop_running_job**](JobserviceApi.md#stop_running_job) | **PUT** /jobservice/jobs/{job_id} | Stop running job


# **action_pending_jobs**
> action_pending_jobs(job_type, action_request, x_request_id=x_request_id)

stop and clean, pause, resume pending jobs in the queue

stop and clean, pause, resume pending jobs in the queue

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
api_instance = harbor_client.JobserviceApi(harbor_client.ApiClient(configuration))
job_type = 'job_type_example' # str | The type of the job. 'all' stands for all job types
action_request = harbor_client.ActionRequest() # ActionRequest | 
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # stop and clean, pause, resume pending jobs in the queue
    api_instance.action_pending_jobs(job_type, action_request, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling JobserviceApi->action_pending_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type** | **str**| The type of the job. &#39;all&#39; stands for all job types | 
 **action_request** | [**ActionRequest**](ActionRequest.md)|  | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_worker_pools**
> list[WorkerPool] get_worker_pools(x_request_id=x_request_id)

Get worker pools

Get worker pools

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
api_instance = harbor_client.JobserviceApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get worker pools
    api_response = api_instance.get_worker_pools(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobserviceApi->get_worker_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**list[WorkerPool]**](WorkerPool.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workers**
> list[Worker] get_workers(pool_id, x_request_id=x_request_id)

Get workers

Get workers in current pool

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
api_instance = harbor_client.JobserviceApi(harbor_client.ApiClient(configuration))
pool_id = 'pool_id_example' # str | The name of the pool. 'all' stands for all pools
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get workers
    api_response = api_instance.get_workers(pool_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobserviceApi->get_workers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| The name of the pool. &#39;all&#39; stands for all pools | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**list[Worker]**](Worker.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_job_queues**
> list[JobQueue] list_job_queues(x_request_id=x_request_id)

list job queues

list job queue

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
api_instance = harbor_client.JobserviceApi(harbor_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # list job queues
    api_response = api_instance.list_job_queues(x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobserviceApi->list_job_queues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**list[JobQueue]**](JobQueue.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_running_job**
> stop_running_job(job_id, x_request_id=x_request_id)

Stop running job

Stop running job

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
api_instance = harbor_client.JobserviceApi(harbor_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The id of the job.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Stop running job
    api_instance.stop_running_job(job_id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling JobserviceApi->stop_running_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The id of the job. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

