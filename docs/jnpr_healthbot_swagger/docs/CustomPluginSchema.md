# CustomPluginSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the identifier of this config, referred in sensor config under topic/rule | 
**parameters** | [**list[CustompluginSchemaParameters]**](CustompluginSchemaParameters.md) | Plugin specific parameters (config) | [optional] 
**plugin_name** | **str** | Name of the loaded input plugin of BYOI | [optional] 
**security_parameters** | [**CustompluginSchemaSecurityparameters**](CustompluginSchemaSecurityparameters.md) |  | [optional] 
**service_name** | **str** | Name of the service (docker container) which implements this plugin | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


