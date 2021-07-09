# WorkflowSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about this workflow | [optional] 
**entry_task** | **str** | Starting entry task of this workflow | [optional] 
**exit_task** | **str** | Exit/Cleanup task to invoke after the completion of the workflow | [optional] 
**argument** | [**WorkflowArgumentGroupSchema**](WorkflowArgumentGroupSchema.md) |  | [optional] 
**batch** | **int** | Maximum parallel steps launched | [optional] 
**retry** | [**RuleSchemaThenRetry**](RuleSchemaThenRetry.md) |  | [optional] 
**timeout** | **str** | Maximum time to wait for the step completion before bailing out (default 60 seconds) | [optional] 
**task** | [**list[WorkflowSchemaTask1]**](WorkflowSchemaTask1.md) | Task configuration which holds a list of steps to execute | [optional] 
**workflow_name** | **str** | Name of the workflow. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


