# WorkflowCommandSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_tag** | **str** | Command tag | 
**commands** | [**list[WorkflowCommandSchemaCommands]**](WorkflowCommandSchemaCommands.md) | List of commands to execute | [optional] 
**ignore** | **list[object]** | Ignore if this command fails | [optional] 
**delay** | **str** | Delay between this command&#39;s repeated attempts | [optional] [default to '10s']
**repeat** | **float** | Repeat this command on failure | [optional] 
**type** | **str** | Type of the data produced or consumed | [optional] 
**arguments** | **list[str]** |  | [optional] 
**environment** | **list[str]** |  | [optional] 
**device** | **list[str]** |  | [optional] 
**device_group** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


