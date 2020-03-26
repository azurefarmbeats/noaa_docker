# AlertResponse

Defines Alert Response model.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets unique id auto generated for the alert. | 
**created_at** | **datetime** | Gets or sets alert creation date. | [optional] 
**last_modified_at** | **datetime** | Gets or sets alert last updated date. | [optional] 
**rule_description** | **str** | Gets or sets rule description. | [optional] 
**rule_severity** | **str** | Gets or sets rule severity. | [optional] 
**rule_id** | **str** | Gets or sets rule id. | 
**rule_actions** | [**list[IAction]**](IAction.md) | Gets or sets rule actions. | [optional] 
**device_id** | **str** | Gets or sets device id in a rule. | 
**device_msg_received** | **datetime** | Gets or sets last message received time. | [optional] 
**status** | **str** | Gets or sets a value indicating whether Alert is acknowledged. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


