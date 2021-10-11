# Schedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the schedule. | [optional] [readonly] 
**status** | **str** | The status of the schedule. | [optional] [readonly] 
**creation_time** | **datetime** | the creation time of the schedule. | [optional] [readonly] 
**update_time** | **datetime** | the update time of the schedule. | [optional] [readonly] 
**schedule** | [**ScheduleObj**](ScheduleObj.md) |  | [optional] 
**parameters** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** | The parameters of schedule job | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


