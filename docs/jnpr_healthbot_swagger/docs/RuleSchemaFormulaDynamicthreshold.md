# RuleSchemaFormulaDynamicthreshold

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Algorithm used to learn the dynamic threshold value | 
**field_name** | **str** | Field name on which dynamic threshold needs to be applied | 
**learning_period** | **str** | Learning period to learn the dynamic threshold. Should be of pattern [1-9][0-9]*(\\.[0-9]+)?(offset|seconds|minutes|hours|days|weeks|years|o|s|m|h|d|w|y) | 
**pattern_periodicity** | **str** | Pattern periodicity. Should be of pattern [1-9][0-9]*(minutes|hours|days|weeks|months)(,[1-9][0-9]*(minutes|hours|days|weeks|months))* | [optional] 
**seasonality** | **str** | Seasonality. Should be of pattern [1-9][0-9]*(minutes|hours|days|weeks|months)(,[1-9][0-9]*(minutes|hours|days|weeks|months))* | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


