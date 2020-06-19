# AzureBatchDetails

Docker image hosting details.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_vmsku** | **str** | Gets or sets Azure Batch VM SKU.  Currently we only support linux VMs.  List of VM SKUs: https://docs.microsoft.com/en-us/azure/cloud-services/cloud-services-sizes-specs. | [default to 'standard_d3_v2']
**dedicated_computer_nodes** | **int** | Gets or sets dedicated computer nodes for batch pool. | [optional] [default to 1]
**node_agent_skuid** | **str** | Gets or sets Azure Batch Node Agent SKU ID.  Currently only \&quot;batch.node.ubuntu 18.04\&quot; batch node agent is supported. | [default to 'batch.node.ubuntu 18.04']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


