# RuleSchemaTrigger

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about the trigger | [optional] 
**frequency** | **str** | Frequency or time interval at which the trigger needs to be evaluated. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s | [optional] 
**synopsis** | **str** | Synopsis about the trigger | [optional] 
**disable_alarm_deduplication** | **list[object]** | Disable alarm deduplication, so that alarms are always generated | [optional] 
**term** | [**list[RuleSchemaTerm]**](RuleSchemaTerm.md) |  | 
**trigger_name** | **str** | Trigger name. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


