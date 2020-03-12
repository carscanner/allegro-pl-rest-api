# CategoryDto

The category data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the category. This can be either in UUID format or an integer format. You should be ready to accept any string value as the category ID. | [optional] 
**leaf** | **bool** | Indicates whether the category is at the lowest level. Leaf categories do not have any children. Offers can be listed only in leaf categories. | [optional] 
**name** | **str** | Name of the category in Polish. | [optional] 
**options** | [**CategoryOptionsDto**](CategoryOptionsDto.md) |  | [optional] 
**parent** | [**CategoryDtoParent**](CategoryDtoParent.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


