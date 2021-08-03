# WorkflowInstanceSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about this workflow instance | [optional] 
**created_at** | **str** | Workflow instance creation time | [optional] 
**started_at** | **str** | Workflow instance startup time | [optional] 
**finished_at** | **str** | Workflow instance completion time | [optional] 
**status** | **str** | Workflow instance current status | [optional] 
**message** | **str** | Workflow instance current status message | [optional] 
**devices** | **list[str]** |  | [optional] 
**device_groups** | **list[str]** |  | [optional] 
**parameters** | [**list[WorkflowInstanceSchemaParameters]**](WorkflowInstanceSchemaParameters.md) |  | [optional] 
**argument** | [**WorkflowArgumentGroupSchema**](WorkflowArgumentGroupSchema.md) |  | [optional] 
**batch** | **int** | Maximum parallel steps launched | [optional] 
**retry** | [**RuleSchemaThenRetry**](RuleSchemaThenRetry.md) |  | [optional] 
**timeout** | **str** | Maximum time to wait for the step completion before bailing out (default 60 seconds) | [optional] 
**workflow_instance_name** | **str** | Name of the workflow instance | [optional] 
**workflow_name** | **str** | Name of the workflow. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


