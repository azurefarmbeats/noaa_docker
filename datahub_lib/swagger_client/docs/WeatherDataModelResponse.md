# WeatherDataModelResponse

Weather data model Response model.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets unique id auto generated for the weather data model type. | 
**created_at** | **datetime** | Gets or sets weather data model type creation date. | [optional] 
**last_modified_at** | **datetime** | Gets or sets weather data model type last updated date. | [optional] 
**weather_measures** | [**list[WeatherMeasure]**](WeatherMeasure.md) | Gets or sets list of Measurements supported by weather data location. | 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


