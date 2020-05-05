# DeviceSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**DevicegroupSchemaAuthentication**](DevicegroupSchemaAuthentication.md) |  | [optional] 
**description** | **str** | Description about the device | [optional] 
**device_id** | **str** | Identifier for the device. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 
**flow** | [**DeviceSchemaFlow**](DeviceSchemaFlow.md) |  | [optional] 
**host** | **str** | Name or IP of the device | 
**i_agent** | [**DeviceSchemaIAgent**](DeviceSchemaIAgent.md) |  | [optional] 
**open_config** | [**DeviceSchemaOpenconfig**](DeviceSchemaOpenconfig.md) |  | [optional] 
**snmp** | [**DeviceSchemaSnmp**](DeviceSchemaSnmp.md) |  | [optional] 
**syslog** | [**DeviceSchemaSyslog**](DeviceSchemaSyslog.md) |  | [optional] 
**timezone** | **str** | Timezone in the format +/-hh:mm, Example: -08:00 | [optional] 
**system_id** | **str** | ID which is sent in the JTI UDP messages | [optional] 
**variable** | [**list[DeviceSchemaVariable]**](DeviceSchemaVariable.md) | Playbook variable configuration | [optional] 
**vendor** | [**DeviceSchemaVendor**](DeviceSchemaVendor.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


