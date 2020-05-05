# RuleSchemaReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_if_missing** | [**RuleSchemaReferenceDataifmissing**](RuleSchemaReferenceDataifmissing.md) |  | [optional] 
**path** | **str** | Reference to a field or trigger in different rule. Format is /topic[topic-name&#x3D;&lt;topic-name&gt;]/rule[rule-name&#x3D;&lt;rule-name&gt;]/field[&lt;condition&gt;]/&lt;field-name&gt; for field reference and /topic[topic-name&#x3D;&lt;topic-name&gt;]/rule[rule-name&#x3D;&lt;rule-name&gt;]/trigger[trigger-name&#x3D;&lt;trigger-name&gt;]/key[condition]/trigger_field for trigger reference. Filtering part where field and key are mentioned is optional | 
**time_range** | **str** | How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


