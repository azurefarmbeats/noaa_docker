# RoleDefinitionResponse

Role Definition response model.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets unique id of role definition. | [optional] 
**created_at** | **datetime** | Gets or sets role definition creation date. | [optional] 
**last_modified_at** | **datetime** | Gets or sets role definition last updated date. | [optional] 
**permissions** | [**list[Permission]**](Permission.md) | Gets or sets permissions of the role definition. | 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


