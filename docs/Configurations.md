# Configurations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_mode** | **str** | The auth mode of current system, such as \&quot;db_auth\&quot;, \&quot;ldap_auth\&quot; | [optional] 
**count_per_project** | **str** | The default count quota for the new created projects. | [optional] 
**email_from** | **str** | The sender name for Email notification. | [optional] 
**email_host** | **str** | The hostname of SMTP server that sends Email notification. | [optional] 
**email_port** | **int** | The port of SMTP server. | [optional] 
**email_identity** | **str** | By default it&#39;s empty so the email_username is picked. | [optional] 
**email_username** | **str** | The username for authenticate against SMTP server. | [optional] 
**email_ssl** | **bool** | When it&#39;s set to true the system will access Email server via TLS by default.  If it&#39;s set to false, it still will handle \&quot;STARTTLS\&quot; from server side. | [optional] 
**email_insecure** | **bool** | Whether or not the certificate will be verified when Harbor tries to access the email server. | [optional] 
**ldap_url** | **str** | The URL of LDAP server. | [optional] 
**ldap_base_dn** | **str** | The Base DN for LDAP binding. | [optional] 
**ldap_filter** | **str** | The filter for LDAP binding. | [optional] 
**ldap_scope** | **int** | 0-LDAP_SCOPE_BASE, 1-LDAP_SCOPE_ONELEVEL, 2-LDAP_SCOPE_SUBTREE | [optional] 
**ldap_uid** | **str** | The attribute which is used as identity for the LDAP binding, such as \&quot;CN\&quot; or \&quot;SAMAccountname\&quot; | [optional] 
**ldap_search_dn** | **str** | The DN of the user to do the search. | [optional] 
**ldap_timeout** | **int** | timeout in seconds for connection to LDAP server. | [optional] 
**ldap_group_attribute_name** | **str** | The attribute which is used as identity of the LDAP group, default is cn. | [optional] 
**ldap_group_base_dn** | **str** | The base DN to search LDAP group. | [optional] 
**ldap_group_search_filter** | **str** | The filter to search the ldap group. | [optional] 
**ldap_group_search_scope** | **int** | The scope to search ldap. &#39;0-LDAP_SCOPE_BASE, 1-LDAP_SCOPE_ONELEVEL, 2-LDAP_SCOPE_SUBTREE&#39; | [optional] 
**ldap_group_admin_dn** | **str** | Specify the ldap group which have the same privilege with Harbor admin. | [optional] 
**oidc_client_id** | **str** | The client id of the OIDC. | [optional] 
**oidc_client_secret** | **str** | The client secret of the OIDC. | [optional] 
**oidc_endpoint** | **str** | The URL of an OIDC-complaint server, must start with &#39;https://&#39;. | [optional] 
**oidc_name** | **str** | The name of the OIDC provider. | [optional] 
**oidc_scope** | **str** | The scope sent to OIDC server during authentication, should be separated by comma. It has to contain “openid”, and “offline_access”. If you are using google, please remove “offline_access” from this field. | [optional] 
**oidc_verify_cert** | **bool** | Whether verify your OIDC server certificate, disable it if your OIDC server is hosted via self-hosted certificate. | [optional] 
**project_creation_restriction** | **str** | This attribute restricts what users have the permission to create project.  It can be \&quot;everyone\&quot; or \&quot;adminonly\&quot;. | [optional] 
**quota_per_project_enable** | **bool** | This attribute indicates whether quota per project enabled in harbor | [optional] 
**read_only** | **bool** | &#39;docker push&#39; is prohibited by Harbor if you set it to true.    | [optional] 
**self_registration** | **bool** | Whether the Harbor instance supports self-registration.  If it&#39;s set to false, admin need to add user to the instance. | [optional] 
**storage_per_project** | **str** | The default storage quota for the new created projects. | [optional] 
**token_expiration** | **int** | The expiration time of the token for internal Registry, in minutes. | [optional] 
**verify_remote_cert** | **bool** | Whether or not the certificate will be verified when Harbor tries to access a remote Harbor instance for replication. | [optional] 
**scan_all_policy** | [**ConfigurationsScanAllPolicy**](ConfigurationsScanAllPolicy.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


