# NotificationSchemaAmqppublish

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange** | **str** | Name of exchange/routing agent of amqp on which connection has to be instantiated | 
**host** | **str** | Host is amqp server/broker valid hostname or IP address | 
**port** | **int** | Port is amqp server/broker listner port | 
**routing_key** | **str** | Routing key is a message attribute the exchange looks at when deciding how to route the message to queues. Should be of pattern \\.*[a-zA-Z0-9_-]+[a-zA-Z0-9\\._-]* , Default value is derived from &lt;device/network-group&gt;.&lt;device-id&gt;.&lt;topic&gt;.&lt;rule&gt;.&lt;trigger&gt; | [optional] 
**sasl** | [**NotificationSchemaAmqppublishSasl**](NotificationSchemaAmqppublishSasl.md) |  | [optional] 
**vhost** | **str** | Virtual host of amqp on which connection has to be instantiated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


