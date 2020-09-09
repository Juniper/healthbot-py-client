# TsdbPostBodyItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_name** | **str** | Name of the query object. Optional. Not used for now | [optional] 
**device_group** | **str** | Name of the deviceGroup(s). Multiple device groups should be separated by &#39;,&#39;. This can be used in combination with device, but is not mandatory. If device is given, then query will be executed only for that particular devices in the given device group, else all devices in group will be considered. Given devices will be applicable for all give device-groups. | [optional] 
**device** | **str** | Name of the device. Multiple device should be separated by &#39;,&#39;. This should be used along with deviceGroup. Without deviceGroup, this config will not be considered | [optional] 
**db** | **str** | Name of the database. Multiple databases should be separated by &#39;,&#39;. &#39;*&#39; can be used to specify all databases. | [optional] 
**topic** | **str** | Name of Healthbot topic. Optional if measurement is used | [optional] 
**rule** | **str** | Name of Healthbot rule. Required if topic is used. Optional if measurement is used | [optional] 
**trigger** | **str** | Name of Healthbot trigger. Optional if measurement is used or rule table is being queried | [optional] 
**measurement** | **str** | Name of the measurement. Optional if topic/rule/trigger is used | [optional] 
**where** | **str** | Where clause filters data based on fields, tags, and/or timestamps. Eg: where&#x3D;\&quot;interface-name\&quot; &#x3D; &#39;ge-0/0/1&#39; and \&quot;in-pkts\&quot; &gt; 0 | [optional] 
**order** | **str** | Sort points in descending order based on time. By default points will be sorted in ascending order. Eg: order&#x3D;desc | [optional] 
**limit** | **int** | Limit number of points in the result. If groupBy is used limit is applied per group. Eg: limit&#x3D;10 | [optional] 
**fields** | **list[str]** |  | [optional] 
**group_by** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


