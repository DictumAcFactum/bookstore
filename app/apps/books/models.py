import uuid

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    class Meta:
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', kwargs={'pk': self.pk})


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'Review: {self.book}'
