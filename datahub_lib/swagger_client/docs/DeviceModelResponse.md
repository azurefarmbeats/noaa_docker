# DeviceModelResponse

Device Model Response Object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets unique id auto generated for the device type. | 
**created_at** | **datetime** | Gets or sets device type creation date. | [optional] 
**last_modified_at** | **datetime** | Gets or sets device type last updated date. | [optional] 
**type** | **str** | Gets or sets type of the device. | 
**manufacturer** | **str** | Gets or sets manufacturer name of the device. | [optional] 
**product_code** | **str** | Gets or sets Device product code Or Model name/Number.  eg: EnviroMonitor#6800. | [optional] 
**ports** | [**list[DevicePort]**](DevicePort.md) | Gets or sets details of ports mapped on the device. | [optional] 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


