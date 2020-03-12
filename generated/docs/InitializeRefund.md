# InitializeRefund

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment** | [**RefundPayment**](RefundPayment.md) |  | 
**reason** | **str** | Reason for a payment refund. | 
**line_items** | [**list[RefundLineItem]**](RefundLineItem.md) | List of order&#39;s line items which can be refunded. | [optional] 
**delivery** | [**InitializeRefundDelivery**](InitializeRefundDelivery.md) |  | [optional] 
**overpaid** | [**InitializeRefundOverpaid**](InitializeRefundOverpaid.md) |  | [optional] 
**surcharges** | [**list[PaymentsSurcharge]**](PaymentsSurcharge.md) | List of surcharges for payment which can be refunded. | [optional] 
**additional_services** | [**InitializeRefundAdditionalServices**](InitializeRefundAdditionalServices.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


