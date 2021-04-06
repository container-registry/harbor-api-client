# ProjectMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_content_trust** | **str, none_type** | Whether content trust is enabled or not. If it is enabled, user can&#39;t pull unsigned images from this project. The valid values are \&quot;true\&quot;, \&quot;false\&quot;. | [optional] 
**public** | **str** | The public status of the project. The valid values are \&quot;true\&quot;, \&quot;false\&quot;. | [optional] 
**auto_scan** | **str, none_type** | Whether scan images automatically when pushing. The valid values are \&quot;true\&quot;, \&quot;false\&quot;. | [optional] 
**severity** | **str, none_type** | If the vulnerability is high than severity defined here, the images can&#39;t be pulled. The valid values are \&quot;none\&quot;, \&quot;low\&quot;, \&quot;medium\&quot;, \&quot;high\&quot;, \&quot;critical\&quot;. | [optional] 
**retention_id** | **str, none_type** | The ID of the tag retention policy for the project | [optional] 
**reuse_sys_cve_allowlist** | **str, none_type** | Whether this project reuse the system level CVE allowlist as the allowlist of its own.  The valid values are \&quot;true\&quot;, \&quot;false\&quot;. If it is set to \&quot;true\&quot; the actual allowlist associate with this project, if any, will be ignored. | [optional] 
**prevent_vul** | **str, none_type** | Whether prevent the vulnerable images from running. The valid values are \&quot;true\&quot;, \&quot;false\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


