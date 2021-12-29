# WorkflowCronOptionsSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about this cron workflow options | [optional] 
**schedule** | **str** | Cron expression of time at which workflow will be run | 
**concurrency_policy** | **str** | Policy that determines what to do if multiple Workflows are scheduled at the same time | [optional] 
**starting_deadline_duration** | **str** | Duration after the last successful run during which a missed Workflow will be run | [optional] 
**successful_jobs_history_limit** | **int** | Number of successful Workflows that will be persisted at a time | [optional] 
**failed_jobs_history_limit** | **int** | Policy that determines what to do if multiple Workflows are scheduled at the same time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


