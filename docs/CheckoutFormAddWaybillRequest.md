# CheckoutFormAddWaybillRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_id** | **str** | Carrier identifier taken from the dictionary below. It’s highly recommended to use an identifier different from OTHER, because its parcel status may be updated automatically. Carrier identifier OTHER is reserved for cases when seller uses a custom carrier or not yet integrated with Allegro. | 
**waybill** | **str** | Waybill number (parcel tracking number). Cannot be empty and must be no longer than 64 characters. It can contain any word character (equal to [a-zA-Z0-9_]) and special characters: parentheses and hyphen-minus. | 
**carrier_name** | **str** | Carrier name to be provided only if carrierId is OTHER, otherwise it’s ignored. Must be no longer than 30 characters. | [optional] 
**line_items** | **list[object]** | List of order line items. They must be from the order specified in the path parameter. List cannot be empty. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


