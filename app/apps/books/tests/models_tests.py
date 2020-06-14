from django.test import TestCase

from ..factories import BookFactory


class BookTestCase(TestCase):
    def setUp(self) -> None:
        self.book = BookFactory.create(
            title='Dialogues',
            author='Plato',
            price='20.00',
        )

    def test_book_listing(self):
        self.assertEqual(self.book.title, 'Dialogues')
        self.assertEqual(self.book.author, 'Plato')
        self.assertEqual(self.book.price, '20.00')
