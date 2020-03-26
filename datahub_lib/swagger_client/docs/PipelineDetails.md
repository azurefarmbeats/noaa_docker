# PipelineDetails

Wrapper class to keep all information related to a pipeline.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_group_name** | **str** | Gets or sets user may have multiple resource groups which must be registered with us.  Specify valid Resource Group Name where a desired pipeline is created. | [optional] 
**data_factory_name** | **str** | Gets or sets user may have multiple Data Factory resources which must be registered with us.  Specify valid Data Factory Name where a desired pipeline is created. | [optional] 
**pipeline_name** | **str** | Gets or sets Data Factory V2 pipeline name. | [optional] 
**parameters** | [**list[Parameter]**](Parameter.md) | Gets or sets specify list of allowed pipeline parameters  so that our system can put some validations while submitting a job. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


