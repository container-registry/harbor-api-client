# ScannerRegistrationReq


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this registration | [optional] 
**url** | **str** | A base URL of the scanner adapter. | [optional] 
**access_credential** | **str** | An optional value of the HTTP Authorization header sent with each request to the Scanner Adapter API.  | [optional] 
**auth** | **str** | Specify what authentication approach is adopted for the HTTP communications. Supported types Basic\&quot;, \&quot;Bearer\&quot; and api key header \&quot;X-ScannerAdapter-API-Key\&quot;  | [optional]  if omitted the server will use the default value of ""
**disabled** | **bool** | Indicate whether the registration is enabled or not | [optional]  if omitted the server will use the default value of False
**use_internal_addr** | **bool** | Indicate whether use internal registry addr for the scanner to pull content or not | [optional]  if omitted the server will use the default value of False
**skip_cert_verify** | **bool** | Indicate if skip the certificate verification when sending HTTP requests | [optional]  if omitted the server will use the default value of False
**description** | **str** | An optional description of this registration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


