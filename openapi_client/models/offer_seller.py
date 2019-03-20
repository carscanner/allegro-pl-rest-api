# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class OfferSeller(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'company': 'bool',
        'super_seller': 'bool',
        'contact': 'OfferSellerContact'
    }

    attribute_map = {
        'id': 'id',
        'company': 'company',
        'super_seller': 'superSeller',
        'contact': 'contact'
    }

    def __init__(self, id=None, company=None, super_seller=None, contact=None):  # noqa: E501
        """OfferSeller - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._company = None
        self._super_seller = None
        self._contact = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if company is not None:
            self.company = company
        if super_seller is not None:
            self.super_seller = super_seller
        if contact is not None:
            self.contact = contact

    @property
    def id(self):
        """Gets the id of this OfferSeller.  # noqa: E501

        Identifier of the seller.  # noqa: E501

        :return: The id of this OfferSeller.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OfferSeller.

        Identifier of the seller.  # noqa: E501

        :param id: The id of this OfferSeller.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def company(self):
        """Gets the company of this OfferSeller.  # noqa: E501

        Indicates whether the seller is a company.  # noqa: E501

        :return: The company of this OfferSeller.  # noqa: E501
        :rtype: bool
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this OfferSeller.

        Indicates whether the seller is a company.  # noqa: E501

        :param company: The company of this OfferSeller.  # noqa: E501
        :type: bool
        """

        self._company = company

    @property
    def super_seller(self):
        """Gets the super_seller of this OfferSeller.  # noqa: E501

        Indicates whether the item has Super Seller option.  # noqa: E501

        :return: The super_seller of this OfferSeller.  # noqa: E501
        :rtype: bool
        """
        return self._super_seller

    @super_seller.setter
    def super_seller(self, super_seller):
        """Sets the super_seller of this OfferSeller.

        Indicates whether the item has Super Seller option.  # noqa: E501

        :param super_seller: The super_seller of this OfferSeller.  # noqa: E501
        :type: bool
        """

        self._super_seller = super_seller

    @property
    def contact(self):
        """Gets the contact of this OfferSeller.  # noqa: E501


        :return: The contact of this OfferSeller.  # noqa: E501
        :rtype: OfferSellerContact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this OfferSeller.


        :param contact: The contact of this OfferSeller.  # noqa: E501
        :type: OfferSellerContact
        """

        self._contact = contact

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OfferSeller):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
