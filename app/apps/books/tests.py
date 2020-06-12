from requests import codes

from django.test import TestCase
from django.urls import reverse


class BookListTestCase(TestCase):
    def setUp(self) -> None:
        url = reverse('books:book_list')
        self.response = self.client.get(url)

    def test_book_list_status_code(self):
        self.assertEqual(self.response.status_code, codes.ok)

    def test_book_list_template(self):
        self.assertTemplateUsed(self.response, 'books/book_list.html')


class BookDetailTestCase(TestCase):
    pass
