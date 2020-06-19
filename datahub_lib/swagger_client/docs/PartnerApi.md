# datahub_lib.swagger_client.PartnerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**partner_create**](PartnerApi.md#partner_create) | **POST** /Partner | Creates new partner with given request body.
[**partner_delete**](PartnerApi.md#partner_delete) | **DELETE** /Partner/{id} | Deletes the partner with given id.
[**partner_get**](PartnerApi.md#partner_get) | **GET** /Partner/{id} | Returns partner for the given id.
[**partner_get_all**](PartnerApi.md#partner_get_all) | **GET** /Partner | Returns list of partners.
[**partner_renew**](PartnerApi.md#partner_renew) | **PATCH** /Partner/{id}/renew | Renew connection strings of event hub.
[**partner_update**](PartnerApi.md#partner_update) | **PUT** /Partner/{id} | Updates the partner with given id.


# **partner_create**
> PartnerResponse partner_create(input=input)

Creates new partner with given request body.

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
    api_instance = datahub_lib.swagger_client.PartnerApi(api_client)
    input = datahub_lib.swagger_client.PartnerRequest() # PartnerRequest | Partner request object. (optional)

    try:
        # Creates new partner with given request body.
        api_response = api_instance.partner_create(input=input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartnerApi->partner_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**PartnerRequest**](PartnerRequest.md)| Partner request object. | [optional] 

### Return type

[**PartnerResponse**](PartnerResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**202** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_delete**
> partner_delete(id, force=force)

Deletes the partner with given id.

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
    api_instance = datahub_lib.swagger_client.PartnerApi(api_client)
    id = 'id_example' # str | Id of the partner object.
force = False # bool | Gets or sets a value indicating whether force delete is allowed. (optional) (default to False)

    try:
        # Deletes the partner with given id.
        api_instance.partner_delete(id, force=force)
    except ApiException as e:
        print("Exception when calling PartnerApi->partner_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the partner object. | 
 **force** | **bool**| Gets or sets a value indicating whether force delete is allowed. | [optional] [default to False]

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
**202** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_get**
> PartnerResponse partner_get(id, debug=debug)

Returns partner for the given id.

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
    api_instance = datahub_lib.swagger_client.PartnerApi(api_client)
    id = 'id_example' # str | Id of the partner object.
debug = True # bool | Flag indicating if debug info is required or not (Default: false). (optional)

    try:
        # Returns partner for the given id.
        api_response = api_instance.partner_get(id, debug=debug)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartnerApi->partner_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the partner object. | 
 **debug** | **bool**| Flag indicating if debug info is required or not (Default: false). | [optional] 

### Return type

[**PartnerResponse**](PartnerResponse.md)

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

# **partner_get_all**
> PartnerLimitedResponseListResponse partner_get_all(names=names, object_ids=object_ids, partner_types=partner_types, tenant_ids=tenant_ids, includes=includes, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)

Returns list of partners.

based on specified filters and date range. Requires ReadAll privileges.

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
    api_instance = datahub_lib.swagger_client.PartnerApi(api_client)
    names = ['names_example'] # list[str] | Gets or sets list of names of partner. (optional)
object_ids = ['object_ids_example'] # list[str] | Gets or sets list of Object id's. (optional)
partner_types = ['partner_types_example'] # list[str] | Gets or sets list of Partner Types. (optional)
tenant_ids = ['tenant_ids_example'] # list[str] | Gets or sets list of Tenant id's. (optional)
includes = ['includes_example'] # list[str] | Gets or sets list of properties to be included in PartnerResponse. Default value is None. (optional)
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
        # Returns list of partners.
        api_response = api_instance.partner_get_all(names=names, object_ids=object_ids, partner_types=partner_types, tenant_ids=tenant_ids, includes=includes, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartnerApi->partner_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| Gets or sets list of names of partner. | [optional] 
 **object_ids** | [**list[str]**](str.md)| Gets or sets list of Object id&#39;s. | [optional] 
 **partner_types** | [**list[str]**](str.md)| Gets or sets list of Partner Types. | [optional] 
 **tenant_ids** | [**list[str]**](str.md)| Gets or sets list of Tenant id&#39;s. | [optional] 
 **includes** | [**list[str]**](str.md)| Gets or sets list of properties to be included in PartnerResponse. Default value is None. | [optional] 
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

[**PartnerLimitedResponseListResponse**](PartnerLimitedResponseListResponse.md)

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

# **partner_renew**
> PartnerResponse partner_renew(id)

Renew connection strings of event hub.

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
    api_instance = datahub_lib.swagger_client.PartnerApi(api_client)
    id = 'id_example' # str | Id of partner (system-generated).

    try:
        # Renew connection strings of event hub.
        api_response = api_instance.partner_renew(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PartnerApi->partner_renew: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of partner (system-generated). | 

### Return type

[**PartnerResponse**](PartnerResponse.md)

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

# **partner_update**
> partner_update(id, input=input)

Updates the partner with given id.

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
    api_instance = datahub_lib.swagger_client.PartnerApi(api_client)
    id = 'id_example' # str | Id of the partner.
input = datahub_lib.swagger_client.PartnerRequest() # PartnerRequest | Partner request object. (optional)

    try:
        # Updates the partner with given id.
        api_instance.partner_update(id, input=input)
    except ApiException as e:
        print("Exception when calling PartnerApi->partner_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the partner. | 
 **input** | [**PartnerRequest**](PartnerRequest.md)| Partner request object. | [optional] 

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
**202** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

