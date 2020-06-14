import factory
from . import models


class BookFactory(factory.Factory):
    author = factory.Faker('name')

    class Meta:
        model = models.Book
