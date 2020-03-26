# JobTypeResponse

Job type response API model.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets unique id of job type. | [optional] 
**status** | **str** | Gets or sets status of JobType.  This status represents whether or not corresponding ADF pipeline has been successfully created. | [optional] 
**error_message** | **str** | Gets or sets error message.  Helps in debugging for the Partner JobTypes. | [optional] 
**created_at** | **datetime** | Gets or sets created date. | [optional] 
**last_modified_at** | **datetime** | Gets or sets last modified date. | [optional] 
**pipeline_details** | [**PipelineDetails**](PipelineDetails.md) |  | [optional] 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


