from django.test import TestCase
from django.urls import reverse, resolve
from app_blog.views import HomePageView, ArticleCategoryList
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)
    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('example-slug',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
class UrlsTest(TestCase):
    def test_home_url_resolves_home_view(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomePageView)

    def test_category_url_resolves_category_view(self):
        url = reverse('articles-category-list', args=('example-slug',))
        self.assertEqual(resolve(url).func.view_class, ArticleCategoryList)
