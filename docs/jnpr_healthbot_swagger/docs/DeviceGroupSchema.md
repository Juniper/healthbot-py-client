# DeviceGroupSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**DevicegroupSchemaAuthentication**](DevicegroupSchemaAuthentication.md) |  | [optional] 
**edge** | **str** | JFM: edge this device group belongs to. This should be of the format &lt;organization-name&gt;.&lt;site-name&gt;.&lt;edge-name&gt; | [optional] 
**description** | **str** | Description about the device group | [optional] 
**device_group_name** | **str** | Name of the group. Should be of pattern [a-zA-Z][a-zA-Z0-9-]* | 
**devices** | **list[str]** |  | [optional] 
**logging** | [**DevicegroupSchemaLogging**](DevicegroupSchemaLogging.md) |  | [optional] 
**native_gpb** | [**DevicegroupSchemaNativegpb**](DevicegroupSchemaNativegpb.md) |  | [optional] 
**flow** | [**DevicegroupSchemaFlow**](DevicegroupSchemaFlow.md) |  | [optional] 
**ingest_frequency** | **list[str]** |  | [optional] 
**raw_data** | [**DevicegroupSchemaRawdata**](DevicegroupSchemaRawdata.md) |  | [optional] 
**field_data** | [**DevicegroupSchemaFielddata**](DevicegroupSchemaFielddata.md) |  | [optional] 
**notification** | [**DevicegroupSchemaNotification**](DevicegroupSchemaNotification.md) |  | [optional] 
**open_config** | [**DevicegroupSchemaOpenconfig**](DevicegroupSchemaOpenconfig.md) |  | [optional] 
**outbound_ssh** | [**DevicegroupSchemaOutboundssh**](DevicegroupSchemaOutboundssh.md) |  | [optional] 
**playbooks** | **list[str]** |  | [optional] 
**publish** | [**DevicegroupSchemaPublish**](DevicegroupSchemaPublish.md) |  | [optional] 
**reports** | **list[str]** |  | [optional] 
**retention_policy** | **str** | Name of the retention policy to be applied | [optional] 
**root_cause_analysis** | [**DevicegroupSchemaRootcauseanalysis**](DevicegroupSchemaRootcauseanalysis.md) |  | [optional] 
**scheduler** | [**list[DevicegroupSchemaScheduler]**](DevicegroupSchemaScheduler.md) | List of schedulers associated with the playbook instances | [optional] 
**variable** | [**list[DevicegroupSchemaVariable]**](DevicegroupSchemaVariable.md) | Playbook variable configuration | [optional] 
**snmp** | [**DevicegroupSchemaSnmp**](DevicegroupSchemaSnmp.md) |  | [optional] 
**syslog** | [**DevicegroupSchemaSyslog**](DevicegroupSchemaSyslog.md) |  | [optional] 
**tagging_profile** | **list[str]** |  | [optional] 
**timezone** | **str** | Timezone in the format +/-hh:mm, Example: -08:00 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


