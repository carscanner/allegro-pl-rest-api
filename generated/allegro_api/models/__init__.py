# coding: utf-8

# flake8: noqa
"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from allegro_api.models.additional_email import AdditionalEmail
from allegro_api.models.additional_email_request import AdditionalEmailRequest
from allegro_api.models.additional_emails_response import AdditionalEmailsResponse
from allegro_api.models.additional_service_definition_request import AdditionalServiceDefinitionRequest
from allegro_api.models.additional_service_request import AdditionalServiceRequest
from allegro_api.models.additional_service_response import AdditionalServiceResponse
from allegro_api.models.additional_services_group import AdditionalServicesGroup
from allegro_api.models.additional_services_group_request import AdditionalServicesGroupRequest
from allegro_api.models.additional_services_group_response import AdditionalServicesGroupResponse
from allegro_api.models.additional_services_groups import AdditionalServicesGroups
from allegro_api.models.address import Address
from allegro_api.models.after_sales_services import AfterSalesServices
from allegro_api.models.answer import Answer
from allegro_api.models.application_time_policy import ApplicationTimePolicy
from allegro_api.models.attachment import Attachment
from allegro_api.models.attachment_declaration import AttachmentDeclaration
from allegro_api.models.attachment_file import AttachmentFile
from allegro_api.models.attachment_file_request import AttachmentFileRequest
from allegro_api.models.attachment_type import AttachmentType
from allegro_api.models.auction_details import AuctionDetails
from allegro_api.models.auth_error import AuthError
from allegro_api.models.available_constraint import AvailableConstraint
from allegro_api.models.average_rates import AverageRates
from allegro_api.models.badge import Badge
from allegro_api.models.badge_application import BadgeApplication
from allegro_api.models.badge_application_bargain_price import BadgeApplicationBargainPrice
from allegro_api.models.badge_application_campaign import BadgeApplicationCampaign
from allegro_api.models.badge_application_market_price import BadgeApplicationMarketPrice
from allegro_api.models.badge_application_offer import BadgeApplicationOffer
from allegro_api.models.badge_application_prices import BadgeApplicationPrices
from allegro_api.models.badge_application_process import BadgeApplicationProcess
from allegro_api.models.badge_application_purchase_constraints import BadgeApplicationPurchaseConstraints
from allegro_api.models.badge_application_purchase_constraints_limit import BadgeApplicationPurchaseConstraintsLimit
from allegro_api.models.badge_application_purchase_constraints_limit_per_user import BadgeApplicationPurchaseConstraintsLimitPerUser
from allegro_api.models.badge_application_rejection_reason import BadgeApplicationRejectionReason
from allegro_api.models.badge_application_rejection_reason_message import BadgeApplicationRejectionReasonMessage
from allegro_api.models.badge_application_request import BadgeApplicationRequest
from allegro_api.models.badge_applications import BadgeApplications
from allegro_api.models.badge_campaign import BadgeCampaign
from allegro_api.models.badge_process import BadgeProcess
from allegro_api.models.badge_publication_time_policy import BadgePublicationTimePolicy
from allegro_api.models.badges_list import BadgesList
from allegro_api.models.base_operation import BaseOperation
from allegro_api.models.basic_definition_response import BasicDefinitionResponse
from allegro_api.models.benefit import Benefit
from allegro_api.models.benefit_specification import BenefitSpecification
from allegro_api.models.bid_request import BidRequest
from allegro_api.models.black_list_paged_response import BlackListPagedResponse
from allegro_api.models.black_list_response import BlackListResponse
from allegro_api.models.blacklist_request import BlacklistRequest
from allegro_api.models.blacklist_user import BlacklistUser
from allegro_api.models.bundle_benefit_specification import BundleBenefitSpecification
from allegro_api.models.bundle_benefit_specification_all_of import BundleBenefitSpecificationAllOf
from allegro_api.models.buy_now_price import BuyNowPrice
from allegro_api.models.buyer_participant import BuyerParticipant
from allegro_api.models.buyer_participant_all_of import BuyerParticipantAllOf
from allegro_api.models.buyer_reference import BuyerReference
from allegro_api.models.campaign_refusal_reason import CampaignRefusalReason
from allegro_api.models.campaign_request_dto import CampaignRequestDto
from allegro_api.models.campaign_response_dto import CampaignResponseDto
from allegro_api.models.caption import Caption
from allegro_api.models.categories_dto import CategoriesDto
from allegro_api.models.category import Category
from allegro_api.models.category_dto import CategoryDto
from allegro_api.models.category_dto_parent import CategoryDtoParent
from allegro_api.models.category_options_dto import CategoryOptionsDto
from allegro_api.models.category_parameter import CategoryParameter
from allegro_api.models.category_parameter_list import CategoryParameterList
from allegro_api.models.category_parameter_options import CategoryParameterOptions
from allegro_api.models.category_product_parameter import CategoryProductParameter
from allegro_api.models.category_product_parameter_list import CategoryProductParameterList
from allegro_api.models.cells import Cells
from allegro_api.models.change_price import ChangePrice
from allegro_api.models.change_price_input import ChangePriceInput
from allegro_api.models.change_price_without_output import ChangePriceWithoutOutput
from allegro_api.models.checkout_form import CheckoutForm
from allegro_api.models.checkout_form_add_waybill_created import CheckoutFormAddWaybillCreated
from allegro_api.models.checkout_form_add_waybill_request import CheckoutFormAddWaybillRequest
from allegro_api.models.checkout_form_additional_service import CheckoutFormAdditionalService
from allegro_api.models.checkout_form_buyer_address_reference import CheckoutFormBuyerAddressReference
from allegro_api.models.checkout_form_buyer_reference import CheckoutFormBuyerReference
from allegro_api.models.checkout_form_delivery_address import CheckoutFormDeliveryAddress
from allegro_api.models.checkout_form_delivery_method import CheckoutFormDeliveryMethod
from allegro_api.models.checkout_form_delivery_pickup_point import CheckoutFormDeliveryPickupPoint
from allegro_api.models.checkout_form_delivery_pickup_point_address import CheckoutFormDeliveryPickupPointAddress
from allegro_api.models.checkout_form_delivery_reference import CheckoutFormDeliveryReference
from allegro_api.models.checkout_form_delivery_time import CheckoutFormDeliveryTime
from allegro_api.models.checkout_form_delivery_time_guaranteed import CheckoutFormDeliveryTimeGuaranteed
from allegro_api.models.checkout_form_discount import CheckoutFormDiscount
from allegro_api.models.checkout_form_fulfillment import CheckoutFormFulfillment
from allegro_api.models.checkout_form_fulfillment_shipment_summary import CheckoutFormFulfillmentShipmentSummary
from allegro_api.models.checkout_form_fulfillment_shipment_summary_line_items_sent import CheckoutFormFulfillmentShipmentSummaryLineItemsSent
from allegro_api.models.checkout_form_fulfillment_status import CheckoutFormFulfillmentStatus
from allegro_api.models.checkout_form_invoice_address import CheckoutFormInvoiceAddress
from allegro_api.models.checkout_form_invoice_address_company import CheckoutFormInvoiceAddressCompany
from allegro_api.models.checkout_form_invoice_address_natural_person import CheckoutFormInvoiceAddressNaturalPerson
from allegro_api.models.checkout_form_invoice_info import CheckoutFormInvoiceInfo
from allegro_api.models.checkout_form_line_item import CheckoutFormLineItem
from allegro_api.models.checkout_form_order_waybill_response import CheckoutFormOrderWaybillResponse
from allegro_api.models.checkout_form_payment_provider import CheckoutFormPaymentProvider
from allegro_api.models.checkout_form_payment_reference import CheckoutFormPaymentReference
from allegro_api.models.checkout_form_payment_type import CheckoutFormPaymentType
from allegro_api.models.checkout_form_reference import CheckoutFormReference
from allegro_api.models.checkout_form_status import CheckoutFormStatus
from allegro_api.models.checkout_form_summary import CheckoutFormSummary
from allegro_api.models.checkout_forms import CheckoutForms
from allegro_api.models.classified_extension import ClassifiedExtension
from allegro_api.models.classified_package import ClassifiedPackage
from allegro_api.models.classified_package_config import ClassifiedPackageConfig
from allegro_api.models.classified_package_configs import ClassifiedPackageConfigs
from allegro_api.models.classified_packages import ClassifiedPackages
from allegro_api.models.classified_promotion import ClassifiedPromotion
from allegro_api.models.classified_publication import ClassifiedPublication
from allegro_api.models.classified_response import ClassifiedResponse
from allegro_api.models.classifieds_packages import ClassifiedsPackages
from allegro_api.models.command_output import CommandOutput
from allegro_api.models.command_task import CommandTask
from allegro_api.models.commission_response import CommissionResponse
from allegro_api.models.company import Company
from allegro_api.models.compatibility_list import CompatibilityList
from allegro_api.models.compatibility_list_id_item import CompatibilityListIdItem
from allegro_api.models.compatibility_list_id_item_additional_info import CompatibilityListIdItemAdditionalInfo
from allegro_api.models.compatibility_list_id_item_all_of import CompatibilityListIdItemAllOf
from allegro_api.models.compatibility_list_item import CompatibilityListItem
from allegro_api.models.compatibility_list_item_product_based import CompatibilityListItemProductBased
from allegro_api.models.compatibility_list_manual import CompatibilityListManual
from allegro_api.models.compatibility_list_manual_all_of import CompatibilityListManualAllOf
from allegro_api.models.compatibility_list_product_based import CompatibilityListProductBased
from allegro_api.models.compatibility_list_product_based_all_of import CompatibilityListProductBasedAllOf
from allegro_api.models.compatibility_list_supported_categories_dto import CompatibilityListSupportedCategoriesDto
from allegro_api.models.compatibility_list_supported_categories_dto_supported_categories import CompatibilityListSupportedCategoriesDtoSupportedCategories
from allegro_api.models.compatibility_list_supported_categories_dto_validation_rules import CompatibilityListSupportedCategoriesDtoValidationRules
from allegro_api.models.compatibility_list_text_item import CompatibilityListTextItem
from allegro_api.models.compatibility_list_text_item_all_of import CompatibilityListTextItemAllOf
from allegro_api.models.compatible_product_dto import CompatibleProductDto
from allegro_api.models.compatible_product_dto_attributes import CompatibleProductDtoAttributes
from allegro_api.models.compatible_product_dto_group import CompatibleProductDtoGroup
from allegro_api.models.compatible_products_groups_dto import CompatibleProductsGroupsDto
from allegro_api.models.compatible_products_groups_dto_groups import CompatibleProductsGroupsDtoGroups
from allegro_api.models.compatible_products_list_dto import CompatibleProductsListDto
from allegro_api.models.configuration import Configuration
from allegro_api.models.constraint_criteria import ConstraintCriteria
from allegro_api.models.contact_request import ContactRequest
from allegro_api.models.contact_response import ContactResponse
from allegro_api.models.contact_response_list import ContactResponseList
from allegro_api.models.contribution_operation import ContributionOperation
from allegro_api.models.contribution_operation_all_of import ContributionOperationAllOf
from allegro_api.models.coordinates import Coordinates
from allegro_api.models.correction_operation import CorrectionOperation
from allegro_api.models.correction_operation_all_of import CorrectionOperationAllOf
from allegro_api.models.current_price import CurrentPrice
from allegro_api.models.deduction import Deduction
from allegro_api.models.deduction_charge_operation import DeductionChargeOperation
from allegro_api.models.deduction_charge_operation_all_of import DeductionChargeOperationAllOf
from allegro_api.models.deduction_increase_operation import DeductionIncreaseOperation
from allegro_api.models.deduction_increase_operation_all_of import DeductionIncreaseOperationAllOf
from allegro_api.models.definitions_response import DefinitionsResponse
from allegro_api.models.delivery import Delivery
from allegro_api.models.delivery_settings_dto import DeliverySettingsDto
from allegro_api.models.delivery_settings_dto_custom_cost import DeliverySettingsDtoCustomCost
from allegro_api.models.delivery_settings_dto_free_delivery import DeliverySettingsDtoFreeDelivery
from allegro_api.models.delivery_settings_dto_join_policy import DeliverySettingsDtoJoinPolicy
from allegro_api.models.describes_listing_fee import DescribesListingFee
from allegro_api.models.describes_success_commission_fee import DescribesSuccessCommissionFee
from allegro_api.models.description_section import DescriptionSection
from allegro_api.models.description_section_item import DescriptionSectionItem
from allegro_api.models.description_section_item_image import DescriptionSectionItemImage
from allegro_api.models.description_section_item_image_all_of import DescriptionSectionItemImageAllOf
from allegro_api.models.description_section_item_text import DescriptionSectionItemText
from allegro_api.models.description_section_item_text_all_of import DescriptionSectionItemTextAllOf
from allegro_api.models.dictionary_category_parameter import DictionaryCategoryParameter
from allegro_api.models.dictionary_category_product_parameter import DictionaryCategoryProductParameter
from allegro_api.models.dictionary_category_product_parameter_all_of import DictionaryCategoryProductParameterAllOf
from allegro_api.models.dictionary_category_product_parameter_all_of_dictionary import DictionaryCategoryProductParameterAllOfDictionary
from allegro_api.models.dictionary_category_product_parameter_all_of_restrictions import DictionaryCategoryProductParameterAllOfRestrictions
from allegro_api.models.dispute import Dispute
from allegro_api.models.dispute_attachment import DisputeAttachment
from allegro_api.models.dispute_attachment_id import DisputeAttachmentId
from allegro_api.models.dispute_author import DisputeAuthor
from allegro_api.models.dispute_author_role import DisputeAuthorRole
from allegro_api.models.dispute_checkout_form import DisputeCheckoutForm
from allegro_api.models.dispute_first_message import DisputeFirstMessage
from allegro_api.models.dispute_list_response import DisputeListResponse
from allegro_api.models.dispute_message import DisputeMessage
from allegro_api.models.dispute_message_author import DisputeMessageAuthor
from allegro_api.models.dispute_message_list import DisputeMessageList
from allegro_api.models.dispute_user import DisputeUser
from allegro_api.models.email_request import EmailRequest
from allegro_api.models.email_response import EmailResponse
from allegro_api.models.error import Error
from allegro_api.models.errors_holder import ErrorsHolder
from allegro_api.models.external_id import ExternalId
from allegro_api.models.fee import Fee
from allegro_api.models.fee_preview_response import FeePreviewResponse
from allegro_api.models.float_category_parameter import FloatCategoryParameter
from allegro_api.models.float_category_product_parameter import FloatCategoryProductParameter
from allegro_api.models.float_category_product_parameter_all_of import FloatCategoryProductParameterAllOf
from allegro_api.models.float_category_product_parameter_all_of_restrictions import FloatCategoryProductParameterAllOfRestrictions
from allegro_api.models.full_definition_response import FullDefinitionResponse
from allegro_api.models.general_report import GeneralReport
from allegro_api.models.get_badge_campaigns_list import GetBadgeCampaignsList
from allegro_api.models.get_sale_products_response import GetSaleProductsResponse
from allegro_api.models.get_sale_products_response_next_page import GetSaleProductsResponseNextPage
from allegro_api.models.header import Header
from allegro_api.models.image_url import ImageUrl
from allegro_api.models.implied_warranties_list_implied_warranty_basic import ImpliedWarrantiesListImpliedWarrantyBasic
from allegro_api.models.implied_warranty import ImpliedWarranty
from allegro_api.models.implied_warranty_basic import ImpliedWarrantyBasic
from allegro_api.models.initialize_refund import InitializeRefund
from allegro_api.models.initialize_refund_additional_services import InitializeRefundAdditionalServices
from allegro_api.models.initialize_refund_delivery import InitializeRefundDelivery
from allegro_api.models.initialize_refund_overpaid import InitializeRefundOverpaid
from allegro_api.models.inline_response200 import InlineResponse200
from allegro_api.models.inline_response2001 import InlineResponse2001
from allegro_api.models.inline_response2001_delivery_methods import InlineResponse2001DeliveryMethods
from allegro_api.models.inline_response2001_shipping_rates_constraints import InlineResponse2001ShippingRatesConstraints
from allegro_api.models.inline_response2001_shipping_rates_constraints_first_item_rate import InlineResponse2001ShippingRatesConstraintsFirstItemRate
from allegro_api.models.inline_response2001_shipping_rates_constraints_max_quantity_per_package import InlineResponse2001ShippingRatesConstraintsMaxQuantityPerPackage
from allegro_api.models.inline_response2001_shipping_rates_constraints_next_item_rate import InlineResponse2001ShippingRatesConstraintsNextItemRate
from allegro_api.models.inline_response2001_shipping_rates_constraints_shipping_time import InlineResponse2001ShippingRatesConstraintsShippingTime
from allegro_api.models.inline_response2001_shipping_rates_constraints_shipping_time_default import InlineResponse2001ShippingRatesConstraintsShippingTimeDefault
from allegro_api.models.inline_response200_shipping_rates import InlineResponse200ShippingRates
from allegro_api.models.integer_category_parameter import IntegerCategoryParameter
from allegro_api.models.integer_category_product_parameter import IntegerCategoryProductParameter
from allegro_api.models.integer_category_product_parameter_all_of import IntegerCategoryProductParameterAllOf
from allegro_api.models.integer_category_product_parameter_all_of_restrictions import IntegerCategoryProductParameterAllOfRestrictions
from allegro_api.models.just_id import JustId
from allegro_api.models.latest_order_event import LatestOrderEvent
from allegro_api.models.line_item_id_mappings import LineItemIdMappings
from allegro_api.models.line_item_id_mappings_mappings import LineItemIdMappingsMappings
from allegro_api.models.listing_category import ListingCategory
from allegro_api.models.listing_category_with_count import ListingCategoryWithCount
from allegro_api.models.listing_offer import ListingOffer
from allegro_api.models.listing_response import ListingResponse
from allegro_api.models.listing_response_categories import ListingResponseCategories
from allegro_api.models.listing_response_filters import ListingResponseFilters
from allegro_api.models.listing_response_filters_values import ListingResponseFiltersValues
from allegro_api.models.listing_response_offers import ListingResponseOffers
from allegro_api.models.listing_response_search_meta import ListingResponseSearchMeta
from allegro_api.models.listing_response_sort import ListingResponseSort
from allegro_api.models.location import Location
from allegro_api.models.max_price import MaxPrice
from allegro_api.models.me_response import MeResponse
from allegro_api.models.message_author_role import MessageAuthorRole
from allegro_api.models.message_request import MessageRequest
from allegro_api.models.minimal_price import MinimalPrice
from allegro_api.models.modification import Modification
from allegro_api.models.modification_delivery import ModificationDelivery
from allegro_api.models.modification_payments import ModificationPayments
from allegro_api.models.modification_promotion import ModificationPromotion
from allegro_api.models.modification_publication import ModificationPublication
from allegro_api.models.modification_size_table import ModificationSizeTable
from allegro_api.models.multi_pack_benefit_specification import MultiPackBenefitSpecification
from allegro_api.models.multi_pack_benefit_specification_all_of import MultiPackBenefitSpecificationAllOf
from allegro_api.models.multi_pack_benefit_specification_all_of_configuration import MultiPackBenefitSpecificationAllOfConfiguration
from allegro_api.models.multi_pack_benefit_specification_all_of_trigger import MultiPackBenefitSpecificationAllOfTrigger
from allegro_api.models.my_bid_response import MyBidResponse
from allegro_api.models.offer import Offer
from allegro_api.models.offer_activated_event import OfferActivatedEvent
from allegro_api.models.offer_activated_event_all_of import OfferActivatedEventAllOf
from allegro_api.models.offer_additional_services import OfferAdditionalServices
from allegro_api.models.offer_archived_event import OfferArchivedEvent
from allegro_api.models.offer_archived_event_all_of import OfferArchivedEventAllOf
from allegro_api.models.offer_attachment import OfferAttachment
from allegro_api.models.offer_attachment_request import OfferAttachmentRequest
from allegro_api.models.offer_badge_campaign import OfferBadgeCampaign
from allegro_api.models.offer_bid_canceled_event import OfferBidCanceledEvent
from allegro_api.models.offer_bid_canceled_event_all_of import OfferBidCanceledEventAllOf
from allegro_api.models.offer_bid_placed_event import OfferBidPlacedEvent
from allegro_api.models.offer_bid_placed_event_all_of import OfferBidPlacedEventAllOf
from allegro_api.models.offer_category import OfferCategory
from allegro_api.models.offer_change_command import OfferChangeCommand
from allegro_api.models.offer_changed_event import OfferChangedEvent
from allegro_api.models.offer_changed_event_all_of import OfferChangedEventAllOf
from allegro_api.models.offer_criterium import OfferCriterium
from allegro_api.models.offer_delivery import OfferDelivery
from allegro_api.models.offer_ended_event import OfferEndedEvent
from allegro_api.models.offer_ended_event_all_of import OfferEndedEventAllOf
from allegro_api.models.offer_event_base_offer import OfferEventBaseOffer
from allegro_api.models.offer_event_ended_offer import OfferEventEndedOffer
from allegro_api.models.offer_event_ended_offer_all_of import OfferEventEndedOfferAllOf
from allegro_api.models.offer_event_ended_offer_all_of_publication import OfferEventEndedOfferAllOfPublication
from allegro_api.models.offer_fixed_price import OfferFixedPrice
from allegro_api.models.offer_id import OfferId
from allegro_api.models.offer_image_link_upload_request import OfferImageLinkUploadRequest
from allegro_api.models.offer_image_upload_response import OfferImageUploadResponse
from allegro_api.models.offer_images import OfferImages
from allegro_api.models.offer_listing_dto import OfferListingDto
from allegro_api.models.offer_listing_dto_image import OfferListingDtoImage
from allegro_api.models.offer_listing_dto_v1_delivery import OfferListingDtoV1Delivery
from allegro_api.models.offer_listing_dto_v1_publication import OfferListingDtoV1Publication
from allegro_api.models.offer_listing_dto_v1_sale_info import OfferListingDtoV1SaleInfo
from allegro_api.models.offer_listing_dto_v1_stats import OfferListingDtoV1Stats
from allegro_api.models.offer_listing_dto_v1_stock import OfferListingDtoV1Stock
from allegro_api.models.offer_lowest_price import OfferLowestPrice
from allegro_api.models.offer_price import OfferPrice
from allegro_api.models.offer_price_change_command import OfferPriceChangeCommand
from allegro_api.models.offer_price_changed_event import OfferPriceChangedEvent
from allegro_api.models.offer_price_changed_event_all_of import OfferPriceChangedEventAllOf
from allegro_api.models.offer_promotion import OfferPromotion
from allegro_api.models.offer_publication import OfferPublication
from allegro_api.models.offer_quantity_change_command import OfferQuantityChangeCommand
from allegro_api.models.offer_quote_dto import OfferQuoteDto
from allegro_api.models.offer_quotes_dto import OfferQuotesDto
from allegro_api.models.offer_rating import OfferRating
from allegro_api.models.offer_rating_score_distribution import OfferRatingScoreDistribution
from allegro_api.models.offer_rating_size_feedback import OfferRatingSizeFeedback
from allegro_api.models.offer_reference import OfferReference
from allegro_api.models.offer_requirements import OfferRequirements
from allegro_api.models.offer_seller import OfferSeller
from allegro_api.models.offer_selling_mode import OfferSellingMode
from allegro_api.models.offer_shipping_rates import OfferShippingRates
from allegro_api.models.offer_status import OfferStatus
from allegro_api.models.offer_stock import OfferStock
from allegro_api.models.offer_stock_changed_event import OfferStockChangedEvent
from allegro_api.models.offer_stock_changed_event_all_of import OfferStockChangedEventAllOf
from allegro_api.models.offer_vendor import OfferVendor
from allegro_api.models.offers_search_result_dto import OffersSearchResultDto
from allegro_api.models.open_hour import OpenHour
from allegro_api.models.operation_participant_address import OperationParticipantAddress
from allegro_api.models.operation_payment import OperationPayment
from allegro_api.models.operation_value import OperationValue
from allegro_api.models.order import Order
from allegro_api.models.order_event import OrderEvent
from allegro_api.models.order_event_data import OrderEventData
from allegro_api.models.order_event_stats import OrderEventStats
from allegro_api.models.order_event_type import OrderEventType
from allegro_api.models.order_events_list import OrderEventsList
from allegro_api.models.order_line_item import OrderLineItem
from allegro_api.models.parameter import Parameter
from allegro_api.models.parameter_range_value import ParameterRangeValue
from allegro_api.models.parameters_for_preview_price import ParametersForPreviewPrice
from allegro_api.models.participant import Participant
from allegro_api.models.payment import Payment
from allegro_api.models.payment_id_mapping import PaymentIdMapping
from allegro_api.models.payment_operations import PaymentOperations
from allegro_api.models.payments import Payments
from allegro_api.models.payments_surcharge import PaymentsSurcharge
from allegro_api.models.payout import Payout
from allegro_api.models.payout_operation import PayoutOperation
from allegro_api.models.payout_operation_all_of import PayoutOperationAllOf
from allegro_api.models.payout_operation_cancel import PayoutOperationCancel
from allegro_api.models.payout_operation_cancel_all_of import PayoutOperationCancelAllOf
from allegro_api.models.phones_request import PhonesRequest
from allegro_api.models.phones_response import PhonesResponse
from allegro_api.models.pos import Pos
from allegro_api.models.price import Price
from allegro_api.models.price_modification import PriceModification
from allegro_api.models.price_modification_fixed_price import PriceModificationFixedPrice
from allegro_api.models.price_modification_fixed_price_all_of import PriceModificationFixedPriceAllOf
from allegro_api.models.price_modification_fixed_price_holder import PriceModificationFixedPriceHolder
from allegro_api.models.price_modification_percentage_change_decrease import PriceModificationPercentageChangeDecrease
from allegro_api.models.price_modification_percentage_change_decrease_all_of import PriceModificationPercentageChangeDecreaseAllOf
from allegro_api.models.price_modification_percentage_change_increase import PriceModificationPercentageChangeIncrease
from allegro_api.models.price_modification_percentage_change_increase_all_of import PriceModificationPercentageChangeIncreaseAllOf
from allegro_api.models.price_modification_value_change_decrease import PriceModificationValueChangeDecrease
from allegro_api.models.price_modification_value_change_decrease_all_of import PriceModificationValueChangeDecreaseAllOf
from allegro_api.models.price_modification_value_change_holder import PriceModificationValueChangeHolder
from allegro_api.models.price_modification_value_change_increase import PriceModificationValueChangeIncrease
from allegro_api.models.price_modification_value_change_increase_all_of import PriceModificationValueChangeIncreaseAllOf
from allegro_api.models.processing_status import ProcessingStatus
from allegro_api.models.product_parameter import ProductParameter
from allegro_api.models.product_parameter_options import ProductParameterOptions
from allegro_api.models.products_category_path import ProductsCategoryPath
from allegro_api.models.products_category_subcategories import ProductsCategorySubcategories
from allegro_api.models.promotion import Promotion
from allegro_api.models.promotion_campaign_request_dto import PromotionCampaignRequestDto
from allegro_api.models.promotion_campaign_response_dto import PromotionCampaignResponseDto
from allegro_api.models.promotion_campaigns_response_dto import PromotionCampaignsResponseDto
from allegro_api.models.promotion_request_dto import PromotionRequestDto
from allegro_api.models.promotion_response_dto import PromotionResponseDto
from allegro_api.models.propose_sale_product_request import ProposeSaleProductRequest
from allegro_api.models.public_offer_preview_request import PublicOfferPreviewRequest
from allegro_api.models.public_table_dto import PublicTableDto
from allegro_api.models.public_table_image_dto import PublicTableImageDto
from allegro_api.models.public_tables_dto import PublicTablesDto
from allegro_api.models.publication import Publication
from allegro_api.models.publication_change_command_dto import PublicationChangeCommandDto
from allegro_api.models.publication_modification import PublicationModification
from allegro_api.models.publication_time_policy import PublicationTimePolicy
from allegro_api.models.quantity_modification import QuantityModification
from allegro_api.models.quote_response import QuoteResponse
from allegro_api.models.rates import Rates
from allegro_api.models.reference import Reference
from allegro_api.models.refund_additional_services_value import RefundAdditionalServicesValue
from allegro_api.models.refund_cancel_operation import RefundCancelOperation
from allegro_api.models.refund_cancel_operation_all_of import RefundCancelOperationAllOf
from allegro_api.models.refund_charge_operation import RefundChargeOperation
from allegro_api.models.refund_charge_operation_all_of import RefundChargeOperationAllOf
from allegro_api.models.refund_delivery_value import RefundDeliveryValue
from allegro_api.models.refund_details import RefundDetails
from allegro_api.models.refund_increase_operation import RefundIncreaseOperation
from allegro_api.models.refund_increase_operation_all_of import RefundIncreaseOperationAllOf
from allegro_api.models.refund_line_item import RefundLineItem
from allegro_api.models.refund_line_item_value import RefundLineItemValue
from allegro_api.models.refund_overpaid_value import RefundOverpaidValue
from allegro_api.models.refund_payment import RefundPayment
from allegro_api.models.refund_surcharge_value import RefundSurchargeValue
from allegro_api.models.refund_total_value import RefundTotalValue
from allegro_api.models.refusal_message import RefusalMessage
from allegro_api.models.removal import Removal
from allegro_api.models.removal_request import RemovalRequest
from allegro_api.models.return_policies_list_return_policy_basic import ReturnPoliciesListReturnPolicyBasic
from allegro_api.models.return_policy import ReturnPolicy
from allegro_api.models.return_policy_basic import ReturnPolicyBasic
from allegro_api.models.sale_product_compatibility_list import SaleProductCompatibilityList
from allegro_api.models.sale_product_dto import SaleProductDto
from allegro_api.models.sale_product_response_categories_dto import SaleProductResponseCategoriesDto
from allegro_api.models.sale_product_response_dto import SaleProductResponseDto
from allegro_api.models.search_result import SearchResult
from allegro_api.models.seller import Seller
from allegro_api.models.seller_create_rebate_request_dto import SellerCreateRebateRequestDto
from allegro_api.models.seller_offer_base_event import SellerOfferBaseEvent
from allegro_api.models.seller_offer_events_response import SellerOfferEventsResponse
from allegro_api.models.seller_participant import SellerParticipant
from allegro_api.models.seller_participant_all_of import SellerParticipantAllOf
from allegro_api.models.seller_rebate_dto import SellerRebateDto
from allegro_api.models.seller_rebate_offer_criterion import SellerRebateOfferCriterion
from allegro_api.models.seller_rebate_offer_criterion_offers import SellerRebateOfferCriterionOffers
from allegro_api.models.seller_rebates_dto import SellerRebatesDto
from allegro_api.models.seller_reference import SellerReference
from allegro_api.models.selling_mode import SellingMode
from allegro_api.models.selling_mode_format import SellingModeFormat
from allegro_api.models.shipping_rate import ShippingRate
from allegro_api.models.shipping_rate_delivery_method import ShippingRateDeliveryMethod
from allegro_api.models.shipping_rate_first_item_rate import ShippingRateFirstItemRate
from allegro_api.models.shipping_rate_next_item_rate import ShippingRateNextItemRate
from allegro_api.models.shipping_rate_shipping_time import ShippingRateShippingTime
from allegro_api.models.shipping_rates import ShippingRates
from allegro_api.models.shipping_rates_set import ShippingRatesSet
from allegro_api.models.single_promotion_campaign_response_dto import SinglePromotionCampaignResponseDto
from allegro_api.models.standardized_description import StandardizedDescription
from allegro_api.models.starting_price import StartingPrice
from allegro_api.models.stock import Stock
from allegro_api.models.string_category_parameter import StringCategoryParameter
from allegro_api.models.string_category_product_parameter import StringCategoryProductParameter
from allegro_api.models.string_category_product_parameter_all_of import StringCategoryProductParameterAllOf
from allegro_api.models.string_category_product_parameter_all_of_restrictions import StringCategoryProductParameterAllOfRestrictions
from allegro_api.models.subject import Subject
from allegro_api.models.surcharge import Surcharge
from allegro_api.models.surcharge_operation import SurchargeOperation
from allegro_api.models.surcharge_operation_all_of import SurchargeOperationAllOf
from allegro_api.models.tag_id import TagId
from allegro_api.models.tag_ids_request import TagIdsRequest
from allegro_api.models.tag_list_response import TagListResponse
from allegro_api.models.tag_request import TagRequest
from allegro_api.models.tag_response import TagResponse
from allegro_api.models.task_count import TaskCount
from allegro_api.models.task_report import TaskReport
from allegro_api.models.tecdoc_specification import TecdocSpecification
from allegro_api.models.tecdoc_specification_item import TecdocSpecificationItem
from allegro_api.models.user import User
from allegro_api.models.user_campaign_eligibility import UserCampaignEligibility
from allegro_api.models.user_rating import UserRating
from allegro_api.models.user_rating_answer_request import UserRatingAnswerRequest
from allegro_api.models.user_rating_list_response import UserRatingListResponse
from allegro_api.models.user_rating_removal_request import UserRatingRemovalRequest
from allegro_api.models.user_rating_removal_request_request import UserRatingRemovalRequestRequest
from allegro_api.models.user_rating_summary_response import UserRatingSummaryResponse
from allegro_api.models.user_rating_summary_response_not_recommended import UserRatingSummaryResponseNotRecommended
from allegro_api.models.user_rating_summary_response_recommended import UserRatingSummaryResponseRecommended
from allegro_api.models.validation import Validation
from allegro_api.models.validation_error import ValidationError
from allegro_api.models.variant_set import VariantSet
from allegro_api.models.variant_set_offer import VariantSetOffer
from allegro_api.models.variant_set_parameter import VariantSetParameter
from allegro_api.models.variant_sets import VariantSets
from allegro_api.models.variant_sets_variant_set import VariantSetsVariantSet
from allegro_api.models.visibility_time_policy import VisibilityTimePolicy
from allegro_api.models.wallet import Wallet
from allegro_api.models.wallet_balance import WalletBalance
from allegro_api.models.warranties_list_warranty_basic import WarrantiesListWarrantyBasic
from allegro_api.models.warranty import Warranty
from allegro_api.models.warranty_basic import WarrantyBasic
from allegro_api.models.wrapper_type_for_preview_conditions import WrapperTypeForPreviewConditions
from allegro_api.models.wraps_listing_and_commissions_fees import WrapsListingAndCommissionsFees
