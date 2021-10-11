# ProjectMemberEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the project member id | [optional] 
**project_id** | **int** | the project id | [optional] 
**entity_name** | **str** | the name of the group member. | [optional] 
**role_name** | **str** | the name of the role | [optional] 
**role_id** | **int** | the role id | [optional] 
**entity_id** | **int** | the id of entity, if the member is a user, it is user_id in user table. if the member is a user group, it is the user group&#39;s ID in user_group table. | [optional] 
**entity_type** | **str** | the entity&#39;s type, u for user entity, g for group entity. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


