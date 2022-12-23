# ReplicationPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The policy ID. | [optional] 
**name** | **str** | The policy name. | [optional] 
**description** | **str** | The description of the policy. | [optional] 
**src_registry** | [**Registry**](Registry.md) | The source registry. | [optional] 
**dest_registry** | [**Registry**](Registry.md) | The destination registry. | [optional] 
**dest_namespace** | **str** | The destination namespace. | [optional] 
**dest_namespace_replace_count** | **int** | Specify how many path components will be replaced by the provided destination namespace. The default value is -1 in which case the legacy mode will be applied. | [optional] 
**trigger** | [**ReplicationTrigger**](ReplicationTrigger.md) |  | [optional] 
**filters** | [**list[ReplicationFilter]**](ReplicationFilter.md) | The replication policy filter array. | [optional] 
**replicate_deletion** | **bool** | Whether to replicate the deletion operation. | [optional] 
**deletion** | **bool** | Deprecated, use \&quot;replicate_deletion\&quot; instead. Whether to replicate the deletion operation. | [optional] 
**override** | **bool** | Whether to override the resources on the destination registry. | [optional] 
**enabled** | **bool** | Whether the policy is enabled or not. | [optional] 
**creation_time** | **datetime** | The create time of the policy. | [optional] 
**update_time** | **datetime** | The update time of the policy. | [optional] 
**speed** | **int** | speed limit for each task | [optional] 
**copy_by_chunk** | **bool** | Whether to enable copy by chunk. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


