from .. import currency


class Currency:
    def __init__(self, amount):
        self.amount = amount

    @staticmethod
    def dollar(val):
        return currency.Dollar(val)

    @staticmethod
    def franc(val):
        return currency.Franc(val)

    def times(self, multiplier):
        return self.__class__(self.amount * multiplier)

    def __eq__(self, other):
        return self.amount == other

    def equals(self, other):
        return self.amount == other.amount and self.__class__ == other.__class__
