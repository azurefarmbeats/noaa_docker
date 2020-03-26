# datahub_lib.swagger_client.SceneFileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scene_file_create**](SceneFileApi.md#scene_file_create) | **POST** /SceneFile | Creates new scene file with given request body.
[**scene_file_delete**](SceneFileApi.md#scene_file_delete) | **DELETE** /SceneFile/{id} | Deletes scene file with given id.
[**scene_file_get**](SceneFileApi.md#scene_file_get) | **GET** /SceneFile/{id} | Returns scene file for the given id.
[**scene_file_get_all**](SceneFileApi.md#scene_file_get_all) | **GET** /SceneFile | Returns list of scene file.
[**scene_file_update**](SceneFileApi.md#scene_file_update) | **PUT** /SceneFile/{id} | Updates scene file with given id.


# **scene_file_create**
> CreateSceneFileResponse scene_file_create(input=input)

Creates new scene file with given request body.

User need to use blobPath or uploadSASUrl to save actual content of file.

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
    api_instance = datahub_lib.swagger_client.SceneFileApi(api_client)
    input = datahub_lib.swagger_client.SceneFileRequest() # SceneFileRequest | User's scene file request. (optional)

    try:
        # Creates new scene file with given request body.
        api_response = api_instance.scene_file_create(input=input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SceneFileApi->scene_file_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**SceneFileRequest**](SceneFileRequest.md)| User&#39;s scene file request. | [optional] 

### Return type

[**CreateSceneFileResponse**](CreateSceneFileResponse.md)

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

# **scene_file_delete**
> scene_file_delete(id)

Deletes scene file with given id.

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
    api_instance = datahub_lib.swagger_client.SceneFileApi(api_client)
    id = 'id_example' # str | Id of scene file to be deleted.

    try:
        # Deletes scene file with given id.
        api_instance.scene_file_delete(id)
    except ApiException as e:
        print("Exception when calling SceneFileApi->scene_file_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of scene file to be deleted. | 

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

# **scene_file_get**
> GetSceneFileResponse scene_file_get(id, generate_download_sas_url=generate_download_sas_url)

Returns scene file for the given id.

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
    api_instance = datahub_lib.swagger_client.SceneFileApi(api_client)
    id = 'id_example' # str | scene file id (system-generated).
generate_download_sas_url = True # bool | Specify if SAS URL need to be generated to download content of a file (Default: false). (optional)

    try:
        # Returns scene file for the given id.
        api_response = api_instance.scene_file_get(id, generate_download_sas_url=generate_download_sas_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SceneFileApi->scene_file_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| scene file id (system-generated). | 
 **generate_download_sas_url** | **bool**| Specify if SAS URL need to be generated to download content of a file (Default: false). | [optional] 

### Return type

[**GetSceneFileResponse**](GetSceneFileResponse.md)

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

# **scene_file_get_all**
> GetSceneFileResponseListResponse scene_file_get_all(types=types, content_types=content_types, scene_id=scene_id, generate_download_sas_url=generate_download_sas_url, names=names, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)

Returns list of scene file.

If generateDownloadSASUrl is true and there are more than 10 scene files then it will throw BadRequest with HTTP status code 400.

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
    api_instance = datahub_lib.swagger_client.SceneFileApi(api_client)
    types = ['types_example'] # list[str] | Gets or sets list of types of scene files.  <remark>Refer /ExtendedType APIs with key \"SceneFileType\" for more information.</remark> (optional)
content_types = ['content_types_example'] # list[str] | Gets or sets list of content types of scene files.  <remark>Refer /ExtendedType APIs with key \"SceneFileContentType\" for more information.</remark> (optional)
scene_id = 'scene_id_example' # str | Gets or sets scene id of scene files. (optional)
generate_download_sas_url = False # bool | Gets or sets a value indicating whether download SAS URLs need to be generated. (optional) (default to False)
names = ['names_example'] # list[str] | Gets or sets list of names of scene files which is specified while creating a scene file. (optional)
ids = ['ids_example'] # list[str] | Gets or sets ids of the resource. (optional)
partner_id = 'partner_id_example' # str | Gets or sets id of the partner. (optional)
min_created_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets minimum creation date of resource (inclusive). (optional)
max_created_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets maximum creation date of resource (inclusive). (optional)
min_last_modified_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets minimum last modified date of resource (inclusive). (optional)
max_last_modified_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets maximum last modified date of resource (inclusive). (optional)
property_filter = 'property_filter_example' # str | Gets or sets property filter query.eg. \"x.y.z eq 'somestringvalue' and p.q gt 5 and a eq false\".  Only AND operation is supported.  Supported Operators: EQ,NE,LE,LT,GT,GE,CONTAINS,NCONTAINS. (optional)
max_items = 1500 # int | Gets or sets maximum number of items needed (inclusive).  Maximum items = 5000. (optional) (default to 1500)
x_ms_continuation = 'x_ms_continuation_example' # str | Gets or sets continuation token. (optional)

    try:
        # Returns list of scene file.
        api_response = api_instance.scene_file_get_all(types=types, content_types=content_types, scene_id=scene_id, generate_download_sas_url=generate_download_sas_url, names=names, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SceneFileApi->scene_file_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**list[str]**](str.md)| Gets or sets list of types of scene files.  &lt;remark&gt;Refer /ExtendedType APIs with key \&quot;SceneFileType\&quot; for more information.&lt;/remark&gt; | [optional] 
 **content_types** | [**list[str]**](str.md)| Gets or sets list of content types of scene files.  &lt;remark&gt;Refer /ExtendedType APIs with key \&quot;SceneFileContentType\&quot; for more information.&lt;/remark&gt; | [optional] 
 **scene_id** | **str**| Gets or sets scene id of scene files. | [optional] 
 **generate_download_sas_url** | **bool**| Gets or sets a value indicating whether download SAS URLs need to be generated. | [optional] [default to False]
 **names** | [**list[str]**](str.md)| Gets or sets list of names of scene files which is specified while creating a scene file. | [optional] 
 **ids** | [**list[str]**](str.md)| Gets or sets ids of the resource. | [optional] 
 **partner_id** | **str**| Gets or sets id of the partner. | [optional] 
 **min_created_at** | **datetime**| Gets or sets minimum creation date of resource (inclusive). | [optional] 
 **max_created_at** | **datetime**| Gets or sets maximum creation date of resource (inclusive). | [optional] 
 **min_last_modified_at** | **datetime**| Gets or sets minimum last modified date of resource (inclusive). | [optional] 
 **max_last_modified_at** | **datetime**| Gets or sets maximum last modified date of resource (inclusive). | [optional] 
 **property_filter** | **str**| Gets or sets property filter query.eg. \&quot;x.y.z eq &#39;somestringvalue&#39; and p.q gt 5 and a eq false\&quot;.  Only AND operation is supported.  Supported Operators: EQ,NE,LE,LT,GT,GE,CONTAINS,NCONTAINS. | [optional] 
 **max_items** | **int**| Gets or sets maximum number of items needed (inclusive).  Maximum items &#x3D; 5000. | [optional] [default to 1500]
 **x_ms_continuation** | **str**| Gets or sets continuation token. | [optional] 

### Return type

[**GetSceneFileResponseListResponse**](GetSceneFileResponseListResponse.md)

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

# **scene_file_update**
> scene_file_update(id, input=input)

Updates scene file with given id.

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
    api_instance = datahub_lib.swagger_client.SceneFileApi(api_client)
    id = 'id_example' # str | Id of scene file to be updated.
input = datahub_lib.swagger_client.SceneFileRequest() # SceneFileRequest | New state of scene file. (optional)

    try:
        # Updates scene file with given id.
        api_instance.scene_file_update(id, input=input)
    except ApiException as e:
        print("Exception when calling SceneFileApi->scene_file_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of scene file to be updated. | 
 **input** | [**SceneFileRequest**](SceneFileRequest.md)| New state of scene file. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

