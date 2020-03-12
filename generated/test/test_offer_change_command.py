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
from allegro_api.models.offer_change_command import OfferChangeCommand  # noqa: E501
from allegro_api.rest import ApiException

class TestOfferChangeCommand(unittest.TestCase):
    """OfferChangeCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OfferChangeCommand
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.offer_change_command.OfferChangeCommand()  # noqa: E501
        if include_optional :
            return OfferChangeCommand(
                modification = allegro_api.models.modification.Modification(
                    additional_services_group = allegro_api.models.additional_services_group.AdditionalServicesGroup(
                        id = '0', ), 
                    delivery = allegro_api.models.modification_delivery.ModificationDelivery(
                        shipping_rates = allegro_api.models.shipping_rates.ShippingRates(
                            id = '0', ), ), 
                    payments = allegro_api.models.modification_payments.ModificationPayments(
                        invoice = 'VAT', ), 
                    promotion = allegro_api.models.modification_promotion.ModificationPromotion(
                        bold = False, 
                        department_page = False, 
                        emphasized = False, 
                        emphasized_highlight_bold_package = False, 
                        highlight = False, ), 
                    size_table = allegro_api.models.modification_size_table.ModificationSizeTable(
                        id = '0', ), 
                    publication = allegro_api.models.modification_publication.ModificationPublication(
                        duration = 'PT72H', 
                        duration_unlimited = False, ), ), 
                offer_criteria = [
                    allegro_api.models.offer_criterium.OfferCriterium(
                        offers = [
                            allegro_api.models.offer_id.OfferId(
                                id = '0', )
                            ], 
                        type = 'CONTAINS_OFFERS', )
                    ]
            )
        else :
            return OfferChangeCommand(
        )

    def testOfferChangeCommand(self):
        """Test OfferChangeCommand"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()