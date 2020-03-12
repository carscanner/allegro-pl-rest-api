# Offer

Single offer data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_services** | [**JustId**](JustId.md) |  | [optional] 
**after_sales_services** | [**AfterSalesServices**](AfterSalesServices.md) |  | [optional] 
**attachments** | [**list[Attachment]**](Attachment.md) | List of offer attachments. You can attach up to 7 files to the offer – one per each attachment type as described in &lt;a href&#x3D;\&quot;/documentation/#operation/createOfferAttachmentUsingPOST\&quot; target&#x3D;\&quot;_blank\&quot;&gt;uploading offer attachments flow&lt;/a&gt;. | [optional] 
**category** | [**Category**](Category.md) |  | [optional] 
**compatibility_list** | [**CompatibilityList**](CompatibilityList.md) |  | [optional] 
**contact** | [**JustId**](JustId.md) |  | [optional] 
**created_at** | **datetime** | Creation date: Format (ISO 8601) - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ. Cannot be modified. | [optional] 
**delivery** | [**Delivery**](Delivery.md) |  | [optional] 
**description** | [**StandardizedDescription**](StandardizedDescription.md) |  | [optional] 
**ean** | **str** |  | [optional] 
**external** | [**ExternalId**](ExternalId.md) |  | [optional] 
**id** | **str** |  | [optional] 
**images** | [**list[ImageUrl]**](ImageUrl.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**name** | **str** | Name of the offer. Words used in the name field cannot be longer than 30 characters. | 
**parameters** | [**list[Parameter]**](Parameter.md) |  | [optional] 
**payments** | [**Payments**](Payments.md) |  | [optional] 
**product** | [**JustId**](JustId.md) |  | [optional] 
**promotion** | [**Promotion**](Promotion.md) |  | [optional] 
**publication** | [**Publication**](Publication.md) |  | [optional] 
**selling_mode** | [**SellingMode**](SellingMode.md) |  | [optional] 
**size_table** | [**JustId**](JustId.md) |  | [optional] 
**stock** | [**Stock**](Stock.md) |  | [optional] 
**tecdoc_specification** | [**TecdocSpecification**](TecdocSpecification.md) |  | [optional] 
**updated_at** | **datetime** | Last update date: Format (ISO 8601) - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ. Cannot be modified | [optional] 
**validation** | [**Validation**](Validation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


