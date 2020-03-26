# SensorMeasure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets name of the Sensor Measure.  For measure from different depths, please specify the depth. Eg.soil_moisture_15cm  This name has to be consistent with the telemetry data. | 
**data_type** | **str** | Gets or sets sensor telemetry data type. | 
**type** | **str** | Gets or sets measurement type of sensor telemetry data. (See ExtendedTypes with key \&quot;SensorMeasureType\&quot; to know all valid values). | 
**unit** | **str** | Gets or sets unit of sensor telemetry data. (See ExtendedTypes with key \&quot;SensorMeasureUnit\&quot; to know all valid values). | 
**aggregation_type** | **str** | Gets or sets aggregation done on telemetry data. | [optional] [default to 'None']
**depth** | **float** | Gets or sets depth in centimeters. | [optional] 
**description** | **str** | Gets or sets description of the Sensor Measure. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


