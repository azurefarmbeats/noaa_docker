# SceneResponse

Scene response.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets system generated unique id. | [optional] 
**created_at** | **datetime** | Gets or sets scene&#39;s creation date. | [optional] 
**last_modified_at** | **datetime** | Gets or sets scene&#39;s last updated date. | [optional] 
**type** | **str** | Gets or sets type of scene.  &lt;remark&gt;Refer /ExtendedType APIs with key \&quot;SceneType\&quot; for more information.&lt;/remark&gt; | 
**source** | **str** | Gets or sets source of scene.  &lt;remark&gt;Refer /ExtendedType APIs with key \&quot;SceneSource\&quot; for more information.&lt;/remark&gt; | 
**farm_id** | **str** | Gets or sets farm id. | 
**date** | **datetime** | Gets or sets the nominal date of the scene. | 
**sequence** | **int** | Gets or sets sequence of the scene within a particular date.  When multiple scenes are available on the same date, each is assigned a different sequence number starting with 0. | [optional] [default to 0]
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


