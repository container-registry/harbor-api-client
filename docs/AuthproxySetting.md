# AuthproxySetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_certificate** | **str** | The certificate to be pinned when connecting auth proxy. | [optional] 
**tokenreivew_endpoint** | **str** | The fully qualified URI of token review endpoint of authproxy, such as &#39;https://192.168.1.2:8443/tokenreview&#39; | [optional] 
**endpoint** | **str** | The fully qualified URI of login endpoint of authproxy, such as &#39;https://192.168.1.2:8443/login&#39; | [optional] 
**verify_cert** | **bool** | The flag to determine whether Harbor should verify the certificate when connecting to the auth proxy. | [optional] 
**skip_search** | **bool** | The flag to determine whether Harbor can skip search the user/group when adding him as a member. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


