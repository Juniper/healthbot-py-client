# DeviceSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**DevicegroupSchemaAuthentication**](DevicegroupSchemaAuthentication.md) |  | [optional] 
**description** | **str** | Description about the device | [optional] 
**device_id** | **str** | Identifier for the device. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 
**uuid** | **str** | EMS: uuid of the EMS-advertised device | [optional] 
**flow** | [**DeviceSchemaFlow**](DeviceSchemaFlow.md) |  | [optional] 
**host** | **str** | Name or IP of the device | 
**i_agent** | [**DeviceSchemaIAgent**](DeviceSchemaIAgent.md) |  | [optional] 
**open_config** | [**DeviceSchemaOpenconfig**](DeviceSchemaOpenconfig.md) |  | [optional] 
**outbound_ssh** | [**DeviceSchemaOutboundssh**](DeviceSchemaOutboundssh.md) |  | [optional] 
**owner** | **str** | Owner of the device: this is a read-only attribute and should not be added to the request payload, value if added will be discarded. | [optional] 
**snmp** | [**DeviceSchemaSnmp**](DeviceSchemaSnmp.md) |  | [optional] 
**syslog** | [**DeviceSchemaSyslog**](DeviceSchemaSyslog.md) |  | [optional] 
**tagging_profile** | **list[str]** |  | [optional] 
**timezone** | **str** | Timezone in the format +/-hh:mm, Example: -08:00 | [optional] 
**system_id** | **str** | ID which is sent in the JTI UDP messages | [optional] 
**variable** | [**list[DeviceSchemaVariable]**](DeviceSchemaVariable.md) | Playbook variable configuration | [optional] 
**vendor** | [**DeviceSchemaVendor**](DeviceSchemaVendor.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


