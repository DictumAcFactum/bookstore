class Currency:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        raise NotImplementedError(f'{self.__class__.__name__} should implement times method')

    def __eq__(self, other):
        return self.amount == other
