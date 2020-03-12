# ProposeSaleProductRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Suggested product name. | 
**category** | [**Category**](Category.md) |  | 
**eans** | **list[str]** | A list of codes that identify this product. Currently this can include EAN, ISBN, and UPC identifier types. | [optional] 
**images** | [**list[ImageUrl]**](ImageUrl.md) | List of product images. At least one image is required. | 
**parameters** | [**list[ProductParameter]**](ProductParameter.md) | List of product parameters. | 
**description** | [**StandardizedDescription**](StandardizedDescription.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


