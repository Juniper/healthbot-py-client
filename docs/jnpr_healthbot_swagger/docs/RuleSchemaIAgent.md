# RuleSchemaIAgent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | [**list[RuleSchemaIAgentArgs]**](RuleSchemaIAgentArgs.md) |  | [optional] 
**file** | **str** | File where table and views are defined | 
**frequency** | **str** | Frequency at which the iagent should execute the commands and extract the data. Specify positive integer followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s | 
**table** | **str** | Table which needs to be used to extract the data | 
**target** | **str** | To run command on FPC, specifiy FPC target (optional) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


