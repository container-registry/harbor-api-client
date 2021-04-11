# ConfigurationsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_mode** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**count_per_project** | [**IntegerConfigItem**](IntegerConfigItem.md) |  | [optional] 
**email_from** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**email_host** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**email_port** | [**IntegerConfigItem**](IntegerConfigItem.md) |  | [optional] 
**email_identity** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**email_username** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**email_ssl** | [**BoolConfigItem**](BoolConfigItem.md) |  | [optional] 
**email_insecure** | [**BoolConfigItem**](BoolConfigItem.md) |  | [optional] 
**ldap_url** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**ldap_base_dn** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**ldap_filter** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**ldap_scope** | **int** | 0-LDAP_SCOPE_BASE, 1-LDAP_SCOPE_ONELEVEL, 2-LDAP_SCOPE_SUBTREE | [optional] 
**ldap_uid** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**ldap_search_dn** | **str** | The DN of the user to do the search. | [optional] 
**ldap_timeout** | [**IntegerConfigItem**](IntegerConfigItem.md) |  | [optional] 
**ldap_group_attribute_name** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**ldap_group_base_dn** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**ldap_group_search_filter** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**ldap_group_search_scope** | [**IntegerConfigItem**](IntegerConfigItem.md) |  | [optional] 
**ldap_group_admin_dn** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**oidc_client_id** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**oidc_endpoint** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**oidc_name** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**oidc_scope** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**oidc_verify_cert** | [**BoolConfigItem**](BoolConfigItem.md) |  | [optional] 
**project_creation_restriction** | [**StringConfigItem**](StringConfigItem.md) |  | [optional] 
**quota_per_project_enable** | [**BoolConfigItem**](BoolConfigItem.md) |  | [optional] 
**read_only** | [**BoolConfigItem**](BoolConfigItem.md) |  | [optional] 
**self_registration** | [**BoolConfigItem**](BoolConfigItem.md) |  | [optional] 
**storage_per_project** | [**IntegerConfigItem**](IntegerConfigItem.md) |  | [optional] 
**token_expiration** | [**IntegerConfigItem**](IntegerConfigItem.md) |  | [optional] 
**verify_remote_cert** | [**BoolConfigItem**](BoolConfigItem.md) |  | [optional] 
**scan_all_policy** | [**ConfigurationsScanAllPolicy**](ConfigurationsScanAllPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


