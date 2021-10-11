# Artifact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the artifact | [optional] 
**type** | **str** | The type of the artifact, e.g. image, chart, etc | [optional] 
**media_type** | **str** | The media type of the artifact | [optional] 
**manifest_media_type** | **str** | The manifest media type of the artifact | [optional] 
**project_id** | **int** | The ID of the project that the artifact belongs to | [optional] 
**repository_id** | **int** | The ID of the repository that the artifact belongs to | [optional] 
**digest** | **str** | The digest of the artifact | [optional] 
**size** | **int** | The size of the artifact | [optional] 
**icon** | **str** | The digest of the icon | [optional] 
**push_time** | **datetime** | The push time of the artifact | [optional] 
**pull_time** | **datetime** | The latest pull time of the artifact | [optional] 
**extra_attrs** | [**ExtraAttrs**](ExtraAttrs.md) |  | [optional] 
**annotations** | [**Annotations**](Annotations.md) |  | [optional] 
**references** | [**[Reference]**](Reference.md) |  | [optional] 
**tags** | [**[Tag]**](Tag.md) |  | [optional] 
**addition_links** | [**AdditionLinks**](AdditionLinks.md) |  | [optional] 
**labels** | [**[Label]**](Label.md) |  | [optional] 
**scan_overview** | [**ScanOverview**](ScanOverview.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


