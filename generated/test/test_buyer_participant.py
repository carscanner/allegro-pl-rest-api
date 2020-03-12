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
from allegro_api.models.buyer_participant import BuyerParticipant  # noqa: E501
from allegro_api.rest import ApiException

class TestBuyerParticipant(unittest.TestCase):
    """BuyerParticipant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BuyerParticipant
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.buyer_participant.BuyerParticipant()  # noqa: E501
        if include_optional :
            return BuyerParticipant(
                company_name = 'Allegro', 
                login = 'User_login', 
                first_name = 'Jan', 
                last_name = 'Nowak', 
                address = allegro_api.models.operation_participant_address.OperationParticipantAddress(
                    street = 'Grunwaldzka 108', 
                    city = 'Poznań', 
                    post_code = '60-166', ), 
                id = '0'
            )
        else :
            return BuyerParticipant(
                login = 'User_login',
                first_name = 'Jan',
                last_name = 'Nowak',
                id = '0',
        )

    def testBuyerParticipant(self):
        """Test BuyerParticipant"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
