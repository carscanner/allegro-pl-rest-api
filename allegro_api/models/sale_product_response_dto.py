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


class SaleProductResponseDto(object):
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
        'name': 'str',
        'category': 'Category',
        'ean': 'str',
        'eans': 'list[str]',
        'images': 'list[ImageUrl]',
        'parameters': 'list[ProductParameter]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'category': 'category',
        'ean': 'ean',
        'eans': 'eans',
        'images': 'images',
        'parameters': 'parameters'
    }

    def __init__(self, id=None, name=None, category=None, ean=None, eans=None, images=None, parameters=None):  # noqa: E501
        """SaleProductResponseDto - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._category = None
        self._ean = None
        self._eans = None
        self._images = None
        self._parameters = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.category = category
        if ean is not None:
            self.ean = ean
        if eans is not None:
            self.eans = eans
        if images is not None:
            self.images = images
        if parameters is not None:
            self.parameters = parameters

    @property
    def id(self):
        """Gets the id of this SaleProductResponseDto.  # noqa: E501


        :return: The id of this SaleProductResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SaleProductResponseDto.


        :param id: The id of this SaleProductResponseDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SaleProductResponseDto.  # noqa: E501

        Name of the product.  # noqa: E501

        :return: The name of this SaleProductResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaleProductResponseDto.

        Name of the product.  # noqa: E501

        :param name: The name of this SaleProductResponseDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def category(self):
        """Gets the category of this SaleProductResponseDto.  # noqa: E501


        :return: The category of this SaleProductResponseDto.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SaleProductResponseDto.


        :param category: The category of this SaleProductResponseDto.  # noqa: E501
        :type: Category
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def ean(self):
        """Gets the ean of this SaleProductResponseDto.  # noqa: E501


        :return: The ean of this SaleProductResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this SaleProductResponseDto.


        :param ean: The ean of this SaleProductResponseDto.  # noqa: E501
        :type: str
        """
        if ean is not None and len(ean) > 18:
            raise ValueError("Invalid value for `ean`, length must be less than or equal to `18`")  # noqa: E501

        self._ean = ean

    @property
    def eans(self):
        """Gets the eans of this SaleProductResponseDto.  # noqa: E501

        A list of codes that identify this product. Currently this can include EAN, ISBN, and UPC identifier types.  # noqa: E501

        :return: The eans of this SaleProductResponseDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._eans

    @eans.setter
    def eans(self, eans):
        """Sets the eans of this SaleProductResponseDto.

        A list of codes that identify this product. Currently this can include EAN, ISBN, and UPC identifier types.  # noqa: E501

        :param eans: The eans of this SaleProductResponseDto.  # noqa: E501
        :type: list[str]
        """

        self._eans = eans

    @property
    def images(self):
        """Gets the images of this SaleProductResponseDto.  # noqa: E501


        :return: The images of this SaleProductResponseDto.  # noqa: E501
        :rtype: list[ImageUrl]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this SaleProductResponseDto.


        :param images: The images of this SaleProductResponseDto.  # noqa: E501
        :type: list[ImageUrl]
        """

        self._images = images

    @property
    def parameters(self):
        """Gets the parameters of this SaleProductResponseDto.  # noqa: E501


        :return: The parameters of this SaleProductResponseDto.  # noqa: E501
        :rtype: list[ProductParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this SaleProductResponseDto.


        :param parameters: The parameters of this SaleProductResponseDto.  # noqa: E501
        :type: list[ProductParameter]
        """

        self._parameters = parameters

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
        if not isinstance(other, SaleProductResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other