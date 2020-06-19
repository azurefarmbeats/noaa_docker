# datahub_lib.swagger_client.JobApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_create**](JobApi.md#job_create) | **POST** /Job | Creates new job with given request body.
[**job_delete**](JobApi.md#job_delete) | **DELETE** /Job/{id} | Deletes job with given id.
[**job_get**](JobApi.md#job_get) | **GET** /Job/{id} | Returns job for the given id.
[**job_get_all**](JobApi.md#job_get_all) | **GET** /Job | Returns a list of jobs.
[**job_stop_job**](JobApi.md#job_stop_job) | **PATCH** /Job/{id}/stop | Request to stop a job with given id.


# **job_create**
> JobResponse job_create(input=input)

Creates new job with given request body.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import datahub_lib.swagger_client
from datahub_lib.swagger_client.rest import ApiException
from pprint import pprint
configuration = datahub_lib.swagger_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with datahub_lib.swagger_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = datahub_lib.swagger_client.JobApi(api_client)
    input = datahub_lib.swagger_client.JobRequest() # JobRequest | User's job request. (optional)

    try:
        # Creates new job with given request body.
        api_response = api_instance.job_create(input=input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->job_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**JobRequest**](JobRequest.md)| User&#39;s job request. | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_delete**
> job_delete(id)

Deletes job with given id.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import datahub_lib.swagger_client
from datahub_lib.swagger_client.rest import ApiException
from pprint import pprint
configuration = datahub_lib.swagger_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with datahub_lib.swagger_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = datahub_lib.swagger_client.JobApi(api_client)
    id = 'id_example' # str | Id of job to deleted.

    try:
        # Deletes job with given id.
        api_instance.job_delete(id)
    except ApiException as e:
        print("Exception when calling JobApi->job_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of job to deleted. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_get**
> JobResponse job_get(id, debug=debug)

Returns job for the given id.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import datahub_lib.swagger_client
from datahub_lib.swagger_client.rest import ApiException
from pprint import pprint
configuration = datahub_lib.swagger_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with datahub_lib.swagger_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = datahub_lib.swagger_client.JobApi(api_client)
    id = 'id_example' # str | Job id (system-generated).
debug = True # bool | Flag indicating if debug info is required or not (Default: false). (optional)

    try:
        # Returns job for the given id.
        api_response = api_instance.job_get(id, debug=debug)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->job_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job id (system-generated). | 
 **debug** | **bool**| Flag indicating if debug info is required or not (Default: false). | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_get_all**
> JobResponseListResponse job_get_all(type_ids=type_ids, states=states, names=names, parent_job_ids=parent_job_ids, includes=includes, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)

Returns a list of jobs.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import datahub_lib.swagger_client
from datahub_lib.swagger_client.rest import ApiException
from pprint import pprint
configuration = datahub_lib.swagger_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with datahub_lib.swagger_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = datahub_lib.swagger_client.JobApi(api_client)
    type_ids = ['type_ids_example'] # list[str] | Gets or sets list of job type ids of jobs. (optional)
states = ['states_example'] # list[str] | Gets or sets list of job states of jobs. (optional)
names = ['names_example'] # list[str] | Gets or sets list of names of jobs which is specified while creating a job. (optional)
parent_job_ids = ['parent_job_ids_example'] # list[str] | Gets or sets list of parent job ids. (optional)
includes = ['includes_example'] # list[str] | Gets or sets list of properties to be included in JobResponse. Default value is None. (optional)
ids = ['ids_example'] # list[str] | Gets or sets ids of the resource. (optional)
partner_id = 'partner_id_example' # str | Gets or sets id of the partner. (optional)
min_created_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets minimum creation date of resource (inclusive). (optional)
max_created_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets maximum creation date of resource (inclusive). (optional)
min_last_modified_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets minimum last modified date of resource (inclusive). (optional)
max_last_modified_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets maximum last modified date of resource (inclusive). (optional)
property_filter = 'property_filter_example' # str | Gets or sets property filter query.eg. \"x.y.z eq 'somestringvalue' and p.q gt 5 and a eq false\".  Only AND operation is supported.  Supported Operators: EQ,NE,LE,LT,GT,GE,CONTAINS,NCONTAINS. (optional)
max_items = 50 # int | Gets or sets maximum number of items needed (inclusive).  Maximum items = 1000. (optional) (default to 50)
x_ms_continuation = 'x_ms_continuation_example' # str | Gets or sets continuation token. (optional)

    try:
        # Returns a list of jobs.
        api_response = api_instance.job_get_all(type_ids=type_ids, states=states, names=names, parent_job_ids=parent_job_ids, includes=includes, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->job_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_ids** | [**list[str]**](str.md)| Gets or sets list of job type ids of jobs. | [optional] 
 **states** | [**list[str]**](str.md)| Gets or sets list of job states of jobs. | [optional] 
 **names** | [**list[str]**](str.md)| Gets or sets list of names of jobs which is specified while creating a job. | [optional] 
 **parent_job_ids** | [**list[str]**](str.md)| Gets or sets list of parent job ids. | [optional] 
 **includes** | [**list[str]**](str.md)| Gets or sets list of properties to be included in JobResponse. Default value is None. | [optional] 
 **ids** | [**list[str]**](str.md)| Gets or sets ids of the resource. | [optional] 
 **partner_id** | **str**| Gets or sets id of the partner. | [optional] 
 **min_created_at** | **datetime**| Gets or sets minimum creation date of resource (inclusive). | [optional] 
 **max_created_at** | **datetime**| Gets or sets maximum creation date of resource (inclusive). | [optional] 
 **min_last_modified_at** | **datetime**| Gets or sets minimum last modified date of resource (inclusive). | [optional] 
 **max_last_modified_at** | **datetime**| Gets or sets maximum last modified date of resource (inclusive). | [optional] 
 **property_filter** | **str**| Gets or sets property filter query.eg. \&quot;x.y.z eq &#39;somestringvalue&#39; and p.q gt 5 and a eq false\&quot;.  Only AND operation is supported.  Supported Operators: EQ,NE,LE,LT,GT,GE,CONTAINS,NCONTAINS. | [optional] 
 **max_items** | **int**| Gets or sets maximum number of items needed (inclusive).  Maximum items &#x3D; 1000. | [optional] [default to 50]
 **x_ms_continuation** | **str**| Gets or sets continuation token. | [optional] 

### Return type

[**JobResponseListResponse**](JobResponseListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_stop_job**
> JobResponse job_stop_job(id)

Request to stop a job with given id.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import datahub_lib.swagger_client
from datahub_lib.swagger_client.rest import ApiException
from pprint import pprint
configuration = datahub_lib.swagger_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with datahub_lib.swagger_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = datahub_lib.swagger_client.JobApi(api_client)
    id = 'id_example' # str | Id of job that need to be stopped.

    try:
        # Request to stop a job with given id.
        api_response = api_instance.job_stop_job(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->job_stop_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of job that need to be stopped. | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

