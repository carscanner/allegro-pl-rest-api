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
from allegro_api.models.user_rating_summary_response import UserRatingSummaryResponse  # noqa: E501
from allegro_api.rest import ApiException

class TestUserRatingSummaryResponse(unittest.TestCase):
    """UserRatingSummaryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserRatingSummaryResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.user_rating_summary_response.UserRatingSummaryResponse()  # noqa: E501
        if include_optional :
            return UserRatingSummaryResponse(
                average_rates = allegro_api.models.average_rates.AverageRates(
                    delivery = 4.7, 
                    delivery_cost = 5, 
                    description = 4.5, 
                    service = 4.8, ), 
                not_recommended = allegro_api.models.user_rating_summary_response_not_recommended.UserRatingSummaryResponse_notRecommended(
                    total = 100, 
                    unique = 80, ), 
                recommended = allegro_api.models.user_rating_summary_response_recommended.UserRatingSummaryResponse_recommended(
                    total = 100, 
                    unique = 75, ), 
                recommended_percentage = '99,8'
            )
        else :
            return UserRatingSummaryResponse(
                not_recommended = allegro_api.models.user_rating_summary_response_not_recommended.UserRatingSummaryResponse_notRecommended(
                    total = 100, 
                    unique = 80, ),
                recommended = allegro_api.models.user_rating_summary_response_recommended.UserRatingSummaryResponse_recommended(
                    total = 100, 
                    unique = 75, ),
                recommended_percentage = '99,8',
        )

    def testUserRatingSummaryResponse(self):
        """Test UserRatingSummaryResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
