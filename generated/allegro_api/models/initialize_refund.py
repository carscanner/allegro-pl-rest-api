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


class InitializeRefund(object):
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
        'payment': 'RefundPayment',
        'reason': 'str',
        'line_items': 'list[RefundLineItem]',
        'delivery': 'InitializeRefundDelivery',
        'overpaid': 'InitializeRefundOverpaid',
        'surcharges': 'list[PaymentsSurcharge]',
        'additional_services': 'InitializeRefundAdditionalServices'
    }

    attribute_map = {
        'payment': 'payment',
        'reason': 'reason',
        'line_items': 'lineItems',
        'delivery': 'delivery',
        'overpaid': 'overpaid',
        'surcharges': 'surcharges',
        'additional_services': 'additionalServices'
    }

    def __init__(self, payment=None, reason=None, line_items=None, delivery=None, overpaid=None, surcharges=None, additional_services=None, local_vars_configuration=None):  # noqa: E501
        """InitializeRefund - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payment = None
        self._reason = None
        self._line_items = None
        self._delivery = None
        self._overpaid = None
        self._surcharges = None
        self._additional_services = None
        self.discriminator = None

        self.payment = payment
        self.reason = reason
        if line_items is not None:
            self.line_items = line_items
        if delivery is not None:
            self.delivery = delivery
        if overpaid is not None:
            self.overpaid = overpaid
        if surcharges is not None:
            self.surcharges = surcharges
        if additional_services is not None:
            self.additional_services = additional_services

    @property
    def payment(self):
        """Gets the payment of this InitializeRefund.  # noqa: E501


        :return: The payment of this InitializeRefund.  # noqa: E501
        :rtype: RefundPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this InitializeRefund.


        :param payment: The payment of this InitializeRefund.  # noqa: E501
        :type: RefundPayment
        """
        if self.local_vars_configuration.client_side_validation and payment is None:  # noqa: E501
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

    @property
    def reason(self):
        """Gets the reason of this InitializeRefund.  # noqa: E501

        Reason for a payment refund.  # noqa: E501

        :return: The reason of this InitializeRefund.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this InitializeRefund.

        Reason for a payment refund.  # noqa: E501

        :param reason: The reason of this InitializeRefund.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reason is None:  # noqa: E501
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501
        allowed_values = ["REFUND", "COMPLAINT", "PRODUCT_NOT_AVAILABLE", "PAID_VALUE_TOO_LOW"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def line_items(self):
        """Gets the line_items of this InitializeRefund.  # noqa: E501

        List of order's line items which can be refunded.  # noqa: E501

        :return: The line_items of this InitializeRefund.  # noqa: E501
        :rtype: list[RefundLineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this InitializeRefund.

        List of order's line items which can be refunded.  # noqa: E501

        :param line_items: The line_items of this InitializeRefund.  # noqa: E501
        :type: list[RefundLineItem]
        """

        self._line_items = line_items

    @property
    def delivery(self):
        """Gets the delivery of this InitializeRefund.  # noqa: E501


        :return: The delivery of this InitializeRefund.  # noqa: E501
        :rtype: InitializeRefundDelivery
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this InitializeRefund.


        :param delivery: The delivery of this InitializeRefund.  # noqa: E501
        :type: InitializeRefundDelivery
        """

        self._delivery = delivery

    @property
    def overpaid(self):
        """Gets the overpaid of this InitializeRefund.  # noqa: E501


        :return: The overpaid of this InitializeRefund.  # noqa: E501
        :rtype: InitializeRefundOverpaid
        """
        return self._overpaid

    @overpaid.setter
    def overpaid(self, overpaid):
        """Sets the overpaid of this InitializeRefund.


        :param overpaid: The overpaid of this InitializeRefund.  # noqa: E501
        :type: InitializeRefundOverpaid
        """

        self._overpaid = overpaid

    @property
    def surcharges(self):
        """Gets the surcharges of this InitializeRefund.  # noqa: E501

        List of surcharges for payment which can be refunded.  # noqa: E501

        :return: The surcharges of this InitializeRefund.  # noqa: E501
        :rtype: list[PaymentsSurcharge]
        """
        return self._surcharges

    @surcharges.setter
    def surcharges(self, surcharges):
        """Sets the surcharges of this InitializeRefund.

        List of surcharges for payment which can be refunded.  # noqa: E501

        :param surcharges: The surcharges of this InitializeRefund.  # noqa: E501
        :type: list[PaymentsSurcharge]
        """

        self._surcharges = surcharges

    @property
    def additional_services(self):
        """Gets the additional_services of this InitializeRefund.  # noqa: E501


        :return: The additional_services of this InitializeRefund.  # noqa: E501
        :rtype: InitializeRefundAdditionalServices
        """
        return self._additional_services

    @additional_services.setter
    def additional_services(self, additional_services):
        """Sets the additional_services of this InitializeRefund.


        :param additional_services: The additional_services of this InitializeRefund.  # noqa: E501
        :type: InitializeRefundAdditionalServices
        """

        self._additional_services = additional_services

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
        if not isinstance(other, InitializeRefund):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InitializeRefund):
            return True

        return self.to_dict() != other.to_dict()
