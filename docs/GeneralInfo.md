# GeneralInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_time** | **datetime** | The current time of the server. | [optional] 
**with_notary** | **bool** | If the Harbor instance is deployed with nested notary. | [optional] 
**with_chartmuseum** | **bool** | If the Harbor instance is deployed with nested chartmuseum. | [optional] 
**registry_url** | **str** | The url of registry against which the docker command should be issued. | [optional] 
**external_url** | **str** | The external URL of Harbor, with protocol. | [optional] 
**auth_mode** | **str** | The auth mode of current Harbor instance. | [optional] 
**project_creation_restriction** | **str** | Indicate who can create projects, it could be &#39;adminonly&#39; or &#39;everyone&#39;. | [optional] 
**self_registration** | **bool** | Indicate whether the Harbor instance enable user to register himself. | [optional] 
**has_ca_root** | **bool** | Indicate whether there is a ca root cert file ready for download in the file system. | [optional] 
**harbor_version** | **str** | The build version of Harbor. | [optional] 
**registry_storage_provider_name** | **str** | The storage provider&#39;s name of Harbor registry | [optional] 
**read_only** | **bool** | The flag to indicate whether Harbor is in readonly mode. | [optional] 
**notification_enable** | **bool** | The flag to indicate whether notification mechanism is enabled on Harbor instance. | [optional] 
**authproxy_settings** | [**AuthproxySetting**](AuthproxySetting.md) | The setting of auth proxy this is only available when Harbor relies on authproxy for authentication. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


