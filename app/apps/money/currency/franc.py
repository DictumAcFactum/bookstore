from .common import Currency


class Franc(Currency):
    def times(self, multiplier):
        return Franc(self.amount * multiplier)
