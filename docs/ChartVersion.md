# ChartVersion

A specified chart entry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** | The name of template engine | 
**app_version** | **str** | The version of the application enclosed in the chart | 
**api_version** | **str** | The API version of this chart | 
**name** | **str** | The name of the chart | 
**version** | **str** | A SemVer 2 version of chart | 
**icon** | **str** | The URL to an icon file | 
**labels** | [**Labels**](Labels.md) |  | [optional] 
**description** | **str** | A one-sentence description of chart | [optional] 
**deprecated** | **bool** | Whether or not this chart is deprecated | [optional] 
**sources** | **[str]** | The URL to the source code of chart | [optional] 
**keywords** | **[str]** | A list of string keywords | [optional] 
**home** | **str** | The URL to the relevant project page | [optional] 
**removed** | **bool** | A flag to indicate if the chart entry is removed | [optional] 
**digest** | **str** | The digest value of the chart entry | [optional] 
**urls** | **[str]** | The urls of the chart entry | [optional] 
**created** | **str** | The created time of the chart entry | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

