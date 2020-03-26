# DeviceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_model_id** | **str** | Gets or sets id of the associated Device Model. | 
**hardware_id** | **str** | Gets or sets unique id for the device such as MAC address etc. | 
**farm_id** | **str** | Gets or sets id of the farm to which the device is provisioned to.  Sensor Partners needs to ignore this field while creating and need to pass the old value while updating device. | [optional] 
**reporting_interval** | **int** | Gets or sets reporting interval of telemetry in seconds. | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**parent_device_id** | **str** | Gets or sets id of the parent device to which this device is connected to.  Eg.A Node connected to a Gateway; Node will have parentDeviceId as the Gateway. | [optional] 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


