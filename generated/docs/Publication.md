# Publication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | Publication duration, ISO 8601 duration format | [optional] 
**ending_at** | **datetime** | Publication ending date: Format (ISO 8601) - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ. Cannot be modified | [optional] 
**starting_at** | **datetime** | Publication starting date: Format (ISO 8601) - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ. Cannot be modified | [optional] 
**status** | [**OfferStatus**](OfferStatus.md) |  | [optional] 
**ended_by** | **str** | Indicates the reason for ending the offer:  - &#x60;USER&#x60; - offer ended by the seller.  - &#x60;ADMIN&#x60; - offer ended by an admin.  - &#x60;EXPIRATION&#x60; - offer ended because all available items had been sold out or offer duration had expired (valid for    offers with specified duration).  - &#x60;ERROR&#x60; - offer ended due to internal problem with offer publication. The publication command responded with    success status, but further processing failed. | [optional] 
**republish** | **bool** | Whether to republish an offer after ending. Automatically republish offers or auctions:&lt;/br&gt; - &#x60;BUY_NOW&#x60; offer type are republished with initial stock, regardless of how many items you have sold.&lt;/br&gt; - &#x60;AUCTION&#x60; offer type are republished only if they were not concluded with purchase.&lt;/br&gt; - &#x60;ADVERTISEMENT&#x60; offer type cannot be republished. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


