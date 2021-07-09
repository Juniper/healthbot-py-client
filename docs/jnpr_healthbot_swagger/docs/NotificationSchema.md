# NotificationSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about the notification | [optional] 
**http_post** | [**NotificationSchemaHttppost**](NotificationSchemaHttppost.md) |  | [optional] 
**notification_name** | **str** | Name of the notification. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 
**slack** | [**NotificationSchemaSlack**](NotificationSchemaSlack.md) |  | [optional] 
**microsoft_teams** | [**NotificationSchemaMicrosoftteams**](NotificationSchemaMicrosoftteams.md) |  | [optional] 
**emails** | [**NotificationSchemaEmails**](NotificationSchemaEmails.md) |  | [optional] 
**kafka_publish** | [**NotificationSchemaKafkapublish**](NotificationSchemaKafkapublish.md) |  | [optional] 
**amqp_publish** | [**NotificationSchemaAmqppublish**](NotificationSchemaAmqppublish.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


