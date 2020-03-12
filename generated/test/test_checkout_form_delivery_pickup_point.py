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
from allegro_api.models.checkout_form_delivery_pickup_point import CheckoutFormDeliveryPickupPoint  # noqa: E501
from allegro_api.rest import ApiException

class TestCheckoutFormDeliveryPickupPoint(unittest.TestCase):
    """CheckoutFormDeliveryPickupPoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CheckoutFormDeliveryPickupPoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.checkout_form_delivery_pickup_point.CheckoutFormDeliveryPickupPoint()  # noqa: E501
        if include_optional :
            return CheckoutFormDeliveryPickupPoint(
                id = 'POZ08A', 
                name = 'Paczkomat POZ08A', 
                description = 'Stacja paliw BP', 
                address = allegro_api.models.checkout_form_delivery_pickup_point_address.CheckoutFormDeliveryPickupPointAddress(
                    street = 'Grunwaldzka 108', 
                    zip_code = '60-166', 
                    city = 'Poznań', )
            )
        else :
            return CheckoutFormDeliveryPickupPoint(
        )

    def testCheckoutFormDeliveryPickupPoint(self):
        """Test CheckoutFormDeliveryPickupPoint"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()