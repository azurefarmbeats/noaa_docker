# datahub_lib.swagger_client.WeatherDataLocationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**weather_data_location_create**](WeatherDataLocationApi.md#weather_data_location_create) | **POST** /WeatherDataLocation | Creates new weather data location with given request body.
[**weather_data_location_delete**](WeatherDataLocationApi.md#weather_data_location_delete) | **DELETE** /WeatherDataLocation/{id} | Deletes the weather data location with given id.
[**weather_data_location_get**](WeatherDataLocationApi.md#weather_data_location_get) | **GET** /WeatherDataLocation/{id} | Returns weather data location for the given id.
[**weather_data_location_get_all**](WeatherDataLocationApi.md#weather_data_location_get_all) | **GET** /WeatherDataLocation | Returns list of weather data locations.
[**weather_data_location_update**](WeatherDataLocationApi.md#weather_data_location_update) | **PUT** /WeatherDataLocation/{id} | Updates the weather data location with given id.


# **weather_data_location_create**
> WeatherDataLocationResponse weather_data_location_create(input=input)

Creates new weather data location with given request body.

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
    api_instance = datahub_lib.swagger_client.WeatherDataLocationApi(api_client)
    input = datahub_lib.swagger_client.WeatherDataLocationRequest() # WeatherDataLocationRequest | Weather data location request object. (optional)

    try:
        # Creates new weather data location with given request body.
        api_response = api_instance.weather_data_location_create(input=input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeatherDataLocationApi->weather_data_location_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**WeatherDataLocationRequest**](WeatherDataLocationRequest.md)| Weather data location request object. | [optional] 

### Return type

[**WeatherDataLocationResponse**](WeatherDataLocationResponse.md)

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

# **weather_data_location_delete**
> weather_data_location_delete(id)

Deletes the weather data location with given id.

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
    api_instance = datahub_lib.swagger_client.WeatherDataLocationApi(api_client)
    id = 'id_example' # str | Id of the weather data location object.

    try:
        # Deletes the weather data location with given id.
        api_instance.weather_data_location_delete(id)
    except ApiException as e:
        print("Exception when calling WeatherDataLocationApi->weather_data_location_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the weather data location object. | 

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

# **weather_data_location_get**
> WeatherDataLocationResponse weather_data_location_get(id)

Returns weather data location for the given id.

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
    api_instance = datahub_lib.swagger_client.WeatherDataLocationApi(api_client)
    id = 'id_example' # str | Id of the weather data location object.

    try:
        # Returns weather data location for the given id.
        api_response = api_instance.weather_data_location_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeatherDataLocationApi->weather_data_location_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the weather data location object. | 

### Return type

[**WeatherDataLocationResponse**](WeatherDataLocationResponse.md)

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

# **weather_data_location_get_all**
> WeatherDataLocationResponseListResponse weather_data_location_get_all(names=names, farm_ids=farm_ids, weather_data_model_ids=weather_data_model_ids, includes=includes, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)

Returns list of weather data locations.

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
    api_instance = datahub_lib.swagger_client.WeatherDataLocationApi(api_client)
    names = ['names_example'] # list[str] | Gets or sets list of names of weather data locations. (optional)
farm_ids = ['farm_ids_example'] # list[str] | Gets or sets list of Farm Ids. (optional)
weather_data_model_ids = ['weather_data_model_ids_example'] # list[str] | Gets or sets list of weather data models id's. (optional)
includes = ['includes_example'] # list[str] | Gets or sets list of properties to be included in WeatherDataLocationResponse. Default value is None. (optional)
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
        # Returns list of weather data locations.
        api_response = api_instance.weather_data_location_get_all(names=names, farm_ids=farm_ids, weather_data_model_ids=weather_data_model_ids, includes=includes, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeatherDataLocationApi->weather_data_location_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| Gets or sets list of names of weather data locations. | [optional] 
 **farm_ids** | [**list[str]**](str.md)| Gets or sets list of Farm Ids. | [optional] 
 **weather_data_model_ids** | [**list[str]**](str.md)| Gets or sets list of weather data models id&#39;s. | [optional] 
 **includes** | [**list[str]**](str.md)| Gets or sets list of properties to be included in WeatherDataLocationResponse. Default value is None. | [optional] 
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

[**WeatherDataLocationResponseListResponse**](WeatherDataLocationResponseListResponse.md)

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

# **weather_data_location_update**
> weather_data_location_update(id, input=input)

Updates the weather data location with given id.

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
    api_instance = datahub_lib.swagger_client.WeatherDataLocationApi(api_client)
    id = 'id_example' # str | Id of the weather data location.
input = datahub_lib.swagger_client.WeatherDataLocationRequest() # WeatherDataLocationRequest | Weather data location request object. (optional)

    try:
        # Updates the weather data location with given id.
        api_instance.weather_data_location_update(id, input=input)
    except ApiException as e:
        print("Exception when calling WeatherDataLocationApi->weather_data_location_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the weather data location. | 
 **input** | [**WeatherDataLocationRequest**](WeatherDataLocationRequest.md)| Weather data location request object. | [optional] 

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

