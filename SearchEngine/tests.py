from django.test import TestCase
from django.urls import resolve
from .views import index


class HomePageTest(TestCase):
    def test_main_root(self):
        found = resolve('/')
        self.assertEqual(found.func, index)