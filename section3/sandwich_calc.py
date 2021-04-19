"""
calc sandwich
"""

from random import randint

import numpy  # pylint: disable=E0401


class Calculator:
    """
    calc costs
    """

    def __init__(self, my_cost):
        self.charge = 0
        self.my_cost = my_cost

    def markup(self):
        """

        :return:
        """
        weights = numpy.random.random((3, 3))
        x = randint(0, 2)  # pylint: disable=C0103
        y = randint(0, 2)  # pylint: disable=C0103
        today_weight = weights[x][y] + 1
        self.charge = self.my_cost * today_weight
        assert self.charge >= self.my_cost
        return self.charge

    def family_discount(self):
        """

        :return:
        """
        self.charge = self.my_cost * 0.75
        return round(self.charge, 2)
