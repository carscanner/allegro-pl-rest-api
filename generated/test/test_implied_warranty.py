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
from allegro_api.models.implied_warranty import ImpliedWarranty  # noqa: E501
from allegro_api.rest import ApiException

class TestImpliedWarranty(unittest.TestCase):
    """ImpliedWarranty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImpliedWarranty
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.implied_warranty.ImpliedWarranty()  # noqa: E501
        if include_optional :
            return ImpliedWarranty(
                id = '09f0b4cc-7880-11e9-8f9e-2a86e4085a59'
            )
        else :
            return ImpliedWarranty(
        )

    def testImpliedWarranty(self):
        """Test ImpliedWarranty"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
