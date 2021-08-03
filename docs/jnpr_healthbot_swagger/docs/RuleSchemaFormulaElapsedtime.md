# RuleSchemaFormulaElapsedtime

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Field name on which elapsed operation needs to be performed | 
**hold_time** | **str** | How long previous value should be stored. Should match the pattern [0-9]*(seconds|minutes|hours|days|weeks|years|offset). Default is 1 day | [optional] 
**multiplication_factor** | **str** | Value to be multiplied with calculated time. Default is 1.0. Should be IEEE-754 64-bit floating-point numbers | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


