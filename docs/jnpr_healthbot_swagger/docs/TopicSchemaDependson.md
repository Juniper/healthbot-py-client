# TopicSchemaDependson

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depends_on_multiple_instances** | **bool** | Depends on multiple instances of the depends-on resource. One to many relationship. Eg: ae interface can be dependent on multiple interfaces | [optional] 
**description** | **str** | Description about the dependency | [optional] 
**resource_name** | **str** | Name of dependent resource &lt;topic-name&gt;/&lt;resource-name&gt;. Should be of pattern [a-z][a-z-]*(\\.{1}[a-z0-9-]+)*/[a-z][a-z0-9-]* | 
**term** | [**list[TopicSchemaTerm]**](TopicSchemaTerm.md) |  | 
**triggered_by** | **list[str]** |  | [optional] 
**with_capture_group** | [**list[TopicSchemaWithcapturegroup]**](TopicSchemaWithcapturegroup.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


