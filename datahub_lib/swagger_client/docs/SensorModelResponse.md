# SensorModelResponse

Sensor Model Response Object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets unique id auto generated for the sensor type. | 
**created_at** | **datetime** | Gets or sets sensor type creation date. | [optional] 
**last_modified_at** | **datetime** | Gets or sets sensor type last updated date. | [optional] 
**type** | **str** | Gets or sets type of the sensor. | 
**manufacturer** | **str** | Gets or sets manufacturer of the sensor. | [optional] 
**product_code** | **str** | Gets or sets sensor product code or Model Name/Number.  eg: RS-CO2-N01. | 
**sensor_measures** | [**list[SensorMeasure]**](SensorMeasure.md) | Gets or sets list of Measurements supported by sensor. | 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


