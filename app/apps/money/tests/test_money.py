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
        self.assertFalse(Currency.dollar(10) == Currency.franc(10))
        self.assertFalse(Currency.franc(10) == Currency.franc(100))
        self.assertTrue(Currency.dollar(1) == Currency.dollar(1))
        self.assertTrue(Currency.franc(42) == Currency.franc(42))
        self.assertFalse(Currency.dollar(1) == Currency.franc(1))

    def test_currency_type(self):
        self.assertEqual('USD', Currency.dollar(1).get_currency_type)
        self.assertNotEqual('CHF', Currency.dollar(1).get_currency_type)
        self.assertEqual('CHF', Currency.franc(1).get_currency_type)
        self.assertEqual('USD', self.five_dollars.times(2).get_currency_type)
        self.assertEqual('USD', self.five_dollars.get_currency_type)
        self.assertEqual('USD', self.five_dollars.get_currency_type)

    def test_currency_str(self):
        self.assertEqual(self.five_francs.__str__(), '5 CHF')
        self.assertEqual(Currency.dollar(100).__str__(), '100 USD')
        self.assertEqual(Currency(5).__str__(), '5 None')
