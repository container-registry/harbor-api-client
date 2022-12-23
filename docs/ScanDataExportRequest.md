# ScanDataExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_name** | **str** | Name of the scan data export job | [optional] 
**projects** | **list[int]** | A list of one or more projects for which to export the scan data, currently only one project is supported due to performance concerns, but define as array for extension in the future. | [optional] 
**labels** | **list[int]** | A list of one or more labels for which to export the scan data, defaults to all if empty | [optional] 
**repositories** | **str** | A list of repositories for which to export the scan data, defaults to all if empty | [optional] 
**cve_ids** | **str** | CVE-IDs for which to export data. Multiple CVE-IDs can be specified by separating using &#39;,&#39; and enclosed between &#39;{}&#39;. Defaults to all if empty | [optional] 
**tags** | **str** | A list of tags enclosed within &#39;{}&#39;. Defaults to all if empty | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


