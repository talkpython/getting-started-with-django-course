# Alexandria/test/test_home.py
from django.test import TestCase
from django.test import Client

class HomeTestCase(TestCase):
    def test_home(self):
        response = self.client.get('/home/sample/')
        self.assertEqual(200, response.status_code)
        self.assertIn("books", response.context)

        response = self.client.get('/home/about/')
        self.assertEqual(200, response.status_code)

        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
