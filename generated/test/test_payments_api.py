# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import allegro_api
from allegro_api.api.payments_api import PaymentsApi  # noqa: E501
from allegro_api.rest import ApiException


class TestPaymentsApi(unittest.TestCase):
    """PaymentsApi unit test stubs"""

    def setUp(self):
        self.api = allegro_api.api.payments_api.PaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_payment_id_mapping(self):
        """Test case for get_payment_id_mapping

        Mapping of payment identifiers  # noqa: E501
        """
        pass

    def test_get_payments_operation_history(self):
        """Test case for get_payments_operation_history

        Payment operations history  # noqa: E501
        """
        pass

    def test_get_refunded_payments(self):
        """Test case for get_refunded_payments

        Get a list of refunded payments  # noqa: E501
        """
        pass

    def test_initiate_refund(self):
        """Test case for initiate_refund

        Initiate a refund of a payment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
