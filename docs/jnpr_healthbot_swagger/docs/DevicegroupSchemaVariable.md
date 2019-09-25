# DevicegroupSchemaVariable

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | Unique ID of the variable instance. This should be unique per playbook and rule combination. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 
**playbook** | **str** | Name of the playbook in which the variable instance needs to be used | 
**rule** | **str** | Name of the rule. This must be of the format &lt;topic-name&gt;/&lt;rule-name&gt; | 
**running_state** | **str** | Current running state of the playbook instance | [optional] 
**variable_value** | [**list[DevicegroupSchemaVariablevalue]**](DevicegroupSchemaVariablevalue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


