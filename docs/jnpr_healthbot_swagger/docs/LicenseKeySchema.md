# LicenseKeySchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **str** | Unique ID of the license | 
**start_date** | **datetime** | License start date and time | 
**end_date** | **datetime** | License end date and time | 
**validity_type** | **str** | License validity type | 
**version** | **int** | License key version, an integer value indicating version of license vendor info | 
**sku_name** | **str** | License stock keeping unit name, indicates category of purchased license | 
**customer_id** | **str** | Identification of customer who has purchased this license | 
**order_type** | **str** | License purchase order type | 
**sw_serial_id** | **str** | Software serial number used for license activation | [optional] 
**mode** | **str** | License mode of operation | [optional] 
**features** | [**list[LicensekeySchemaFeatures]**](LicensekeySchemaFeatures.md) | Features which are part of the license | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


