# RefundLineItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The line-item identifier. | 
**type** | **str** | Type for line items refund. QUANTITY is provided when you can refund one or more items. AMOUNT is provided when you can refund a partial price. | 
**quantity** | **float** | This field is provided for QUANTITY type only. It specifies how many items will be refunded. | [optional] 
**value** | [**RefundLineItemValue**](RefundLineItemValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


