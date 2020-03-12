# CheckoutFormAddWaybillRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_id** | **str** | Supported carriers:   * Polish carriers: &#x60;UPS&#x60;, &#x60;INPOST&#x60;, &#x60;DHL&#x60;, &#x60;GLS&#x60;, &#x60;RUCH&#x60;, &#x60;POCZTA_POLSKA&#x60;, &#x60;DPD&#x60;, &#x60;FEDEX&#x60;, &#x60;TNT_EXPRESS&#x60;, &#x60;DB_SCHENKER&#x60;, &#x60;RABEN&#x60;, &#x60;GEIS&#x60;, &#x60;DTS&#x60;, &#x60;PEKAES&#x60;, &#x60;PATRON&#x60;, &#x60;X_PRESS_COURIERS&#x60;, &#x60;RHENUS_LOGISTICS&#x60;   * International carriers: &#x60;YUN_EXPRESS&#x60;, &#x60;CHINA_POST&#x60;   * Other: &#x60;OTHER&#x60;  Carrier identifier taken from the dictionary below. It’s highly recommended to use an identifier different from &#x60;OTHER&#x60;, because its parcel status may be updated automatically. Carrier identifier &#x60;OTHER&#x60; is reserved for cases when seller uses a custom carrier or not yet integrated with Allegro. | 
**waybill** | **str** | Waybill number (parcel tracking number). Cannot be empty and must be no longer than 64 characters. It can contain any word character (equal to [a-zA-Z0-9_]) and special characters: parentheses and hyphen-minus. | 
**carrier_name** | **str** | Carrier name to be provided only if carrierId is OTHER, otherwise it’s ignored. Must be no longer than 30 characters. | [optional] 
**line_items** | **list[object]** | List of order line items. They must be from the order specified in the path parameter. List cannot be empty. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


