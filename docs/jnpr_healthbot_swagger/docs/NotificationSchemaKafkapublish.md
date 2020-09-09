# NotificationSchemaKafkapublish

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootstrap_servers** | **list[str]** |  | 
**sasl** | [**NotificationSchemaKafkapublishSasl**](NotificationSchemaKafkapublishSasl.md) |  | [optional] 
**topic** | **str** | Kafka topic to which Healthbot should publish. Should be of pattern \\.*[a-zA-Z0-9_-]+[a-zA-Z0-9\\._-]* , Default value is derived from &lt;device/network-group&gt;.&lt;device-id&gt;.&lt;topic&gt;.&lt;rule&gt;.&lt;trigger&gt; | [optional] 
**use_hash_partitioner** | **bool** | If true, key will be generated which will be hashed to provide a consistent partition number for the given kafka topic | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


