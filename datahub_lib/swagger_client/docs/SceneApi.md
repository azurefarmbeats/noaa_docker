# datahub_lib.swagger_client.SceneApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scene_create**](SceneApi.md#scene_create) | **POST** /Scene | Creates new scene with given request body.
[**scene_delete**](SceneApi.md#scene_delete) | **DELETE** /Scene/{id} | Deletes scene with given id.
[**scene_get**](SceneApi.md#scene_get) | **GET** /Scene/{id} | Returns scene for the given id.
[**scene_get_all**](SceneApi.md#scene_get_all) | **GET** /Scene | Returns a list of scenes.
[**scene_update**](SceneApi.md#scene_update) | **PUT** /Scene/{id} | Updates scene with given id.


# **scene_create**
> SceneResponse scene_create(input=input)

Creates new scene with given request body.

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
    api_instance = datahub_lib.swagger_client.SceneApi(api_client)
    input = datahub_lib.swagger_client.SceneRequest() # SceneRequest | User's scene request. (optional)

    try:
        # Creates new scene with given request body.
        api_response = api_instance.scene_create(input=input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SceneApi->scene_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**SceneRequest**](SceneRequest.md)| User&#39;s scene request. | [optional] 

### Return type

[**SceneResponse**](SceneResponse.md)

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

# **scene_delete**
> scene_delete(id)

Deletes scene with given id.

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
    api_instance = datahub_lib.swagger_client.SceneApi(api_client)
    id = 'id_example' # str | Id of scene to be deleted.

    try:
        # Deletes scene with given id.
        api_instance.scene_delete(id)
    except ApiException as e:
        print("Exception when calling SceneApi->scene_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of scene to be deleted. | 

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

# **scene_get**
> SceneResponse scene_get(id)

Returns scene for the given id.

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
    api_instance = datahub_lib.swagger_client.SceneApi(api_client)
    id = 'id_example' # str | scene id (system-generated).

    try:
        # Returns scene for the given id.
        api_response = api_instance.scene_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SceneApi->scene_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| scene id (system-generated). | 

### Return type

[**SceneResponse**](SceneResponse.md)

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

# **scene_get_all**
> SceneResponseListResponse scene_get_all(types=types, sources=sources, farm_id=farm_id, sequence=sequence, min_scene_date=min_scene_date, max_scene_date=max_scene_date, names=names, includes=includes, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)

Returns a list of scenes.

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
    api_instance = datahub_lib.swagger_client.SceneApi(api_client)
    types = ['types_example'] # list[str] | Gets or sets list of types of scenes.  <remark>Refer /ExtendedType APIs with key \"SceneType\" for more information.</remark> (optional)
sources = ['sources_example'] # list[str] | Gets or sets list of sources of scenes.  <remark>Refer /ExtendedType APIs with key \"SceneSource\" for more information.</remark> (optional)
farm_id = 'farm_id_example' # str | Gets or sets farm id of scenes. (optional)
sequence = 56 # int | Gets or sets sequence number of scenes. (optional)
min_scene_date = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets minimum scene nominal date (inclusive). (optional)
max_scene_date = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets maximum scene nominal date (inclusive). (optional)
names = ['names_example'] # list[str] | Gets or sets list of names of scenes which is specified while creating a scene. (optional)
includes = ['includes_example'] # list[str] | Gets or sets list of properties to be included in SceneResponse. (optional)
ids = ['ids_example'] # list[str] | Gets or sets ids of the resource. (optional)
partner_id = 'partner_id_example' # str | Gets or sets id of the partner. (optional)
min_created_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets minimum creation date of resource (inclusive). (optional)
max_created_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets maximum creation date of resource (inclusive). (optional)
min_last_modified_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets minimum last modified date of resource (inclusive). (optional)
max_last_modified_at = '2013-10-20T19:20:30+01:00' # datetime | Gets or sets maximum last modified date of resource (inclusive). (optional)
property_filter = 'property_filter_example' # str | Gets or sets property filter query.eg. \"x.y.z eq 'somestringvalue' and p.q gt 5 and a eq false\".  Only AND operation is supported.  Supported Operators: EQ,NE,LE,LT,GT,GE,CONTAINS,NCONTAINS. (optional)
max_items = 50 # int | Gets or sets maximum number of items needed (inclusive).  Maximum items = 5000. (optional) (default to 50)
x_ms_continuation = 'x_ms_continuation_example' # str | Gets or sets continuation token. (optional)

    try:
        # Returns a list of scenes.
        api_response = api_instance.scene_get_all(types=types, sources=sources, farm_id=farm_id, sequence=sequence, min_scene_date=min_scene_date, max_scene_date=max_scene_date, names=names, includes=includes, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SceneApi->scene_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**list[str]**](str.md)| Gets or sets list of types of scenes.  &lt;remark&gt;Refer /ExtendedType APIs with key \&quot;SceneType\&quot; for more information.&lt;/remark&gt; | [optional] 
 **sources** | [**list[str]**](str.md)| Gets or sets list of sources of scenes.  &lt;remark&gt;Refer /ExtendedType APIs with key \&quot;SceneSource\&quot; for more information.&lt;/remark&gt; | [optional] 
 **farm_id** | **str**| Gets or sets farm id of scenes. | [optional] 
 **sequence** | **int**| Gets or sets sequence number of scenes. | [optional] 
 **min_scene_date** | **datetime**| Gets or sets minimum scene nominal date (inclusive). | [optional] 
 **max_scene_date** | **datetime**| Gets or sets maximum scene nominal date (inclusive). | [optional] 
 **names** | [**list[str]**](str.md)| Gets or sets list of names of scenes which is specified while creating a scene. | [optional] 
 **includes** | [**list[str]**](str.md)| Gets or sets list of properties to be included in SceneResponse. | [optional] 
 **ids** | [**list[str]**](str.md)| Gets or sets ids of the resource. | [optional] 
 **partner_id** | **str**| Gets or sets id of the partner. | [optional] 
 **min_created_at** | **datetime**| Gets or sets minimum creation date of resource (inclusive). | [optional] 
 **max_created_at** | **datetime**| Gets or sets maximum creation date of resource (inclusive). | [optional] 
 **min_last_modified_at** | **datetime**| Gets or sets minimum last modified date of resource (inclusive). | [optional] 
 **max_last_modified_at** | **datetime**| Gets or sets maximum last modified date of resource (inclusive). | [optional] 
 **property_filter** | **str**| Gets or sets property filter query.eg. \&quot;x.y.z eq &#39;somestringvalue&#39; and p.q gt 5 and a eq false\&quot;.  Only AND operation is supported.  Supported Operators: EQ,NE,LE,LT,GT,GE,CONTAINS,NCONTAINS. | [optional] 
 **max_items** | **int**| Gets or sets maximum number of items needed (inclusive).  Maximum items &#x3D; 5000. | [optional] [default to 50]
 **x_ms_continuation** | **str**| Gets or sets continuation token. | [optional] 

### Return type

[**SceneResponseListResponse**](SceneResponseListResponse.md)

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

# **scene_update**
> scene_update(id, input=input)

Updates scene with given id.

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
    api_instance = datahub_lib.swagger_client.SceneApi(api_client)
    id = 'id_example' # str | Id of scene that need to be updated (system-generated).
input = datahub_lib.swagger_client.SceneRequest() # SceneRequest | New state of scene. (optional)

    try:
        # Updates scene with given id.
        api_instance.scene_update(id, input=input)
    except ApiException as e:
        print("Exception when calling SceneApi->scene_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of scene that need to be updated (system-generated). | 
 **input** | [**SceneRequest**](SceneRequest.md)| New state of scene. | [optional] 

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

