# Pos

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID. When creating a point of service (Post) the field is ignored. It is required when updating (Put) a point of service. | [optional] 
**external_id** | **str** | ID from external client system. | [optional] 
**name** | **str** |  | 
**seller** | [**Seller**](Seller.md) |  | [optional] 
**type** | **str** | Indicates point type. The only valid value so far is PICKUP_POINT. | 
**address** | [**Address**](Address.md) |  | 
**phone_number** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**open_hours** | [**list[OpenHour]**](OpenHour.md) | Possible empty list of opening hours. | 
**service_time** | **str** | Delivery time / Time period for receipt. Date format ISO 8601 e.g. &#39;PT24H&#39; | [optional] 
**payments** | [**list[Payment]**](Payment.md) | An empty list of payment types is available. | [optional] 
**confirmation_type** | **str** | Confirmation method: AWAIT_CONTACT - We will inform you about the time of receipt, CALL_US - Please make an appointment, CONTACT_NOT_REQUIRED - Contact is not required. | 
**status** | **str** | Point of service status: ACTIVE - active, TEMPORARILY_CLOSED - temporarily closed, CLOSED_DOWN - closed down, DELETED - deleted. | 
**created_at** | **str** | Creation date. Date format (ISO 8601) - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ When creating (Post) or updating (Put) a point of service (Post) the field is ignored. | [optional] 
**updated_at** | **str** | Modification date. Date format (ISO 8601) - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ When creating (Post) or updating (Put) a point of service (Post) the field is ignored. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


