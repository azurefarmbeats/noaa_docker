# AzureBatchDetails

Docker image hosting details.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_vmsku** | **str** | Gets or sets Azure Batch VM SKU.  Visit https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes?toc&#x3D;%2fazure%2fvirtual-machines%2flinux%2ftoc.json for all Linux virtual machines available. | 
**dedicated_computer_nodes** | **int** | Gets or sets dedicated computer nodes for batch pool.  Default value is 1. | [optional] [default to 1]
**node_agent_skuid** | **str** | Gets or sets Azure Batch Node Agent SKU ID.  Currently only \&quot;batch.node.ubuntu 16.04\&quot; batch node agent is supported. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


