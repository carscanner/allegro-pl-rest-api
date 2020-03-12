# SaleProductDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product id. | 
**name** | **str** | Product name. | 
**category** | [**Category**](Category.md) |  | 
**eans** | **list[str]** | A list of codes that identify this product. Currently this can include EAN, ISBN, and UPC identifier types. | [optional] 
**images** | [**list[ImageUrl]**](ImageUrl.md) | List of product images. | [optional] 
**parameters** | [**list[ProductParameter]**](ProductParameter.md) | List of product parameters. | [optional] 
**offer_requirements** | [**OfferRequirements**](OfferRequirements.md) |  | [optional] 
**compatibility_list** | [**SaleProductCompatibilityList**](SaleProductCompatibilityList.md) |  | [optional] 
**tecdoc_specification** | [**TecdocSpecification**](TecdocSpecification.md) |  | [optional] 
**description** | [**StandardizedDescription**](StandardizedDescription.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


