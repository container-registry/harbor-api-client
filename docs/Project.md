# Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_time** | **str** | The update time of the project. | [optional] 
**owner_name** | **str** | The owner name of the project. | [optional] 
**name** | **str** | The name of the project. | [optional] 
**deleted** | **bool** | A deletion mark of the project. | [optional] 
**owner_id** | **int** | The owner ID of the project always means the creator of the project. | [optional] 
**repo_count** | **int** | The number of the repositories under this project. | [optional] 
**chart_count** | **int** | The total number of charts under this project. | [optional] 
**creation_time** | **str** | The creation time of the project. | [optional] 
**togglable** | **bool** | Correspond to the UI about whether the project&#39;s publicity is updatable (for UI) | [optional] 
**current_user_role_id** | **int** | The role ID with highest permission of the current user who triggered the API (for UI).  This attribute is deprecated and will be removed in future versions. | [optional] 
**current_user_role_ids** | **[int]** | The list of role ID of the current user who triggered the API (for UI) | [optional] 
**cve_allowlist** | [**CVEAllowlist**](CVEAllowlist.md) |  | [optional] 
**project_id** | **int** | Project ID | [optional] 
**registry_id** | **int** | The ID of referenced registry when the project is a proxy cache project. | [optional] 
**metadata** | [**ProjectMetadata**](ProjectMetadata.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


