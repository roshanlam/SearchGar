from django.test import TestCase
from django.urls import resolve
from .views import index


class HomePageTest(TestCase):
    def test_main_root(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

class SearchFunctionlity(TestCase):
    def test_search(self):
        pass

class CrawlFunctionlity(TestCase):
    def test_crawl(self):
        pass