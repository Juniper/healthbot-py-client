# PatternSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constant** | [**list[PatternSchemaConstant]**](PatternSchemaConstant.md) | Constant details | [optional] 
**description** | **str** | Pattern description | [optional] 
**event_id** | **str** | Event id that identifies a log uniquely. Field names also can be part of event-id. Example my-event+$field1 | 
**field** | [**list[PatternSchemaField]**](PatternSchemaField.md) | Field details | [optional] 
**filter** | **str** | Filter to match a log line | [optional] 
**filter_type** | **str** | Filter type, default is grok | [optional] 
**key_fields** | **list[str]** |  | [optional] 
**name** | **str** | Name of a pattern. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


