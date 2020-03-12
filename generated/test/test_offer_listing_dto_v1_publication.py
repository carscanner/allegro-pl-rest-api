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
from allegro_api.models.offer_listing_dto_v1_publication import OfferListingDtoV1Publication  # noqa: E501
from allegro_api.rest import ApiException

class TestOfferListingDtoV1Publication(unittest.TestCase):
    """OfferListingDtoV1Publication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OfferListingDtoV1Publication
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.offer_listing_dto_v1_publication.OfferListingDtoV1Publication()  # noqa: E501
        if include_optional :
            return OfferListingDtoV1Publication(
                status = 'INACTIVE', 
                starting_at = '2019-05-29T12:00:00Z', 
                started_at = '2019-05-29T12:00:00Z', 
                ending_at = '2019-06-30T12:00:00Z', 
                ended_at = '2019-06-30T12:10:00Z'
            )
        else :
            return OfferListingDtoV1Publication(
        )

    def testOfferListingDtoV1Publication(self):
        """Test OfferListingDtoV1Publication"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
