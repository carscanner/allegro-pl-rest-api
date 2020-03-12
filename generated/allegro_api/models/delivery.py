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


class Delivery(object):
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
        'additional_info': 'str',
        'handling_time': 'str',
        'shipment_date': 'datetime',
        'shipping_rates': 'JustId'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'handling_time': 'handlingTime',
        'shipment_date': 'shipmentDate',
        'shipping_rates': 'shippingRates'
    }

    def __init__(self, additional_info=None, handling_time=None, shipment_date=None, shipping_rates=None, local_vars_configuration=None):  # noqa: E501
        """Delivery - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_info = None
        self._handling_time = None
        self._shipment_date = None
        self._shipping_rates = None
        self.discriminator = None

        if additional_info is not None:
            self.additional_info = additional_info
        if handling_time is not None:
            self.handling_time = handling_time
        if shipment_date is not None:
            self.shipment_date = shipment_date
        if shipping_rates is not None:
            self.shipping_rates = shipping_rates

    @property
    def additional_info(self):
        """Gets the additional_info of this Delivery.  # noqa: E501


        :return: The additional_info of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Delivery.


        :param additional_info: The additional_info of this Delivery.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                additional_info is not None and len(additional_info) > 650):
            raise ValueError("Invalid value for `additional_info`, length must be less than or equal to `650`")  # noqa: E501

        self._additional_info = additional_info

    @property
    def handling_time(self):
        """Gets the handling_time of this Delivery.  # noqa: E501

        Handling time, ISO 8601 duration format  # noqa: E501

        :return: The handling_time of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._handling_time

    @handling_time.setter
    def handling_time(self, handling_time):
        """Sets the handling_time of this Delivery.

        Handling time, ISO 8601 duration format  # noqa: E501

        :param handling_time: The handling_time of this Delivery.  # noqa: E501
        :type: str
        """

        self._handling_time = handling_time

    @property
    def shipment_date(self):
        """Gets the shipment_date of this Delivery.  # noqa: E501

        Shipment date, Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :return: The shipment_date of this Delivery.  # noqa: E501
        :rtype: datetime
        """
        return self._shipment_date

    @shipment_date.setter
    def shipment_date(self, shipment_date):
        """Sets the shipment_date of this Delivery.

        Shipment date, Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :param shipment_date: The shipment_date of this Delivery.  # noqa: E501
        :type: datetime
        """

        self._shipment_date = shipment_date

    @property
    def shipping_rates(self):
        """Gets the shipping_rates of this Delivery.  # noqa: E501


        :return: The shipping_rates of this Delivery.  # noqa: E501
        :rtype: JustId
        """
        return self._shipping_rates

    @shipping_rates.setter
    def shipping_rates(self, shipping_rates):
        """Sets the shipping_rates of this Delivery.


        :param shipping_rates: The shipping_rates of this Delivery.  # noqa: E501
        :type: JustId
        """

        self._shipping_rates = shipping_rates

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
        if not isinstance(other, Delivery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Delivery):
            return True

        return self.to_dict() != other.to_dict()
