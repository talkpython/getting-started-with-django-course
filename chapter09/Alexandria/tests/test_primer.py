# Alexandria/tests/test_primer.py
from django.test import TestCase
from django.test import Client

class PrimerTestCase(TestCase):
    def test_say_hello(self):
        response = self.client.get('/say_hello/')
        self.assertEqual(200, response.status_code)
        self.assertIn("Hello", str(response.content))
