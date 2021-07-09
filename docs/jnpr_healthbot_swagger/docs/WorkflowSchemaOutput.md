# WorkflowSchemaOutput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact** | [**WorkflowSchemaArtifact**](WorkflowSchemaArtifact.md) |  | [optional] 
**command_tag** | **str** | Command tag whose output is used for pattern match | [optional] 
**data_xml** | [**WorkflowSchemaDataxml**](WorkflowSchemaDataxml.md) |  | [optional] 
**description** | **str** | Exported output field desciption | [optional] 
**grok** | [**WorkflowSchemaGrok**](WorkflowSchemaGrok.md) |  | [optional] 
**json** | [**WorkflowSchemaJson**](WorkflowSchemaJson.md) |  | [optional] 
**name** | **str** | Output parameter name exported from the workflow. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 
**result** | **list[object]** | Export stdout output (stdout) of the step | [optional] 
**regex** | [**WorkflowSchemaRegex**](WorkflowSchemaRegex.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


