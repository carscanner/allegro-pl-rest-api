# CheckoutForm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Checkout form id | 
**message_to_seller** | **str** | Message from buyer to seller | [optional] 
**buyer** | [**CheckoutFormBuyerReference**](CheckoutFormBuyerReference.md) |  | 
**payment** | [**CheckoutFormPaymentReference**](CheckoutFormPaymentReference.md) |  | [optional] 
**status** | [**CheckoutFormStatus**](CheckoutFormStatus.md) |  | 
**delivery** | [**CheckoutFormDeliveryReference**](CheckoutFormDeliveryReference.md) |  | [optional] 
**invoice** | [**CheckoutFormInvoiceInfo**](CheckoutFormInvoiceInfo.md) |  | 
**line_items** | [**list[CheckoutFormLineItem]**](CheckoutFormLineItem.md) |  | 
**surcharges** | [**list[CheckoutFormPaymentReference]**](CheckoutFormPaymentReference.md) |  | 
**discounts** | [**list[CheckoutFormDiscount]**](CheckoutFormDiscount.md) |  | 
**summary** | [**CheckoutFormSummary**](CheckoutFormSummary.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


