# GeneralInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_only** | **bool, none_type** | The flag to indicate whether Harbor is in readonly mode. | [optional] 
**authproxy_settings** | [**AuthproxySetting**](AuthproxySetting.md) |  | [optional] 
**harbor_version** | **str, none_type** | The build version of Harbor. | [optional] 
**notification_enable** | **bool, none_type** | The flag to indicate whether notification mechanism is enabled on Harbor instance. | [optional] 
**auth_mode** | **str, none_type** | The auth mode of current Harbor instance. | [optional] 
**self_registration** | **bool, none_type** | Indicate whether the Harbor instance enable user to register himself. | [optional] 
**external_url** | **str, none_type** | The external URL of Harbor, with protocol. | [optional] 
**project_creation_restriction** | **str, none_type** | Indicate who can create projects, it could be &#39;adminonly&#39; or &#39;everyone&#39;. | [optional] 
**has_ca_root** | **bool, none_type** | Indicate whether there is a ca root cert file ready for download in the file system. | [optional] 
**with_notary** | **bool, none_type** | If the Harbor instance is deployed with nested notary. | [optional] 
**registry_storage_provider_name** | **str, none_type** | The storage provider&#39;s name of Harbor registry | [optional] 
**with_chartmuseum** | **bool, none_type** | If the Harbor instance is deployed with nested chartmuseum. | [optional] 
**registry_url** | **str, none_type** | The url of registry against which the docker command should be issued. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


