"""
utils functions
"""
from typing import Union


def is_element_exist(elements: Union[list, tuple, str], element) -> bool:
    """
    search an item at items
    :param elements: iterable obj
    :param element: item to find
    :return: True if item exist else False
    """

    return element in elements


print(is_element_exist([2, 4, 5], 4))


class Number:
    """
    representation for numbers
    """

    def __init__(self, num):
        self.num = num

    def is_even(self):
        """
        check the number is even or odd
        :return: True if number is even else False
        """
        return self.num % 2 == 0

    def fizzbuz(self):
        """
        check fizz buzz for number
        :return: Fizzbuzz, Fizz, Buzz, number
        """
        if self.num % 3 == 0 and self.num % 5 == 0:
            return "FizzBuzz"
        if self.num % 3 == 0:
            return "Fizz"
        if self.num % 5 == 0:
            return "Buzz"
        return self.num

    def is_odd(self):
        """
        :return:
        """
        return self


def get_quarter_by_mont(month):
    """

    :param month: valid month number
    :return: quarter of that month
    """
    if month not in range(1, 13):
        raise ValueError("invalid month <{}>".format(month))
    return month // 4 + 1


print(get_quarter_by_mont(4))
