class Expression:
    """Base class for money expressions"""

    def plus(self, other):
        """Return new child class with sum amounts and given currency type"""
        return self.__class__((self.amount + other.amount), self.get_currency_type)
