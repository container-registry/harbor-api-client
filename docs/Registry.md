# Registry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The registry ID. | [optional] 
**url** | **str** | The registry URL string. | [optional] 
**name** | **str** | The registry name. | [optional] 
**credential** | [**RegistryCredential**](RegistryCredential.md) |  | [optional] 
**type** | **str** | Type of the registry, e.g. &#39;harbor&#39;. | [optional] 
**insecure** | **bool** | Whether or not the certificate will be verified when Harbor tries to access the server. | [optional] 
**description** | **str** | Description of the registry. | [optional] 
**status** | **str** | Health status of the registry. | [optional] 
**creation_time** | **datetime** | The create time of the policy. | [optional] 
**update_time** | **datetime** | The update time of the policy. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


