import factory
from . import models


class BookFactory(factory.Factory):
    author = factory.Faker('name')
    price = factory.Faker('pydecimal')

    class Meta:
        model = models.Book
