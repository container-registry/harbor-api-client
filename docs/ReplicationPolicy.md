# ReplicationPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The policy ID. | [optional] 
**name** | **str** | The policy name. | [optional] 
**description** | **str** | The description of the policy. | [optional] 
**src_registry** | [**Registry**](Registry.md) |  | [optional] 
**dest_registry** | [**Registry**](Registry.md) |  | [optional] 
**dest_namespace** | **str** | The destination namespace. | [optional] 
**trigger** | [**ReplicationTrigger**](ReplicationTrigger.md) |  | [optional] 
**filters** | [**[ReplicationFilter]**](ReplicationFilter.md) | The replication policy filter array. | [optional] 
**replicate_deletion** | **bool** | Whether to replicate the deletion operation. | [optional] 
**deletion** | **bool** | Deprecated, use \&quot;replicate_deletion\&quot; instead. Whether to replicate the deletion operation. | [optional] 
**override** | **bool** | Whether to override the resources on the destination registry. | [optional] 
**enabled** | **bool** | Whether the policy is enabled or not. | [optional] 
**creation_time** | **datetime** | The create time of the policy. | [optional] 
**update_time** | **datetime** | The update time of the policy. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


