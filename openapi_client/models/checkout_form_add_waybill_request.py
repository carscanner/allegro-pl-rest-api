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


class CheckoutFormAddWaybillRequest(object):
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
        'carrier_id': 'str',
        'waybill': 'str',
        'carrier_name': 'str',
        'line_items': 'list[object]'
    }

    attribute_map = {
        'carrier_id': 'carrierId',
        'waybill': 'waybill',
        'carrier_name': 'carrierName',
        'line_items': 'lineItems'
    }

    def __init__(self, carrier_id=None, waybill=None, carrier_name=None, line_items=None):  # noqa: E501
        """CheckoutFormAddWaybillRequest - a model defined in OpenAPI"""  # noqa: E501

        self._carrier_id = None
        self._waybill = None
        self._carrier_name = None
        self._line_items = None
        self.discriminator = None

        self.carrier_id = carrier_id
        self.waybill = waybill
        if carrier_name is not None:
            self.carrier_name = carrier_name
        self.line_items = line_items

    @property
    def carrier_id(self):
        """Gets the carrier_id of this CheckoutFormAddWaybillRequest.  # noqa: E501

        Carrier identifier taken from the dictionary below. It’s highly recommended to use an identifier different from OTHER, because its parcel status may be updated automatically. Carrier identifier OTHER is reserved for cases when seller uses a custom carrier or not yet integrated with Allegro.  # noqa: E501

        :return: The carrier_id of this CheckoutFormAddWaybillRequest.  # noqa: E501
        :rtype: str
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this CheckoutFormAddWaybillRequest.

        Carrier identifier taken from the dictionary below. It’s highly recommended to use an identifier different from OTHER, because its parcel status may be updated automatically. Carrier identifier OTHER is reserved for cases when seller uses a custom carrier or not yet integrated with Allegro.  # noqa: E501

        :param carrier_id: The carrier_id of this CheckoutFormAddWaybillRequest.  # noqa: E501
        :type: str
        """
        if carrier_id is None:
            raise ValueError("Invalid value for `carrier_id`, must not be `None`")  # noqa: E501
        allowed_values = ["UPS", "INPOST", "DHL", "GLS", "RUCH", "POCZTA_POLSKA", "DPD", "POCZTEX", "FEDEX", "TNT_EXPRESS", "DB_SCHENKER", "RABEN", "GEIS", "DTS", "PEKAES", "PATRON", "X_PRESS_COURIERS", "RHENUS_LOGISTICS", "OTHER"]  # noqa: E501
        if carrier_id not in allowed_values:
            raise ValueError(
                "Invalid value for `carrier_id` ({0}), must be one of {1}"  # noqa: E501
                .format(carrier_id, allowed_values)
            )

        self._carrier_id = carrier_id

    @property
    def waybill(self):
        """Gets the waybill of this CheckoutFormAddWaybillRequest.  # noqa: E501

        Waybill number (parcel tracking number). Cannot be empty and must be no longer than 64 characters. It can contain any word character (equal to [a-zA-Z0-9_]) and special characters: parentheses and hyphen-minus.  # noqa: E501

        :return: The waybill of this CheckoutFormAddWaybillRequest.  # noqa: E501
        :rtype: str
        """
        return self._waybill

    @waybill.setter
    def waybill(self, waybill):
        """Sets the waybill of this CheckoutFormAddWaybillRequest.

        Waybill number (parcel tracking number). Cannot be empty and must be no longer than 64 characters. It can contain any word character (equal to [a-zA-Z0-9_]) and special characters: parentheses and hyphen-minus.  # noqa: E501

        :param waybill: The waybill of this CheckoutFormAddWaybillRequest.  # noqa: E501
        :type: str
        """
        if waybill is None:
            raise ValueError("Invalid value for `waybill`, must not be `None`")  # noqa: E501
        if waybill is not None and len(waybill) > 64:
            raise ValueError("Invalid value for `waybill`, length must be less than or equal to `64`")  # noqa: E501

        self._waybill = waybill

    @property
    def carrier_name(self):
        """Gets the carrier_name of this CheckoutFormAddWaybillRequest.  # noqa: E501

        Carrier name to be provided only if carrierId is OTHER, otherwise it’s ignored. Must be no longer than 30 characters.  # noqa: E501

        :return: The carrier_name of this CheckoutFormAddWaybillRequest.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this CheckoutFormAddWaybillRequest.

        Carrier name to be provided only if carrierId is OTHER, otherwise it’s ignored. Must be no longer than 30 characters.  # noqa: E501

        :param carrier_name: The carrier_name of this CheckoutFormAddWaybillRequest.  # noqa: E501
        :type: str
        """
        if carrier_name is not None and len(carrier_name) > 30:
            raise ValueError("Invalid value for `carrier_name`, length must be less than or equal to `30`")  # noqa: E501

        self._carrier_name = carrier_name

    @property
    def line_items(self):
        """Gets the line_items of this CheckoutFormAddWaybillRequest.  # noqa: E501

        List of order line items. They must be from the order specified in the path parameter. List cannot be empty.  # noqa: E501

        :return: The line_items of this CheckoutFormAddWaybillRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this CheckoutFormAddWaybillRequest.

        List of order line items. They must be from the order specified in the path parameter. List cannot be empty.  # noqa: E501

        :param line_items: The line_items of this CheckoutFormAddWaybillRequest.  # noqa: E501
        :type: list[object]
        """
        if line_items is None:
            raise ValueError("Invalid value for `line_items`, must not be `None`")  # noqa: E501

        self._line_items = line_items

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
        if not isinstance(other, CheckoutFormAddWaybillRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
