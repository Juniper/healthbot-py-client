# RuleSchemaWhenIncreasingatleastbyvalue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | [**list[ERRORUNKNOWN]**](.md) | With this flag, result is set to True only if all the data matches the given condition | [optional] 
**any** | [**list[ERRORUNKNOWN]**](.md) | With this flag, result is set to True if any one of the data matches the condition | [optional] 
**field_name** | **str** | Field name. Should match the pattern $[a-z][a-zA-Z0-9_-]* | 
**time_range** | **str** | How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s | [optional] 
**value** | **str** | Value of increase between current and last reported values | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


