# RuleSchemaFormulaPredict

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Algorithm used to create baseline thresholds | 
**field_name** | **str** | Field name on which ML algorithm needs to be applied | 
**learning_period** | **str** | Learning period to learn the baseline threshold. Should be of pattern [1-9][0-9]*(seconds|minutes|hours|days|weeks|years|offset) | 
**pattern_periodicity** | **str** | Pattern periodicity. Should be of pattern [1-9][0-9]*(minutes|hours|days|weeks|months)(,[1-9][0-9]*(minutes|hours|days|weeks|months))* | 
**prediction_offset** | **str** | Time offset in future to predict. Should be of pattern [1-9][0-9]*(offset|seconds|minutes|hours|days|weeks|years|s|m|h|d|w|y) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


