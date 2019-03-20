# coding: utf-8

# flake8: noqa
"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from openapi_client.models.additional_service_definition_request import AdditionalServiceDefinitionRequest
from openapi_client.models.additional_service_request import AdditionalServiceRequest
from openapi_client.models.additional_service_response import AdditionalServiceResponse
from openapi_client.models.additional_services_group import AdditionalServicesGroup
from openapi_client.models.additional_services_group_request import AdditionalServicesGroupRequest
from openapi_client.models.additional_services_group_response import AdditionalServicesGroupResponse
from openapi_client.models.additional_services_groups import AdditionalServicesGroups
from openapi_client.models.address import Address
from openapi_client.models.after_sales_services import AfterSalesServices
from openapi_client.models.answer import Answer
from openapi_client.models.attachment_declaration import AttachmentDeclaration
from openapi_client.models.attachment_file import AttachmentFile
from openapi_client.models.attachment_file_request import AttachmentFileRequest
from openapi_client.models.attachment_type import AttachmentType
from openapi_client.models.available_constraint import AvailableConstraint
from openapi_client.models.average_rates import AverageRates
from openapi_client.models.basic_definition_response import BasicDefinitionResponse
from openapi_client.models.benefit import Benefit
from openapi_client.models.benefit_specification import BenefitSpecification
from openapi_client.models.buyer_reference import BuyerReference
from openapi_client.models.campaign_request_dto import CampaignRequestDto
from openapi_client.models.campaign_response_dto import CampaignResponseDto
from openapi_client.models.caption import Caption
from openapi_client.models.categories_dto import CategoriesDto
from openapi_client.models.category import Category
from openapi_client.models.category_dto import CategoryDto
from openapi_client.models.category_id_dto import CategoryIdDto
from openapi_client.models.category_options_dto import CategoryOptionsDto
from openapi_client.models.category_parameter import CategoryParameter
from openapi_client.models.category_parameter_list import CategoryParameterList
from openapi_client.models.category_parameter_options import CategoryParameterOptions
from openapi_client.models.cells import Cells
from openapi_client.models.change_price import ChangePrice
from openapi_client.models.change_price_input import ChangePriceInput
from openapi_client.models.change_price_without_output import ChangePriceWithoutOutput
from openapi_client.models.checkout_form import CheckoutForm
from openapi_client.models.checkout_form_add_waybill_created import CheckoutFormAddWaybillCreated
from openapi_client.models.checkout_form_add_waybill_request import CheckoutFormAddWaybillRequest
from openapi_client.models.checkout_form_additional_service import CheckoutFormAdditionalService
from openapi_client.models.checkout_form_buyer_reference import CheckoutFormBuyerReference
from openapi_client.models.checkout_form_delivery_address import CheckoutFormDeliveryAddress
from openapi_client.models.checkout_form_delivery_method import CheckoutFormDeliveryMethod
from openapi_client.models.checkout_form_delivery_pickup_point import CheckoutFormDeliveryPickupPoint
from openapi_client.models.checkout_form_delivery_pickup_point_address import CheckoutFormDeliveryPickupPointAddress
from openapi_client.models.checkout_form_delivery_reference import CheckoutFormDeliveryReference
from openapi_client.models.checkout_form_discount import CheckoutFormDiscount
from openapi_client.models.checkout_form_invoice_address import CheckoutFormInvoiceAddress
from openapi_client.models.checkout_form_invoice_address_company import CheckoutFormInvoiceAddressCompany
from openapi_client.models.checkout_form_invoice_address_natural_person import CheckoutFormInvoiceAddressNaturalPerson
from openapi_client.models.checkout_form_invoice_info import CheckoutFormInvoiceInfo
from openapi_client.models.checkout_form_line_item import CheckoutFormLineItem
from openapi_client.models.checkout_form_order_waybill_response import CheckoutFormOrderWaybillResponse
from openapi_client.models.checkout_form_payment_provider import CheckoutFormPaymentProvider
from openapi_client.models.checkout_form_payment_reference import CheckoutFormPaymentReference
from openapi_client.models.checkout_form_payment_type import CheckoutFormPaymentType
from openapi_client.models.checkout_form_reference import CheckoutFormReference
from openapi_client.models.checkout_form_status import CheckoutFormStatus
from openapi_client.models.checkout_form_summary import CheckoutFormSummary
from openapi_client.models.checkout_forms import CheckoutForms
from openapi_client.models.command_output import CommandOutput
from openapi_client.models.command_task import CommandTask
from openapi_client.models.compatibility_list import CompatibilityList
from openapi_client.models.compatibility_list_item import CompatibilityListItem
from openapi_client.models.configuration import Configuration
from openapi_client.models.constraint_criteria import ConstraintCriteria
from openapi_client.models.contact_request import ContactRequest
from openapi_client.models.contact_response import ContactResponse
from openapi_client.models.contact_response_list import ContactResponseList
from openapi_client.models.coordinates import Coordinates
from openapi_client.models.definitions_response import DefinitionsResponse
from openapi_client.models.delivery import Delivery
from openapi_client.models.describes_listing_fee import DescribesListingFee
from openapi_client.models.describes_success_commission_fee import DescribesSuccessCommissionFee
from openapi_client.models.description_section import DescriptionSection
from openapi_client.models.description_section_item import DescriptionSectionItem
from openapi_client.models.description_section_item_image import DescriptionSectionItemImage
from openapi_client.models.description_section_item_text import DescriptionSectionItemText
from openapi_client.models.dictionary_category_parameter import DictionaryCategoryParameter
from openapi_client.models.dispute import Dispute
from openapi_client.models.dispute_attachment import DisputeAttachment
from openapi_client.models.dispute_attachment_id import DisputeAttachmentId
from openapi_client.models.dispute_author import DisputeAuthor
from openapi_client.models.dispute_author_role import DisputeAuthorRole
from openapi_client.models.dispute_checkout_form import DisputeCheckoutForm
from openapi_client.models.dispute_first_message import DisputeFirstMessage
from openapi_client.models.dispute_list_response import DisputeListResponse
from openapi_client.models.dispute_message import DisputeMessage
from openapi_client.models.dispute_message_author import DisputeMessageAuthor
from openapi_client.models.dispute_message_list import DisputeMessageList
from openapi_client.models.dispute_user import DisputeUser
from openapi_client.models.email_request import EmailRequest
from openapi_client.models.email_response import EmailResponse
from openapi_client.models.error import Error
from openapi_client.models.errors_holder import ErrorsHolder
from openapi_client.models.fee import Fee
from openapi_client.models.float_category_parameter import FloatCategoryParameter
from openapi_client.models.full_definition_response import FullDefinitionResponse
from openapi_client.models.general_report import GeneralReport
from openapi_client.models.header import Header
from openapi_client.models.image_url import ImageUrl
from openapi_client.models.implied_warranties_list_implied_warranty_basic import ImpliedWarrantiesListImpliedWarrantyBasic
from openapi_client.models.implied_warranty_basic import ImpliedWarrantyBasic
from openapi_client.models.inline_response200 import InlineResponse200
from openapi_client.models.inline_response2001 import InlineResponse2001
from openapi_client.models.inline_response2001_delivery_methods import InlineResponse2001DeliveryMethods
from openapi_client.models.inline_response200_shipping_rates import InlineResponse200ShippingRates
from openapi_client.models.integer_category_parameter import IntegerCategoryParameter
from openapi_client.models.just_id import JustId
from openapi_client.models.latest_order_event import LatestOrderEvent
from openapi_client.models.line_item_id_mappings import LineItemIdMappings
from openapi_client.models.line_item_id_mappings_mappings import LineItemIdMappingsMappings
from openapi_client.models.listing_category import ListingCategory
from openapi_client.models.listing_offer import ListingOffer
from openapi_client.models.listing_response import ListingResponse
from openapi_client.models.listing_response_categories import ListingResponseCategories
from openapi_client.models.listing_response_filters import ListingResponseFilters
from openapi_client.models.listing_response_filters_values import ListingResponseFiltersValues
from openapi_client.models.listing_response_offers import ListingResponseOffers
from openapi_client.models.listing_response_search_meta import ListingResponseSearchMeta
from openapi_client.models.listing_response_sort import ListingResponseSort
from openapi_client.models.location import Location
from openapi_client.models.message_author_role import MessageAuthorRole
from openapi_client.models.message_request import MessageRequest
from openapi_client.models.modification import Modification
from openapi_client.models.modification_delivery import ModificationDelivery
from openapi_client.models.modification_payments import ModificationPayments
from openapi_client.models.modification_promotion import ModificationPromotion
from openapi_client.models.modification_size_table import ModificationSizeTable
from openapi_client.models.monetary_amount import MonetaryAmount
from openapi_client.models.offer import Offer
from openapi_client.models.offer_attachment import OfferAttachment
from openapi_client.models.offer_attachment_request import OfferAttachmentRequest
from openapi_client.models.offer_category import OfferCategory
from openapi_client.models.offer_change_command import OfferChangeCommand
from openapi_client.models.offer_criterion import OfferCriterion
from openapi_client.models.offer_criterium import OfferCriterium
from openapi_client.models.offer_delivery import OfferDelivery
from openapi_client.models.offer_description import OfferDescription
from openapi_client.models.offer_fixed_price import OfferFixedPrice
from openapi_client.models.offer_id import OfferId
from openapi_client.models.offer_images import OfferImages
from openapi_client.models.offer_listing_dto_v1 import OfferListingDtoV1
from openapi_client.models.offer_listing_dto_v1_category import OfferListingDtoV1Category
from openapi_client.models.offer_listing_dto_v1_image import OfferListingDtoV1Image
from openapi_client.models.offer_listing_dto_v1_offer_status import OfferListingDtoV1OfferStatus
from openapi_client.models.offer_listing_dto_v1_offer_type import OfferListingDtoV1OfferType
from openapi_client.models.offer_listing_dto_v1_publication import OfferListingDtoV1Publication
from openapi_client.models.offer_listing_dto_v1_sale_info import OfferListingDtoV1SaleInfo
from openapi_client.models.offer_listing_dto_v1_selling_mode import OfferListingDtoV1SellingMode
from openapi_client.models.offer_listing_dto_v1_stats import OfferListingDtoV1Stats
from openapi_client.models.offer_listing_dto_v1_stock import OfferListingDtoV1Stock
from openapi_client.models.offer_lowest_price import OfferLowestPrice
from openapi_client.models.offer_price import OfferPrice
from openapi_client.models.offer_price_change_command import OfferPriceChangeCommand
from openapi_client.models.offer_promotion import OfferPromotion
from openapi_client.models.offer_publication import OfferPublication
from openapi_client.models.offer_quantity_change_command import OfferQuantityChangeCommand
from openapi_client.models.offer_quote_dto import OfferQuoteDto
from openapi_client.models.offer_quotes_dto import OfferQuotesDto
from openapi_client.models.offer_reference import OfferReference
from openapi_client.models.offer_seller import OfferSeller
from openapi_client.models.offer_seller_contact import OfferSellerContact
from openapi_client.models.offer_seller_contact_phones import OfferSellerContactPhones
from openapi_client.models.offer_selling_mode import OfferSellingMode
from openapi_client.models.offer_stock import OfferStock
from openapi_client.models.offer_vendor import OfferVendor
from openapi_client.models.offers_search_result_dto_v1 import OffersSearchResultDtoV1
from openapi_client.models.open_hour import OpenHour
from openapi_client.models.order import Order
from openapi_client.models.order_event import OrderEvent
from openapi_client.models.order_event_data import OrderEventData
from openapi_client.models.order_event_stats import OrderEventStats
from openapi_client.models.order_events_list import OrderEventsList
from openapi_client.models.order_line_item import OrderLineItem
from openapi_client.models.parameter import Parameter
from openapi_client.models.parameter_range_value import ParameterRangeValue
from openapi_client.models.parameters_for_preview_price import ParametersForPreviewPrice
from openapi_client.models.payment import Payment
from openapi_client.models.payments import Payments
from openapi_client.models.phones_request import PhonesRequest
from openapi_client.models.phones_response import PhonesResponse
from openapi_client.models.pos import Pos
from openapi_client.models.price import Price
from openapi_client.models.price_modification import PriceModification
from openapi_client.models.price_modification_fixed_price import PriceModificationFixedPrice
from openapi_client.models.price_modification_value_change import PriceModificationValueChange
from openapi_client.models.processing_status import ProcessingStatus
from openapi_client.models.promotion import Promotion
from openapi_client.models.promotion_campaign_request_dto import PromotionCampaignRequestDto
from openapi_client.models.promotion_campaign_response_dto import PromotionCampaignResponseDto
from openapi_client.models.promotion_campaigns_response_dto import PromotionCampaignsResponseDto
from openapi_client.models.promotion_request_dto import PromotionRequestDto
from openapi_client.models.promotion_response_dto import PromotionResponseDto
from openapi_client.models.public_table_dto import PublicTableDto
from openapi_client.models.public_table_image_dto import PublicTableImageDto
from openapi_client.models.public_tables_dto import PublicTablesDto
from openapi_client.models.publication import Publication
from openapi_client.models.publication_change_command_dto import PublicationChangeCommandDto
from openapi_client.models.publication_modification import PublicationModification
from openapi_client.models.quantity_modification import QuantityModification
from openapi_client.models.rates import Rates
from openapi_client.models.reference import Reference
from openapi_client.models.removal import Removal
from openapi_client.models.removal_request import RemovalRequest
from openapi_client.models.return_policies_list_return_policy_basic import ReturnPoliciesListReturnPolicyBasic
from openapi_client.models.return_policy_basic import ReturnPolicyBasic
from openapi_client.models.search_result import SearchResult
from openapi_client.models.seller import Seller
from openapi_client.models.seller_create_rebate_request_dto import SellerCreateRebateRequestDto
from openapi_client.models.seller_rebate_dto import SellerRebateDto
from openapi_client.models.seller_rebates_dto import SellerRebatesDto
from openapi_client.models.seller_reference import SellerReference
from openapi_client.models.selling_mode import SellingMode
from openapi_client.models.shipping_rates import ShippingRates
from openapi_client.models.shipping_rates_set import ShippingRatesSet
from openapi_client.models.shipping_rates_set_rates import ShippingRatesSetRates
from openapi_client.models.shipping_rates_set_rates_delivery_method import ShippingRatesSetRatesDeliveryMethod
from openapi_client.models.shipping_rates_set_rates_first_item_rate import ShippingRatesSetRatesFirstItemRate
from openapi_client.models.shipping_rates_set_rates_next_item_rate import ShippingRatesSetRatesNextItemRate
from openapi_client.models.shipping_rates_set_rates_shipping_time import ShippingRatesSetRatesShippingTime
from openapi_client.models.single_promotion_campaign_response_dto import SinglePromotionCampaignResponseDto
from openapi_client.models.stock import Stock
from openapi_client.models.string_category_parameter import StringCategoryParameter
from openapi_client.models.subject import Subject
from openapi_client.models.summary import Summary
from openapi_client.models.tag_id import TagId
from openapi_client.models.tag_ids_request import TagIdsRequest
from openapi_client.models.tag_list_response import TagListResponse
from openapi_client.models.tag_request import TagRequest
from openapi_client.models.tag_response import TagResponse
from openapi_client.models.task_count import TaskCount
from openapi_client.models.task_report import TaskReport
from openapi_client.models.user import User
from openapi_client.models.user_rating import UserRating
from openapi_client.models.user_rating_list_response import UserRatingListResponse
from openapi_client.models.user_rating_summary_response import UserRatingSummaryResponse
from openapi_client.models.validation import Validation
from openapi_client.models.validation_error import ValidationError
from openapi_client.models.variant_set import VariantSet
from openapi_client.models.variant_set_offer import VariantSetOffer
from openapi_client.models.variant_set_parameter import VariantSetParameter
from openapi_client.models.variant_sets import VariantSets
from openapi_client.models.variant_sets_variant_set import VariantSetsVariantSet
from openapi_client.models.warranties_list_warranty_basic import WarrantiesListWarrantyBasic
from openapi_client.models.warranty_basic import WarrantyBasic
from openapi_client.models.wrapper_type_for_preview_conditions import WrapperTypeForPreviewConditions
from openapi_client.models.wraps_listing_and_commissions_fees import WrapsListingAndCommissionsFees
