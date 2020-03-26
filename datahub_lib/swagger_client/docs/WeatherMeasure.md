# WeatherMeasure

Definition for weather measure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets name of the Weather Measure.  For measure from different depths, please specify the depth. Eg.soil_moisture_15cm  This name has to be consistent with the telemetry data. | 
**data_type** | **str** | Gets or sets weather telemetry data type. | 
**measure_enum_definition** | **dict(str, int)** | Gets or sets weather measure enum definition. | [optional] 
**type** | **str** | Gets or sets measurement type of weather telemetry data. (See ExtendedTypes with key \&quot;WeatherMeasureType\&quot; to know all valid values). | 
**unit** | **str** | Gets or sets unit of weather telemetry data. (See ExtendedTypes with key \&quot;WeatherMeasureUnit\&quot; to know all valid values). | 
**aggregation_type** | **str** | Gets or sets aggregation done on weather telemetry data. | [optional] [default to 'None']
**depth** | **float** | Gets or sets depth in centimeters. | [optional] 
**description** | **str** | Gets or sets description of the Weather Measure. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


