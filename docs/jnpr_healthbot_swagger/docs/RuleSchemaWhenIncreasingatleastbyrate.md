# RuleSchemaWhenIncreasingatleastbyrate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | [**list[ERRORUNKNOWN]**](.md) | With this flag, result is set to True only if all the data matches the given condition | [optional] 
**any** | [**list[ERRORUNKNOWN]**](.md) | With this flag, result is set to True if any one of the data matches the condition | [optional] 
**field_name** | **str** | Field name. Should match the pattern $[a-z][a-zA-Z0-9_-]* | 
**per** | **str** | Time unit part of rate | 
**time_range** | **str** | How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s | [optional] 
**value** | **str** | Value part of rate. This can be a float or field name from this rule and should match the pattern (\\d+(\\.\\d{0,2})?)|($[a-z][a-zA-Z0-9_-]*) | [optional] 
**percentage** | **str** | Percentage of change from previous value. This can be a float or field name from this rule and should match the pattern (\\d+(\\.\\d{0,2})?)|($[a-z][a-zA-Z0-9_-]*) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


