# ScannerRegistration

Registration represents a named configuration for invoking a scanner via its adapter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Indicate whether the registration is enabled or not | [optional]  if omitted the server will use the default value of False
**vendor** | **str** | Optional property to describe the vendor of the scanner registration | [optional] 
**description** | **str** | An optional description of this registration. | [optional] 
**url** | **str** | A base URL of the scanner adapter | [optional] 
**adapter** | **str** | Optional property to describe the name of the scanner registration | [optional] 
**access_credential** | **str** | An optional value of the HTTP Authorization header sent with each request to the Scanner Adapter API.  | [optional] 
**uuid** | **str** | The unique identifier of this registration. | [optional] 
**auth** | **str** | Specify what authentication approach is adopted for the HTTP communications. Supported types Basic\&quot;, \&quot;Bearer\&quot; and api key header \&quot;X-ScannerAdapter-API-Key\&quot;  | [optional]  if omitted the server will use the default value of ""
**is_default** | **bool** | Indicate if the registration is set as the system default one | [optional]  if omitted the server will use the default value of False
**version** | **str** | Optional property to describe the version of the scanner registration | [optional] 
**health** | **str** | Indicate the healthy of the registration | [optional]  if omitted the server will use the default value of ""
**use_internal_addr** | **bool** | Indicate whether use internal registry addr for the scanner to pull content or not | [optional]  if omitted the server will use the default value of False
**skip_cert_verify** | **bool** | Indicate if skip the certificate verification when sending HTTP requests | [optional]  if omitted the server will use the default value of False
**name** | **str** | The name of this registration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


