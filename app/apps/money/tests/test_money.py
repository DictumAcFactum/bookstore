from django.test import TestCase
from ..currency import Dollar


class MoneyTestCase(TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))
