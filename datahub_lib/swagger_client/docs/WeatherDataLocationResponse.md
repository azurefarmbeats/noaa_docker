# WeatherDataLocationResponse

Weather data location Response model.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets unique id auto generated for the weatherDataLocation. | 
**created_at** | **datetime** | Gets or sets weatherDataLocation creation date. | [optional] 
**last_modified_at** | **datetime** | Gets or sets weatherDataLocation last updated date. | [optional] 
**weather_data_model_id** | **str** | Gets or sets id of the associated weather data model. | 
**location** | [**Location**](Location.md) |  | 
**farm_id** | **str** | Gets or sets id of the associated farm. | [optional] 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


