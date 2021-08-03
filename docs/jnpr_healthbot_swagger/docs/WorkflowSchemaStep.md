# WorkflowSchemaStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cli_command** | [**list[WorkflowCommandSchema]**](WorkflowCommandSchema.md) | Run CLI command(s) | [optional] 
**executable** | [**list[WorkflowCommandSchema]**](WorkflowCommandSchema.md) | Run an arbitrary executable file such as bash, python, ruby, etc. | [optional] 
**netconf_command** | [**list[WorkflowCommandSchema]**](WorkflowCommandSchema.md) | Run netconf command(s) | [optional] 
**notification** | [**list[WorkflowNotificationSchema]**](WorkflowNotificationSchema.md) | Send a notification message (configured under notification section) | [optional] 
**condition** | **list[str]** |  | [optional] 
**condition_description** | **str** | Description of the configured conditions | [optional] 
**condition_type** | **str** | Call the step if any of the conditions evaluates to true or all of the conditions evaluate to true (default any) | [optional] 
**dependencies** | **list[str]** |  | [optional] 
**description** | **str** | Description about the step being called | [optional] 
**input** | [**list[WorkflowSchemaInput]**](WorkflowSchemaInput.md) | Workflow input parameters configuration | [optional] 
**output** | [**list[WorkflowSchemaOutput]**](WorkflowSchemaOutput.md) | Workflow output parameters configuration | [optional] 
**step_name** | **str** | Name of the step being called. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 
**suspend** | [**WorkflowSchemaSuspend**](WorkflowSchemaSuspend.md) |  | [optional] 
**task** | [**WorkflowSchemaTask**](WorkflowSchemaTask.md) |  | [optional] 
**workflow** | [**WorkflowSchemaWorkflow**](WorkflowSchemaWorkflow.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


