# UserResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**realname** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**sysadmin_flag** | **bool** |  | [optional] 
**admin_role_in_auth** | **bool** | indicate the admin privilege is grant by authenticator (LDAP), is always false unless it is the current login user | [optional] 
**oidc_user_meta** | [**OIDCUserInfo**](OIDCUserInfo.md) |  | [optional] 
**creation_time** | **datetime** | The creation time of the user. | [optional] 
**update_time** | **datetime** | The update time of the user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


