# ScannerRegistration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The unique identifier of this registration. | [optional] 
**name** | **str** | The name of this registration. | [optional] 
**description** | **str** | An optional description of this registration. | [optional] 
**url** | **str** | A base URL of the scanner adapter | [optional] 
**disabled** | **bool** | Indicate whether the registration is enabled or not | [optional] [default to False]
**is_default** | **bool** | Indicate if the registration is set as the system default one | [optional] [default to False]
**auth** | **str** | Specify what authentication approach is adopted for the HTTP communications. Supported types Basic\&quot;, \&quot;Bearer\&quot; and api key header \&quot;X-ScannerAdapter-API-Key\&quot;  | [optional] [default to '']
**access_credential** | **str** | An optional value of the HTTP Authorization header sent with each request to the Scanner Adapter API.  | [optional] 
**skip_cert_verify** | **bool** | Indicate if skip the certificate verification when sending HTTP requests | [optional] [default to False]
**use_internal_addr** | **bool** | Indicate whether use internal registry addr for the scanner to pull content or not | [optional] [default to False]
**create_time** | **datetime** | The creation time of this registration | [optional] 
**update_time** | **datetime** | The update time of this registration | [optional] 
**adapter** | **str** | Optional property to describe the name of the scanner registration | [optional] 
**vendor** | **str** | Optional property to describe the vendor of the scanner registration | [optional] 
**version** | **str** | Optional property to describe the version of the scanner registration | [optional] 
**health** | **str** | Indicate the healthy of the registration | [optional] [default to '']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


