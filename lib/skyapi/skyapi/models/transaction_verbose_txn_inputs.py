# coding: utf-8

"""
    Skycoin REST API.

    Skycoin is a next-generation cryptocurrency.  # noqa: E501

    OpenAPI spec version: 0.26.0
    Contact: contact@skycoin.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TransactionVerboseTxnInputs(object):
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
        'uxid': 'str',
        'owner': 'str',
        'coins': 'str',
        'hours': 'int',
        'calculated_hours': 'int'
    }

    attribute_map = {
        'uxid': 'uxid',
        'owner': 'owner',
        'coins': 'coins',
        'hours': 'hours',
        'calculated_hours': 'calculated_hours'
    }

    def __init__(self, uxid=None, owner=None, coins=None, hours=None, calculated_hours=None):  # noqa: E501
        """TransactionVerboseTxnInputs - a model defined in OpenAPI"""  # noqa: E501

        self._uxid = None
        self._owner = None
        self._coins = None
        self._hours = None
        self._calculated_hours = None
        self.discriminator = None

        if uxid is not None:
            self.uxid = uxid
        if owner is not None:
            self.owner = owner
        if coins is not None:
            self.coins = coins
        if hours is not None:
            self.hours = hours
        if calculated_hours is not None:
            self.calculated_hours = calculated_hours

    @property
    def uxid(self):
        """Gets the uxid of this TransactionVerboseTxnInputs.  # noqa: E501


        :return: The uxid of this TransactionVerboseTxnInputs.  # noqa: E501
        :rtype: str
        """
        return self._uxid

    @uxid.setter
    def uxid(self, uxid):
        """Sets the uxid of this TransactionVerboseTxnInputs.


        :param uxid: The uxid of this TransactionVerboseTxnInputs.  # noqa: E501
        :type: str
        """

        self._uxid = uxid

    @property
    def owner(self):
        """Gets the owner of this TransactionVerboseTxnInputs.  # noqa: E501


        :return: The owner of this TransactionVerboseTxnInputs.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this TransactionVerboseTxnInputs.


        :param owner: The owner of this TransactionVerboseTxnInputs.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def coins(self):
        """Gets the coins of this TransactionVerboseTxnInputs.  # noqa: E501


        :return: The coins of this TransactionVerboseTxnInputs.  # noqa: E501
        :rtype: str
        """
        return self._coins

    @coins.setter
    def coins(self, coins):
        """Sets the coins of this TransactionVerboseTxnInputs.


        :param coins: The coins of this TransactionVerboseTxnInputs.  # noqa: E501
        :type: str
        """

        self._coins = coins

    @property
    def hours(self):
        """Gets the hours of this TransactionVerboseTxnInputs.  # noqa: E501


        :return: The hours of this TransactionVerboseTxnInputs.  # noqa: E501
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this TransactionVerboseTxnInputs.


        :param hours: The hours of this TransactionVerboseTxnInputs.  # noqa: E501
        :type: int
        """

        self._hours = hours

    @property
    def calculated_hours(self):
        """Gets the calculated_hours of this TransactionVerboseTxnInputs.  # noqa: E501


        :return: The calculated_hours of this TransactionVerboseTxnInputs.  # noqa: E501
        :rtype: int
        """
        return self._calculated_hours

    @calculated_hours.setter
    def calculated_hours(self, calculated_hours):
        """Sets the calculated_hours of this TransactionVerboseTxnInputs.


        :param calculated_hours: The calculated_hours of this TransactionVerboseTxnInputs.  # noqa: E501
        :type: int
        """

        self._calculated_hours = calculated_hours

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
        if not isinstance(other, TransactionVerboseTxnInputs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
