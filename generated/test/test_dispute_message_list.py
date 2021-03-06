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
from allegro_api.models.dispute_message_list import DisputeMessageList  # noqa: E501
from allegro_api.rest import ApiException

class TestDisputeMessageList(unittest.TestCase):
    """DisputeMessageList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DisputeMessageList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = allegro_api.models.dispute_message_list.DisputeMessageList()  # noqa: E501
        if include_optional :
            return DisputeMessageList(
                messages = [
                    allegro_api.models.dispute_message.DisputeMessage(
                        id = '0', 
                        text = '0', 
                        attachment = allegro_api.models.dispute_attachment.DisputeAttachment(
                            file_name = '0', 
                            url = 'https://upload.allegro.pl/sale/dispute-attachments/eeed0007-4404-4176-a1eb-11d26f056c0d', ), 
                        author = allegro_api.models.dispute_message_author.DisputeMessageAuthor(
                            login = '0', 
                            role = 'BUYER', ), 
                        created_at = '2018-02-10T12:12:12Z', )
                    ]
            )
        else :
            return DisputeMessageList(
        )

    def testDisputeMessageList(self):
        """Test DisputeMessageList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
