from django.test import TestCase
from ..currency import Dollar, Franc


class MoneyTestCase(TestCase):
    def setUp(self) -> None:
        self.five_dollars = Dollar(5)
        self.five_francs = Franc(5)

    def test_dollar_multiplication(self):
        self.assertEqual(Dollar(10), self.five_dollars.times(2))
        self.assertEqual(Dollar(15), self.five_dollars.times(3))

    def test_franc_multiplication(self):
        self.assertEqual(Franc(10), self.five_francs.times(2))
        self.assertEqual(Franc(15), self.five_francs.times(3))

    def test_equality(self):
        self.assertFalse(Dollar(10).equals(Franc(10)))
        self.assertFalse(Franc(5).equals(Dollar(5)))
        self.assertFalse(Dollar(77).equals(Dollar(88)))
        self.assertTrue(Dollar(1).equals(Dollar(1)))
        self.assertTrue(Franc(42).equals(Franc(42)))
