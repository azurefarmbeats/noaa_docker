# JobRequest

Model to define a job input in the system.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **str** | Gets or sets Job type id for user-defined or system defined jobs.  &lt;remarks&gt;Refer /JobType APIs for more information.&lt;/remarks&gt; | 
**arguments** | **dict(str, object)** | Gets or sets job specific arguments specified in the corresponding Job Type.  &lt;remarks&gt;  If arguments are not in the format expected by the Job Type, you get a BAD Request.  These arguments will be passed directly  to the Azure Data Factory Pipeline run.  &lt;/remarks&gt; | [optional] 
**parent_job_id** | **str** | Gets or sets specify parent job id for this job.  &lt;remarks&gt;  If there is no parent of a job then it should be set to null.  It is user&#39;s responsibility to set correct parent job id for better job tracking and monitoring.  &lt;/remarks&gt; | [optional] 
**name** | **str** | Gets or sets name to identify resource. | 
**description** | **str** | Gets or sets textual description of resource. | [optional] 
**properties** | **dict(str, object)** | Gets or sets additional properties of the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


