# CheckoutForm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Checkout form id | 
**message_to_seller** | **str** | Message from buyer to seller | [optional] 
**buyer** | [**CheckoutFormBuyerReference**](CheckoutFormBuyerReference.md) |  | 
**payment** | [**CheckoutFormPaymentReference**](CheckoutFormPaymentReference.md) |  | [optional] 
**status** | [**CheckoutFormStatus**](CheckoutFormStatus.md) |  | 
**fulfillment** | [**CheckoutFormFulfillment**](CheckoutFormFulfillment.md) |  | [optional] 
**delivery** | [**CheckoutFormDeliveryReference**](CheckoutFormDeliveryReference.md) |  | [optional] 
**invoice** | [**CheckoutFormInvoiceInfo**](CheckoutFormInvoiceInfo.md) |  | [optional] 
**line_items** | [**list[CheckoutFormLineItem]**](CheckoutFormLineItem.md) |  | 
**surcharges** | [**list[CheckoutFormPaymentReference]**](CheckoutFormPaymentReference.md) |  | 
**discounts** | [**list[CheckoutFormDiscount]**](CheckoutFormDiscount.md) |  | 
**summary** | [**CheckoutFormSummary**](CheckoutFormSummary.md) |  | 
**updated_at** | **str** | Provided in [ISO 8601 format](link: https://en.wikipedia.org/wiki/ISO_8601). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


