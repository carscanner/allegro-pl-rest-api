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
from allegro_api.models.badges_list import BadgesList  # noqa: E501
from allegro_api.rest import ApiException

class TestBadgesList(unittest.TestCase):
    """BadgesList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BadgesList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.badges_list.BadgesList()  # noqa: E501
        if include_optional :
            return BadgesList(
                badges = [
                    allegro_api.models.badge.Badge(
                        offer = allegro_api.models.badge_offer.BadgeOffer(
                            id = '987654321', ), 
                        campaign = allegro_api.models.offer_badge_campaign.OfferBadgeCampaign(
                            id = 'BARGAIN', 
                            name = 'Strefa Okazji', ), 
                        publication = {"type":"UNTIL","to":"2012-12-03T10:15:30.000Z"}, 
                        prices = allegro_api.models.badge_prices.BadgePrices(
                            market = allegro_api.models.badge_application_market_price.BadgeApplicationMarketPrice(
                                amount = '1.23', 
                                currency = 'PLN', ), 
                            bargain = allegro_api.models.badge_application_bargain_price.BadgeApplicationBargainPrice(
                                amount = '1.23', 
                                currency = 'PLN', ), ), 
                        process = allegro_api.models.badge_process.BadgeProcess(
                            status = 'IN_VERIFICATION', 
                            rejection_reasons = [
                                allegro_api.models.rejection_reason.RejectionReason(
                                    code = '0', 
                                    messages = [
                                        allegro_api.models.badge_application_rejection_reason_message.BadgeApplicationRejectionReasonMessage(
                                            text = 'See requirements.', 
                                            link = 'https://allegro.pl/regulamin/pl', )
                                        ], )
                                ], ), )
                    ]
            )
        else :
            return BadgesList(
                badges = [
                    allegro_api.models.badge.Badge(
                        offer = allegro_api.models.badge_offer.BadgeOffer(
                            id = '987654321', ), 
                        campaign = allegro_api.models.offer_badge_campaign.OfferBadgeCampaign(
                            id = 'BARGAIN', 
                            name = 'Strefa Okazji', ), 
                        publication = {"type":"UNTIL","to":"2012-12-03T10:15:30.000Z"}, 
                        prices = allegro_api.models.badge_prices.BadgePrices(
                            market = allegro_api.models.badge_application_market_price.BadgeApplicationMarketPrice(
                                amount = '1.23', 
                                currency = 'PLN', ), 
                            bargain = allegro_api.models.badge_application_bargain_price.BadgeApplicationBargainPrice(
                                amount = '1.23', 
                                currency = 'PLN', ), ), 
                        process = allegro_api.models.badge_process.BadgeProcess(
                            status = 'IN_VERIFICATION', 
                            rejection_reasons = [
                                allegro_api.models.rejection_reason.RejectionReason(
                                    code = '0', 
                                    messages = [
                                        allegro_api.models.badge_application_rejection_reason_message.BadgeApplicationRejectionReasonMessage(
                                            text = 'See requirements.', 
                                            link = 'https://allegro.pl/regulamin/pl', )
                                        ], )
                                ], ), )
                    ],
        )

    def testBadgesList(self):
        """Test BadgesList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
