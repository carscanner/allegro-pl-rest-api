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


class ParametersForPreviewPrice(object):
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
        'category': 'Category',
        'condition': 'str',
        'duration': 'str',
        'has_any_quantity': 'bool',
        'number_of_big_photos': 'int',
        'number_of_photos': 'int',
        'quantity': 'int',
        'shop': 'bool',
        'sold_quantity': 'int',
        'type': 'str',
        'unit_price': 'float',
        'bold': 'bool',
        'highlight': 'bool',
        'department_page': 'bool',
        'emphasized': 'bool',
        'emphasized_highlight_bold_package': 'bool',
        'multi_variant': 'bool'
    }

    attribute_map = {
        'category': 'category',
        'condition': 'condition',
        'duration': 'duration',
        'has_any_quantity': 'hasAnyQuantity',
        'number_of_big_photos': 'numberOfBigPhotos',
        'number_of_photos': 'numberOfPhotos',
        'quantity': 'quantity',
        'shop': 'shop',
        'sold_quantity': 'soldQuantity',
        'type': 'type',
        'unit_price': 'unitPrice',
        'bold': 'bold',
        'highlight': 'highlight',
        'department_page': 'departmentPage',
        'emphasized': 'emphasized',
        'emphasized_highlight_bold_package': 'emphasizedHighlightBoldPackage',
        'multi_variant': 'multiVariant'
    }

    def __init__(self, category=None, condition=None, duration=None, has_any_quantity=None, number_of_big_photos=None, number_of_photos=None, quantity=None, shop=None, sold_quantity=None, type=None, unit_price=None, bold=None, highlight=None, department_page=None, emphasized=None, emphasized_highlight_bold_package=None, multi_variant=None, local_vars_configuration=None):  # noqa: E501
        """ParametersForPreviewPrice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._category = None
        self._condition = None
        self._duration = None
        self._has_any_quantity = None
        self._number_of_big_photos = None
        self._number_of_photos = None
        self._quantity = None
        self._shop = None
        self._sold_quantity = None
        self._type = None
        self._unit_price = None
        self._bold = None
        self._highlight = None
        self._department_page = None
        self._emphasized = None
        self._emphasized_highlight_bold_package = None
        self._multi_variant = None
        self.discriminator = None

        self.category = category
        if condition is not None:
            self.condition = condition
        if duration is not None:
            self.duration = duration
        if has_any_quantity is not None:
            self.has_any_quantity = has_any_quantity
        if number_of_big_photos is not None:
            self.number_of_big_photos = number_of_big_photos
        if number_of_photos is not None:
            self.number_of_photos = number_of_photos
        if quantity is not None:
            self.quantity = quantity
        if shop is not None:
            self.shop = shop
        if sold_quantity is not None:
            self.sold_quantity = sold_quantity
        if type is not None:
            self.type = type
        self.unit_price = unit_price
        if bold is not None:
            self.bold = bold
        if highlight is not None:
            self.highlight = highlight
        if department_page is not None:
            self.department_page = department_page
        if emphasized is not None:
            self.emphasized = emphasized
        if emphasized_highlight_bold_package is not None:
            self.emphasized_highlight_bold_package = emphasized_highlight_bold_package
        if multi_variant is not None:
            self.multi_variant = multi_variant

    @property
    def category(self):
        """Gets the category of this ParametersForPreviewPrice.  # noqa: E501


        :return: The category of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ParametersForPreviewPrice.


        :param category: The category of this ParametersForPreviewPrice.  # noqa: E501
        :type: Category
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def condition(self):
        """Gets the condition of this ParametersForPreviewPrice.  # noqa: E501

        Offer condition, if is new, used or other.  # noqa: E501

        :return: The condition of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this ParametersForPreviewPrice.

        Offer condition, if is new, used or other.  # noqa: E501

        :param condition: The condition of this ParametersForPreviewPrice.  # noqa: E501
        :type: str
        """
        allowed_values = ["NEW", "USED", "OTHER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and condition not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def duration(self):
        """Gets the duration of this ParametersForPreviewPrice.  # noqa: E501


        :return: The duration of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ParametersForPreviewPrice.


        :param duration: The duration of this ParametersForPreviewPrice.  # noqa: E501
        :type: str
        """
        allowed_values = ["PT72H", "PT120H", "PT168H", "PT240H", "PT336H", "PT480H", "PT720H"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and duration not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `duration` ({0}), must be one of {1}"  # noqa: E501
                .format(duration, allowed_values)
            )

        self._duration = duration

    @property
    def has_any_quantity(self):
        """Gets the has_any_quantity of this ParametersForPreviewPrice.  # noqa: E501


        :return: The has_any_quantity of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: bool
        """
        return self._has_any_quantity

    @has_any_quantity.setter
    def has_any_quantity(self, has_any_quantity):
        """Sets the has_any_quantity of this ParametersForPreviewPrice.


        :param has_any_quantity: The has_any_quantity of this ParametersForPreviewPrice.  # noqa: E501
        :type: bool
        """

        self._has_any_quantity = has_any_quantity

    @property
    def number_of_big_photos(self):
        """Gets the number_of_big_photos of this ParametersForPreviewPrice.  # noqa: E501

        If set, minimum value 0  # noqa: E501

        :return: The number_of_big_photos of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: int
        """
        return self._number_of_big_photos

    @number_of_big_photos.setter
    def number_of_big_photos(self, number_of_big_photos):
        """Sets the number_of_big_photos of this ParametersForPreviewPrice.

        If set, minimum value 0  # noqa: E501

        :param number_of_big_photos: The number_of_big_photos of this ParametersForPreviewPrice.  # noqa: E501
        :type: int
        """

        self._number_of_big_photos = number_of_big_photos

    @property
    def number_of_photos(self):
        """Gets the number_of_photos of this ParametersForPreviewPrice.  # noqa: E501

        If set, minimum value 0  # noqa: E501

        :return: The number_of_photos of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: int
        """
        return self._number_of_photos

    @number_of_photos.setter
    def number_of_photos(self, number_of_photos):
        """Sets the number_of_photos of this ParametersForPreviewPrice.

        If set, minimum value 0  # noqa: E501

        :param number_of_photos: The number_of_photos of this ParametersForPreviewPrice.  # noqa: E501
        :type: int
        """

        self._number_of_photos = number_of_photos

    @property
    def quantity(self):
        """Gets the quantity of this ParametersForPreviewPrice.  # noqa: E501

        Quantity of items to be sold. If set, minimum value 1  # noqa: E501

        :return: The quantity of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ParametersForPreviewPrice.

        Quantity of items to be sold. If set, minimum value 1  # noqa: E501

        :param quantity: The quantity of this ParametersForPreviewPrice.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def shop(self):
        """Gets the shop of this ParametersForPreviewPrice.  # noqa: E501

        Deprecated. Value 'true' sets the 'offer.type' field to 'shop', value 'false' to 'offer'. This field is ignored if 'offer.type' field is set.  # noqa: E501

        :return: The shop of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: bool
        """
        return self._shop

    @shop.setter
    def shop(self, shop):
        """Sets the shop of this ParametersForPreviewPrice.

        Deprecated. Value 'true' sets the 'offer.type' field to 'shop', value 'false' to 'offer'. This field is ignored if 'offer.type' field is set.  # noqa: E501

        :param shop: The shop of this ParametersForPreviewPrice.  # noqa: E501
        :type: bool
        """

        self._shop = shop

    @property
    def sold_quantity(self):
        """Gets the sold_quantity of this ParametersForPreviewPrice.  # noqa: E501

        Quantity of sold items. Relates to commission success fee. If set, minimum value 1  # noqa: E501

        :return: The sold_quantity of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: int
        """
        return self._sold_quantity

    @sold_quantity.setter
    def sold_quantity(self, sold_quantity):
        """Sets the sold_quantity of this ParametersForPreviewPrice.

        Quantity of sold items. Relates to commission success fee. If set, minimum value 1  # noqa: E501

        :param sold_quantity: The sold_quantity of this ParametersForPreviewPrice.  # noqa: E501
        :type: int
        """

        self._sold_quantity = sold_quantity

    @property
    def type(self):
        """Gets the type of this ParametersForPreviewPrice.  # noqa: E501

        Offer type. 'type' or 'shop' fields must be provided. Takes precedence over 'shop' field. Note: if type = 'advertisement' then either 'quantity' or 'soldQuantity' field must be set.  # noqa: E501

        :return: The type of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ParametersForPreviewPrice.

        Offer type. 'type' or 'shop' fields must be provided. Takes precedence over 'shop' field. Note: if type = 'advertisement' then either 'quantity' or 'soldQuantity' field must be set.  # noqa: E501

        :param type: The type of this ParametersForPreviewPrice.  # noqa: E501
        :type: str
        """
        allowed_values = ["shop", "offer", "advertisement"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def unit_price(self):
        """Gets the unit_price of this ParametersForPreviewPrice.  # noqa: E501


        :return: The unit_price of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this ParametersForPreviewPrice.


        :param unit_price: The unit_price of this ParametersForPreviewPrice.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and unit_price is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_price`, must not be `None`")  # noqa: E501

        self._unit_price = unit_price

    @property
    def bold(self):
        """Gets the bold of this ParametersForPreviewPrice.  # noqa: E501


        :return: The bold of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: bool
        """
        return self._bold

    @bold.setter
    def bold(self, bold):
        """Sets the bold of this ParametersForPreviewPrice.


        :param bold: The bold of this ParametersForPreviewPrice.  # noqa: E501
        :type: bool
        """

        self._bold = bold

    @property
    def highlight(self):
        """Gets the highlight of this ParametersForPreviewPrice.  # noqa: E501


        :return: The highlight of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: bool
        """
        return self._highlight

    @highlight.setter
    def highlight(self, highlight):
        """Sets the highlight of this ParametersForPreviewPrice.


        :param highlight: The highlight of this ParametersForPreviewPrice.  # noqa: E501
        :type: bool
        """

        self._highlight = highlight

    @property
    def department_page(self):
        """Gets the department_page of this ParametersForPreviewPrice.  # noqa: E501


        :return: The department_page of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: bool
        """
        return self._department_page

    @department_page.setter
    def department_page(self, department_page):
        """Sets the department_page of this ParametersForPreviewPrice.


        :param department_page: The department_page of this ParametersForPreviewPrice.  # noqa: E501
        :type: bool
        """

        self._department_page = department_page

    @property
    def emphasized(self):
        """Gets the emphasized of this ParametersForPreviewPrice.  # noqa: E501


        :return: The emphasized of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: bool
        """
        return self._emphasized

    @emphasized.setter
    def emphasized(self, emphasized):
        """Sets the emphasized of this ParametersForPreviewPrice.


        :param emphasized: The emphasized of this ParametersForPreviewPrice.  # noqa: E501
        :type: bool
        """

        self._emphasized = emphasized

    @property
    def emphasized_highlight_bold_package(self):
        """Gets the emphasized_highlight_bold_package of this ParametersForPreviewPrice.  # noqa: E501


        :return: The emphasized_highlight_bold_package of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: bool
        """
        return self._emphasized_highlight_bold_package

    @emphasized_highlight_bold_package.setter
    def emphasized_highlight_bold_package(self, emphasized_highlight_bold_package):
        """Sets the emphasized_highlight_bold_package of this ParametersForPreviewPrice.


        :param emphasized_highlight_bold_package: The emphasized_highlight_bold_package of this ParametersForPreviewPrice.  # noqa: E501
        :type: bool
        """

        self._emphasized_highlight_bold_package = emphasized_highlight_bold_package

    @property
    def multi_variant(self):
        """Gets the multi_variant of this ParametersForPreviewPrice.  # noqa: E501


        :return: The multi_variant of this ParametersForPreviewPrice.  # noqa: E501
        :rtype: bool
        """
        return self._multi_variant

    @multi_variant.setter
    def multi_variant(self, multi_variant):
        """Sets the multi_variant of this ParametersForPreviewPrice.


        :param multi_variant: The multi_variant of this ParametersForPreviewPrice.  # noqa: E501
        :type: bool
        """

        self._multi_variant = multi_variant

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
        if not isinstance(other, ParametersForPreviewPrice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParametersForPreviewPrice):
            return True

        return self.to_dict() != other.to_dict()