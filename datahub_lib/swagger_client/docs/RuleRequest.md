# RuleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**farm_id** | **str** | Gets or sets id of the farm to which it is applied to. | 
**conditions** | [**list[Condition]**](Condition.md) | Gets or sets list of conditions in the Rule. | 
**severity_level** | **str** | Gets or sets severity level of the rule. | [optional] [default to 'Info']
**status** | **str** | Gets or sets status of the rule. | [optional] [default to 'Enabled']
**actions** | [**list[IAction]**](IAction.md) | Gets or sets actions configuration of the rule. | [optional] 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


