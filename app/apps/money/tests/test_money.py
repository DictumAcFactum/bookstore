from django.test import TestCase
from ..currency import Dollar


class MoneyTestCase(TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEqual(5 * 2, five.amount)
