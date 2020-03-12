# ShippingRatesSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Shipping rates set ID (UUID) When creating a shipping rates set (Post) the field is ignored. It is required when updating (Put) a shipping rates. | [optional] 
**name** | **str** | User defined name of the shipping rates set. It may only contain: letters, numbers, hyphens, dots, commas and spaces. | [optional] 
**rates** | [**list[ShippingRate]**](ShippingRate.md) |  | 
**last_modified** | **str** | Date and time of the last modification of the set in UTC ISO 8601 format. When creating (Post) or updating (Put) a shipping rates set the field is ignored. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


