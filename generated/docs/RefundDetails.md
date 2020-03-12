# RefundDetails

Detailed information about the refund.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The payment refund identifier. | 
**payment** | [**RefundPayment**](RefundPayment.md) |  | [optional] 
**reason** | **str** | Reason for a payment refund. | 
**status** | **str** | Current status of payment refund. | 
**created_at** | **datetime** | Date and time when the refund was created provided in ISO 8601 format. | 
**total_value** | [**RefundTotalValue**](RefundTotalValue.md) |  | 
**line_items** | [**list[RefundLineItem]**](RefundLineItem.md) | List of order&#39;s line items which can be refunded. | [optional] 
**delivery** | [**InitializeRefundDelivery**](InitializeRefundDelivery.md) |  | [optional] 
**overpaid** | [**InitializeRefundOverpaid**](InitializeRefundOverpaid.md) |  | [optional] 
**surcharges** | [**list[PaymentsSurcharge]**](PaymentsSurcharge.md) | List of surcharges for payment which can be refunded. | [optional] 
**additional_services** | [**InitializeRefundAdditionalServices**](InitializeRefundAdditionalServices.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


