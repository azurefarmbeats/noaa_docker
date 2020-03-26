# GetSceneFileResponse

Create scene file response.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_sas_url** | **str** | Gets or sets Shared Access URL (SAS) to download actual content of file using Azure blob storage client. | [optional] 
**id** | **str** | Gets or sets system generated unique id. | [optional] 
**created_at** | **datetime** | Gets or sets scene file&#39;s creation date. | [optional] 
**last_modified_at** | **datetime** | Gets or sets scene file&#39;s last updated date. | [optional] 
**blob_url** | **str** | Gets or sets blob path for actual content of file to download/upload if user has access to blob storage.  User should use Azure blob storage client to accomplish this. | [optional] 
**scene_id** | **str** | Gets or sets scene id. | 
**type** | **str** | Gets or sets type of scene file.  &lt;remark&gt;Refer /ExtendedType APIs with key \&quot;SceneFileType\&quot; for more information.&lt;/remark&gt; | 
**content_type** | **str** | Gets or sets content type of scene file.  &lt;remark&gt;Refer /ExtendedType APIs with key \&quot;SceneFileContentType\&quot; for more information.&lt;/remark&gt; | 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


