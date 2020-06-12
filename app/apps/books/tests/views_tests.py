from requests import codes

from django.test import TestCase
from django.urls import reverse

from .. import models


class BookListTestCase(TestCase):
    def setUp(self) -> None:
        url = reverse('books:book_list')
        self.response = self.client.get(url)

    def test_book_list_status_code(self):
        self.assertEqual(self.response.status_code, codes.ok)

    def test_book_list_template(self):
        self.assertTemplateUsed(self.response, 'books/book_list.html')


class BookDetailTestCase(TestCase):
    def setUp(self) -> None:
        self.book = models.Book.objects.create(
            title='Dialogues',
            author='Plato',
            price='20.00',
        )
        self.response = self.client.get(self.book.get_absolute_url())
        self.no_response = self.client.get('books/1234')

    def test_book_detail_status_code(self):
        self.assertEqual(self.response.status_code, codes.ok)
        self.assertEqual(self.no_response.status_code, codes.not_found)

    def test_book_detail_template(self):
        self.assertTemplateUsed(self.response, 'books/book_detail.html')
