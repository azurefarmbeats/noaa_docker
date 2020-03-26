# JobResponse

Model to define complete state of job in the system.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets system generated unique id. | [optional] 
**created_at** | **datetime** | Gets or sets job&#39;s creation date. | [optional] 
**last_modified_at** | **datetime** | Gets or sets job&#39;s last modified date. | [optional] 
**stop_requested** | **bool** | Gets or sets a value indicating whether flag indicating stop is requested by user or not. | [optional] 
**current_state** | **str** | Gets or sets current state of job. | [optional] 
**error** | **str** | Gets or sets error message if any.  &lt;remarks&gt;  This field is going be deprecated in favor of Status which has more detailed information.  &lt;/remarks&gt; | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**debug_info** | [**DebugInformation**](DebugInformation.md) |  | [optional] 
**info** | [**JobInfo**](JobInfo.md) |  | [optional] 
**type_id** | **str** | Gets or sets Job type id for user-defined or system defined jobs.  &lt;remarks&gt;Refer /JobType APIs for more information.&lt;/remarks&gt; | 
**arguments** | **dict(str, object)** | Gets or sets job specific arguments specified in the corresponding Job Type.  &lt;remarks&gt;  If arguments are not in the format expected by the Job Type, you get a BAD Request.  These arguments will be passed directly  to the Azure Data Factory Pipeline run.  &lt;/remarks&gt; | [optional] 
**parent_job_id** | **str** | Gets or sets specify parent job id for this job.  &lt;remarks&gt;  If there is no parent of a job then it should be set to null.  It is user&#39;s responsibility to set correct parent job id for better job tracking and monitoring.  &lt;/remarks&gt; | [optional] 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


