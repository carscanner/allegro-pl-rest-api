# CommandTask

Status of single command task.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Modified field as JSON path. | [optional] 
**finished_at** | **datetime** | Date of completion of the modification. Format (ISO 8601) - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ | [optional] 
**message** | **str** | General fail reason. You should check the errors structure to get more detailed information of the encountered errors. | [optional] 
**offer** | [**OfferId**](OfferId.md) |  | [optional] 
**scheduled_at** | **datetime** | Date of the modification schedule. Format (ISO 8601) - yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ | [optional] 
**status** | **str** | Available statuses: NEW, SUCCESS, FAIL | [optional] 
**errors** | [**list[Error]**](Error.md) | The list of error objects explaining the problems with command processing for the given offer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


