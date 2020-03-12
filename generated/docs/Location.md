# Location

for offer with a delivery method it is a parcel dispatch location. For offers with personal pick-up it is a pick-up location, additionally we recommend to use points of service (<a href=\"../../documentation/#tag/Points-of-service\" target=\"_blank\">https://developer.allegro.pl/documentation/#tag/Points-of-service</a>)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**post_code** | **str** |  | [optional] 
**province** | **str** | This field is mandatory if countryCode is set to \&quot;PL\&quot;, for other values, currently, it is ignored. For countryCode equalling \&quot;PL\&quot;, this field must be set to one of the following: DOLNOSLASKIE, KUJAWSKO_POMORSKIE, LUBELSKIE, LUBUSKIE, LODZKIE, MALOPOLSKIE, MAZOWIECKIE, OPOLSKIE, PODKARPACKIE, PODLASKIE, POMORSKIE, SLASKIE, SWIETOKRZYSKIE, WARMINSKO_MAZURSKIE, WIELKOPOLSKIE, ZACHODNIOPOMORSKIE. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


