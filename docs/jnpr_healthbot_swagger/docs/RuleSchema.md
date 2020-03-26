# RuleSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about the rule | [optional] 
**field** | [**list[RuleSchemaField]**](RuleSchemaField.md) |  | [optional] 
**function** | [**list[RuleSchemaFunction]**](RuleSchemaFunction.md) |  | [optional] 
**keys** | **list[str]** |  | [optional] 
**network_rule** | [**list[ERRORUNKNOWN]**](.md) | Flag to denote a network rule | [optional] 
**rule_frequency** | **str** | Frequency at which the rule’s field, reference, and vector elements should be computed. Required only when a rule doesn’t have a sensor defined. Specify integer &gt;&#x3D; 0 followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s | [optional] 
**rule_name** | **str** | Name of the rule. Should be of pattern [a-z][a-z0-9_-]* | 
**sensor** | [**list[RuleSchemaSensor1]**](RuleSchemaSensor1.md) |  | [optional] 
**synopsis** | **str** | Synopsis about the rule | [optional] 
**field_aggregation_time_range** | **str** | How much back in time should we look for field aggregation. Specify positive integer followed by s/m/h/d/w/y representing seconds/minutes/hours/days/weeks/years. Eg: 2s | [optional] 
**trigger** | [**list[RuleSchemaTrigger]**](RuleSchemaTrigger.md) |  | [optional] 
**variable** | [**list[RuleSchemaVariable]**](RuleSchemaVariable.md) | Playbook variable configuration | [optional] 
**vector** | [**list[RuleSchemaVector]**](RuleSchemaVector.md) |  | [optional] 
**rule_properties** | [**RuleSchemaRuleproperties**](RuleSchemaRuleproperties.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


