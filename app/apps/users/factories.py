import factory

from django.contrib.auth import get_user_model


class UserFactory(factory.Factory):
    is_active = True
    email = factory.Faker('email')
    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = get_user_model()
