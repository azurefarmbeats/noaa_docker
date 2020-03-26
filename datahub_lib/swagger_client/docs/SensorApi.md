# datahub_lib.swagger_client.SensorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sensor_create**](SensorApi.md#sensor_create) | **POST** /Sensor | Creates new sensor with given request body.
[**sensor_delete**](SensorApi.md#sensor_delete) | **DELETE** /Sensor/{id} | Deletes the sensor with given id.
[**sensor_get**](SensorApi.md#sensor_get) | **GET** /Sensor/{id} | Returns sensor for the given id.
[**sensor_get_all**](SensorApi.md#sensor_get_all) | **GET** /Sensor | Returns list of sensors.
[**sensor_update**](SensorApi.md#sensor_update) | **PUT** /Sensor/{id} | Updates the sensor with given id.


# **sensor_create**
> SensorResponse sensor_create(input=input)

Creates new sensor with given request body.

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
    api_instance = datahub_lib.swagger_client.SensorApi(api_client)
    input = datahub_lib.swagger_client.SensorRequest() # SensorRequest | Sensor request object. (optional)

    try:
        # Creates new sensor with given request body.
        api_response = api_instance.sensor_create(input=input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SensorApi->sensor_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**SensorRequest**](SensorRequest.md)| Sensor request object. | [optional] 

### Return type

[**SensorResponse**](SensorResponse.md)

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

# **sensor_delete**
> sensor_delete(id)

Deletes the sensor with given id.

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
    api_instance = datahub_lib.swagger_client.SensorApi(api_client)
    id = 'id_example' # str | Id of the sensor object.

    try:
        # Deletes the sensor with given id.
        api_instance.sensor_delete(id)
    except ApiException as e:
        print("Exception when calling SensorApi->sensor_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the sensor object. | 

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

# **sensor_get**
> SensorResponse sensor_get(id)

Returns sensor for the given id.

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
    api_instance = datahub_lib.swagger_client.SensorApi(api_client)
    id = 'id_example' # str | Id of the sensor object.

    try:
        # Returns sensor for the given id.
        api_response = api_instance.sensor_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SensorApi->sensor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the sensor object. | 

### Return type

[**SensorResponse**](SensorResponse.md)

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

# **sensor_get_all**
> SensorResponseListResponse sensor_get_all(names=names, hardware_ids=hardware_ids, sensor_model_ids=sensor_model_ids, device_ids=device_ids, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)

Returns list of sensors.

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
    api_instance = datahub_lib.swagger_client.SensorApi(api_client)
    names = ['names_example'] # list[str] | Gets or sets list of names of sensors. (optional)
hardware_ids = ['hardware_ids_example'] # list[str] | Gets or sets list of hardware id's. (optional)
sensor_model_ids = ['sensor_model_ids_example'] # list[str] | Gets or sets list of sensor models id's. (optional)
device_ids = ['device_ids_example'] # list[str] | Gets or sets list of device id's. (optional)
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
        # Returns list of sensors.
        api_response = api_instance.sensor_get_all(names=names, hardware_ids=hardware_ids, sensor_model_ids=sensor_model_ids, device_ids=device_ids, ids=ids, partner_id=partner_id, min_created_at=min_created_at, max_created_at=max_created_at, min_last_modified_at=min_last_modified_at, max_last_modified_at=max_last_modified_at, property_filter=property_filter, max_items=max_items, x_ms_continuation=x_ms_continuation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SensorApi->sensor_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| Gets or sets list of names of sensors. | [optional] 
 **hardware_ids** | [**list[str]**](str.md)| Gets or sets list of hardware id&#39;s. | [optional] 
 **sensor_model_ids** | [**list[str]**](str.md)| Gets or sets list of sensor models id&#39;s. | [optional] 
 **device_ids** | [**list[str]**](str.md)| Gets or sets list of device id&#39;s. | [optional] 
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

[**SensorResponseListResponse**](SensorResponseListResponse.md)

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

# **sensor_update**
> sensor_update(id, input=input)

Updates the sensor with given id.

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
    api_instance = datahub_lib.swagger_client.SensorApi(api_client)
    id = 'id_example' # str | Id of the sensor.
input = datahub_lib.swagger_client.SensorRequest() # SensorRequest | Sensor request object. (optional)

    try:
        # Updates the sensor with given id.
        api_instance.sensor_update(id, input=input)
    except ApiException as e:
        print("Exception when calling SensorApi->sensor_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the sensor. | 
 **input** | [**SensorRequest**](SensorRequest.md)| Sensor request object. | [optional] 

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

