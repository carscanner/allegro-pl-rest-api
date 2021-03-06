# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import allegro_api
from allegro_api.models.public_offer_preview_request import PublicOfferPreviewRequest  # noqa: E501
from allegro_api.rest import ApiException

class TestPublicOfferPreviewRequest(unittest.TestCase):
    """PublicOfferPreviewRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PublicOfferPreviewRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.public_offer_preview_request.PublicOfferPreviewRequest()  # noqa: E501
        if include_optional :
            return PublicOfferPreviewRequest(
                offer = allegro_api.models.offer.Offer(
                    additional_services = allegro_api.models.just_id.JustId(
                        id = '0', ), 
                    after_sales_services = allegro_api.models.after_sales_services.AfterSalesServices(
                        implied_warranty = allegro_api.models.implied_warranty.ImpliedWarranty(
                            id = '09f0b4cc-7880-11e9-8f9e-2a86e4085a59', ), 
                        return_policy = allegro_api.models.return_policy.ReturnPolicy(
                            id = '09f0b4cc-7880-11e9-8f9e-2a86e4085a59', ), 
                        warranty = allegro_api.models.warranty.Warranty(
                            id = '09f0b4cc-7880-11e9-8f9e-2a86e4085a59', ), ), 
                    attachments = [
                        allegro_api.models.attachment.Attachment(
                            id = '1928302_MANUAL_45d7a0f543e1b0d05e12a1aef5642efe63389a1d419fe9286d0f158044391fdce', )
                        ], 
                    category = allegro_api.models.category.Category(
                        id = '0', ), 
                    compatibility_list = allegro_api.models.compatibility_list.CompatibilityList(), 
                    contact = allegro_api.models.just_id.JustId(
                        id = '0', ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    delivery = allegro_api.models.delivery.Delivery(
                        additional_info = '0', 
                        handling_time = 'PDT12H30M5S', 
                        shipment_date = '2018-04-01T08:00Z', 
                        shipping_rates = allegro_api.models.just_id.JustId(
                            id = '0', ), ), 
                    description = allegro_api.models.standardized_description.StandardizedDescription(
                        sections = [
                            allegro_api.models.description_section.DescriptionSection(
                                items = [
                                    allegro_api.models.description_section_item.DescriptionSectionItem(
                                        type = '0', )
                                    ], )
                            ], ), 
                    ean = '0', 
                    external = allegro_api.models.external_id.ExternalId(
                        id = 'AH-129834', ), 
                    id = '0', 
                    images = [
                        allegro_api.models.image_url.ImageUrl(
                            url = '0', )
                        ], 
                    location = allegro_api.models.location.Location(
                        city = '0', 
                        country_code = '0', 
                        post_code = '0', 
                        province = '0', ), 
                    name = '0', 
                    parameters = [
                        allegro_api.models.parameter.Parameter(
                            id = '0', 
                            range_value = allegro_api.models.parameter_range_value.ParameterRangeValue(
                                from = '0', 
                                to = '0', ), 
                            values = [
                                '0'
                                ], 
                            values_ids = [
                                '0'
                                ], )
                        ], 
                    payments = allegro_api.models.payments.Payments(
                        invoice = '0', ), 
                    product = allegro_api.models.just_id.JustId(
                        id = '0', ), 
                    promotion = allegro_api.models.promotion.Promotion(
                        bold = True, 
                        department_page = True, 
                        emphasized = True, 
                        emphasized_highlight_bold_package = True, 
                        highlight = True, ), 
                    publication = allegro_api.models.publication.Publication(
                        duration = 'PDT12H30M5S', 
                        ending_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        starting_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = 'INACTIVE', 
                        ended_by = 'USER', 
                        republish = False, ), 
                    selling_mode = allegro_api.models.selling_mode.SellingMode(
                        format = 'BUY_NOW', 
                        price = null, 
                        minimal_price = null, 
                        starting_price = null, ), 
                    size_table = allegro_api.models.just_id.JustId(
                        id = '0', ), 
                    stock = allegro_api.models.stock.Stock(
                        available = 56, 
                        unit = '0', ), 
                    tecdoc_specification = allegro_api.models.tecdoc_specification.TecdocSpecification(
                        id = '470b8513-b786-b7b9-9e7e-2f848729cfd6', ), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    validation = allegro_api.models.validation.Validation(
                        errors = [
                            allegro_api.models.validation_error.ValidationError(
                                code = '0', 
                                details = '0', 
                                message = '0', 
                                path = '0', 
                                user_message = '0', )
                            ], 
                        validated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), ), 
                classifieds_packages = allegro_api.models.classifieds_packages.ClassifiedsPackages(
                    base_package = allegro_api.models.classified_package.ClassifiedPackage(
                        id = 'e76d443b-c088-4da5-95f7-cc9aaf73bf7b', ), 
                    extra_packages = [
                        allegro_api.models.classified_package.ClassifiedPackage(
                            id = 'e76d443b-c088-4da5-95f7-cc9aaf73bf7b', )
                        ], )
            )
        else :
            return PublicOfferPreviewRequest(
        )

    def testPublicOfferPreviewRequest(self):
        """Test PublicOfferPreviewRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
