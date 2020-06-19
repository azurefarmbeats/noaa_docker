# datahub_lib.swagger_client.TelemetryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**telemetry_get_all**](TelemetryApi.md#telemetry_get_all) | **POST** /Telemetry | Returns list of telemetry messages.


# **telemetry_get_all**
> QueryResultPage telemetry_get_all(remove_duplicate_data=remove_duplicate_data, query_filter=query_filter)

Returns list of telemetry messages.

based on specified filters. Requires ReadAll privileges.

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
    api_instance = datahub_lib.swagger_client.TelemetryApi(api_client)
    remove_duplicate_data = True # bool | Flag to remove duplicate Telemetry data. Applicable only for weather data. (optional)
query_filter = datahub_lib.swagger_client.TelemetryQueryFilter() # TelemetryQueryFilter | Telemetry query filter object. (optional)

    try:
        # Returns list of telemetry messages.
        api_response = api_instance.telemetry_get_all(remove_duplicate_data=remove_duplicate_data, query_filter=query_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TelemetryApi->telemetry_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_duplicate_data** | **bool**| Flag to remove duplicate Telemetry data. Applicable only for weather data. | [optional] 
 **query_filter** | [**TelemetryQueryFilter**](TelemetryQueryFilter.md)| Telemetry query filter object. | [optional] 

### Return type

[**QueryResultPage**](QueryResultPage.md)

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

