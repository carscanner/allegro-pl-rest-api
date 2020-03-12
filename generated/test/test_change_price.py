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
from allegro_api.models.change_price import ChangePrice  # noqa: E501
from allegro_api.rest import ApiException

class TestChangePrice(unittest.TestCase):
    """ChangePrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ChangePrice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.change_price.ChangePrice()  # noqa: E501
        if include_optional :
            return ChangePrice(
                id = '6365996a-6cae-11e9-a923-1681be663d3e', 
                input = allegro_api.models.change_price_input.ChangePriceInput(
                    buy_now_price = allegro_api.models.price.Price(
                        amount = '123.45', 
                        currency = 'PLN', ), ), 
                output = allegro_api.models.command_output.CommandOutput(
                    status = 'QUEUEING', 
                    errors = [
                        allegro_api.models.error.Error(
                            code = 'NotAcceptableException', 
                            details = '0', 
                            message = 'Not acceptable representation requested. Please check 'Accept' request header', 
                            path = '0', 
                            user_message = 'The request contains incorrect data. Contact the author of the application.', )
                        ], )
            )
        else :
            return ChangePrice(
                input = allegro_api.models.change_price_input.ChangePriceInput(
                    buy_now_price = allegro_api.models.price.Price(
                        amount = '123.45', 
                        currency = 'PLN', ), ),
        )

    def testChangePrice(self):
        """Test ChangePrice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
