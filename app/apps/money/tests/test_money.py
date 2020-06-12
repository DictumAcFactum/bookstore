from django.test import TestCase
from ..currency import Currency


class MoneyTestCase(TestCase):
    def setUp(self) -> None:
        self.five_dollars = Currency.dollar(5)
        self.five_francs = Currency.franc(5)

    def test_dollar_multiplication(self):
        self.assertEqual(Currency.dollar(10), self.five_dollars.times(2))
        self.assertEqual(Currency.dollar(15), self.five_dollars.times(3))

    def test_franc_multiplication(self):
        self.assertEqual(Currency.franc(10), self.five_francs.times(2))
        self.assertEqual(Currency.franc(15), self.five_francs.times(3))

    def test_equality(self):
        self.assertFalse(Currency.dollar(10).equals(Currency.franc(10)))
        self.assertFalse(Currency.franc(10).equals(Currency.franc(100)))
        self.assertFalse(Currency.dollar(77).equals(Currency.dollar(88)))
        self.assertTrue(Currency.dollar(1).equals(Currency.dollar(1)))
        self.assertTrue(Currency.franc(42).equals(Currency.franc(42)))
        self.assertFalse(Currency.dollar(1).equals(Currency.franc(1)))
