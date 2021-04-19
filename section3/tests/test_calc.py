from unittest import TestCase

from section3.sandwich_calc import Calculator


class TestCalc(TestCase):
    edge_cases = [0, 0.0]

    def test_markup(self):
        for item in self.edge_cases:
            test_calc = Calculator(item)
            self.assertGreaterEqual(test_calc.markup(), item)

    def test_discount(self):
        self.assertEqual(1, 1)
