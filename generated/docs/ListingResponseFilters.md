# ListingResponseFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the filter. Should be used as query parameter key, optionally followed by idSuffix from parameter value (only for NUMERIC filters). | [optional] 
**type** | **str** | The type of the filter:   - *MULTI* - multiple choice filter,  - *SINGLE* - single select (dropdown) filter,  - *NUMERIC* - range of numeric values (search offers with value matching this range),  - *NUMERIC_SINGLE* - single numeric value (search offers with given value matching the range defined in offer),  - *TEXT* - filter allowing user to input any text. | [optional] 
**name** | **str** | Name of the filter. | [optional] 
**values** | [**list[ListingResponseFiltersValues]**](ListingResponseFiltersValues.md) | Available filter values. | [optional] 
**min_value** | **float** | Minimum valid value for filters of type NUMERIC. | [optional] 
**max_value** | **float** | Maximum valid value for filters of type NUMERIC. | [optional] 
**unit** | **str** | Unit of the NUMERIC/NUMERIC_SINGLE filter. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


