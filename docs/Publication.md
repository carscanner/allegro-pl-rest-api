# Publication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | Publication duration, ISO 8601 duration format | [optional] 
**ending_at** | **datetime** | Publication ending date: Format (ISO 8601) - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ. Cannot be modified | [optional] 
**starting_at** | **datetime** | Publication starting date: Format (ISO 8601) - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ. Cannot be modified | [optional] 
**status** | **str** | Publication status, one of: INACTIVE, ACTIVATING, ACTIVE, ENDED | [optional] 
**ended_by** | **str** | The types of ended by can be as follows:&lt;/br&gt; - &#x60;USER&#x60; - offer ended by user.&lt;/br&gt; - &#x60;ADMIN&#x60; - offer ended by admin.&lt;/br&gt; - &#x60;EXPIRATION&#x60; - offer ended due to available items had sold out or offer duration had expired (valid for offers with specified duration).&lt;/br&gt; - &#x60;ERROR&#x60; - offer ended due to internal problem with offer publication. The publication command responded with success status, but further processing failed.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


