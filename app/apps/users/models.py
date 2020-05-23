from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField('User image', upload_to='user/image', blank=True)

    def __str__(self):
        return self.username
