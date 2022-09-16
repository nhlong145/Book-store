from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse, resolve # new
from .views import HomePageView # new

class HomepageTests(SimpleTestCase):
    def setUp(self):
        url =self.urls= reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self): # new
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self): # new
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self): # new
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve('/')
        print(view)
        print(reverse('home'))
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
