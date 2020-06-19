# datahub_lib.swagger_client.AlertApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alert_get**](AlertApi.md#alert_get) | **GET** /Alert/{id} | Returns alert for the given id.
[**alert_get_all**](AlertApi.md#alert_get_all) | **GET** /Alert | Returns list of alerts.
[**alert_update**](AlertApi.md#alert_update) | **PUT** /Alert/{id} | Updates the alert with given id.


# **alert_get**
> AlertResponse alert_get(id)

Returns alert for the given id.

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
    api_instance = datahub_lib.swagger_client.AlertApi(api_client)
    id = 'id_example' # str | Id of the alert object.

    try:
        # Returns alert for the given id.
        api_response = api_instance.alert_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->alert_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the alert object. | 

### Return type

[**AlertResponse**](AlertResponse.md)

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

# **alert_get_all**
> AlertResponseListResponse alert_get_all(rule_ids=rule_ids, device_ids=device_ids, severity_levels=severity_levels, status=status, includes=includes, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)

Returns list of alerts.

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
    api_instance = datahub_lib.swagger_client.AlertApi(api_client)
    rule_ids = ['rule_ids_example'] # list[str] | Gets or sets list of rule ids for which alerts are generated. (optional)
device_ids = ['device_ids_example'] # list[str] | Gets or sets list of device ids for which alerts are generated. (optional)
severity_levels = ['severity_levels_example'] # list[str] | Gets or sets list of rule severity levels. (optional)
status = 'status_example' # str | Gets or sets alert status. (optional)
includes = ['includes_example'] # list[str] | Gets or sets list of properties to be included in AlertResponse. Default value is None. (optional)
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
        # Returns list of alerts.
        api_response = api_instance.alert_get_all(rule_ids=rule_ids, device_ids=device_ids, severity_levels=severity_levels, status=status, includes=includes, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->alert_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_ids** | [**list[str]**](str.md)| Gets or sets list of rule ids for which alerts are generated. | [optional] 
 **device_ids** | [**list[str]**](str.md)| Gets or sets list of device ids for which alerts are generated. | [optional] 
 **severity_levels** | [**list[str]**](str.md)| Gets or sets list of rule severity levels. | [optional] 
 **status** | **str**| Gets or sets alert status. | [optional] 
 **includes** | [**list[str]**](str.md)| Gets or sets list of properties to be included in AlertResponse. Default value is None. | [optional] 
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

[**AlertResponseListResponse**](AlertResponseListResponse.md)

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

# **alert_update**
> alert_update(id, input=input)

Updates the alert with given id.

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
    api_instance = datahub_lib.swagger_client.AlertApi(api_client)
    id = 'id_example' # str | Id of the alert.
input = datahub_lib.swagger_client.AlertRequest() # AlertRequest | Alert request object. (optional)

    try:
        # Updates the alert with given id.
        api_instance.alert_update(id, input=input)
    except ApiException as e:
        print("Exception when calling AlertApi->alert_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the alert. | 
 **input** | [**AlertRequest**](AlertRequest.md)| Alert request object. | [optional] 

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

