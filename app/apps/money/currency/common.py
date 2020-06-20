from .. import currency


class Currency:
    def __init__(self, amount, currency_type=None):
        self.amount = amount
        self.currency_type = currency_type

    def __eq__(self, other):
        return self.amount == other

    def __str__(self):
        return f'{self.amount} {self.currency_type}'

    @staticmethod
    def dollar(val):
        return currency.Dollar(val, currency_type='USD')

    @staticmethod
    def franc(val):
        return currency.Franc(val, currency_type='CHF')

    def times(self, multiplier):
        return Currency(self.amount * multiplier, currency_type=self.currency_type)

    def equals(self, other):
        return self.amount == other.amount and self.get_currency_type == other.get_currency_type

    @property
    def get_currency_type(self):
        return self.currency_type
