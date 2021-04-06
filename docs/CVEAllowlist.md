# CVEAllowlist

The CVE Allowlist for system or project

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_time** | **datetime** | The update time of the allowlist. | [optional] 
**items** | [**[CVEAllowlistItem]**](CVEAllowlistItem.md) |  | [optional] 
**project_id** | **int** | ID of the project which the allowlist belongs to.  For system level allowlist this attribute is zero. | [optional] 
**creation_time** | **datetime** | The creation time of the allowlist. | [optional] 
**id** | **int** | ID of the allowlist | [optional] 
**expires_at** | **int, none_type** | the time for expiration of the allowlist, in the form of seconds since epoch.  This is an optional attribute, if it&#39;s not set the CVE allowlist does not expire. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


