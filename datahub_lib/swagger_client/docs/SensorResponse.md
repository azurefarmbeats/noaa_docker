# SensorResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets unique id auto generated for the sensor. | 
**created_at** | **datetime** | Gets or sets sensor creation date. | [optional] 
**last_modified_at** | **datetime** | Gets or sets sensor last updated date. | [optional] 
**hardware_id** | **str** | Gets or sets id of the sensor given by manufacturer. | [optional] 
**sensor_model_id** | **str** | Gets or sets id of the associated sensor Model. | 
**location** | [**Location**](Location.md) |  | [optional] 
**depth** | **float** | Gets or sets depth in centimeters. | [optional] 
**port** | [**DevicePort**](DevicePort.md) |  | [optional] 
**device_id** | **str** | Gets or sets id of the associated device. | [optional] 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


