import factory

from apps.users import factories as users_factories
from . import models


class BookFactory(factory.Factory):
    author = factory.Faker('name')
    price = factory.Faker('pydecimal')

    class Meta:
        model = models.Book


class ReviewFactory(factory.Factory):
    book = factory.SubFactory(BookFactory)
    review = factory.Faker('sentence')
    author = factory.SubFactory(users_factories.UserFactory)

    class Meta:
        model = models.Review
