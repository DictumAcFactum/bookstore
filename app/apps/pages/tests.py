from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView


class HomepageTests(TestCase):

    def setUp(self) -> None:
        self.response = self.client.get(reverse('home'))

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_homepage_url_resolves_homepage_view(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__, HomePageView.as_view().__name__
        )
