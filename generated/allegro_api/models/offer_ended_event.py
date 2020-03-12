# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from allegro_api.configuration import Configuration


class OfferEndedEvent(object):
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
        'type': 'str',
        'offer': 'OfferEventEndedOffer'
    }

    attribute_map = {
        'type': 'type',
        'offer': 'offer'
    }

    def __init__(self, type='OFFER_ENDED', offer=None, local_vars_configuration=None):  # noqa: E501
        """OfferEndedEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._offer = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.offer = offer

    @property
    def type(self):
        """Gets the type of this OfferEndedEvent.  # noqa: E501


        :return: The type of this OfferEndedEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OfferEndedEvent.


        :param type: The type of this OfferEndedEvent.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def offer(self):
        """Gets the offer of this OfferEndedEvent.  # noqa: E501


        :return: The offer of this OfferEndedEvent.  # noqa: E501
        :rtype: OfferEventEndedOffer
        """
        return self._offer

    @offer.setter
    def offer(self, offer):
        """Sets the offer of this OfferEndedEvent.


        :param offer: The offer of this OfferEndedEvent.  # noqa: E501
        :type: OfferEventEndedOffer
        """
        if self.local_vars_configuration.client_side_validation and offer is None:  # noqa: E501
            raise ValueError("Invalid value for `offer`, must not be `None`")  # noqa: E501

        self._offer = offer

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
        if not isinstance(other, OfferEndedEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OfferEndedEvent):
            return True

        return self.to_dict() != other.to_dict()
