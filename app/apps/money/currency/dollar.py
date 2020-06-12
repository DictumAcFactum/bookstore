from .common import Currency


class Dollar(Currency):
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
