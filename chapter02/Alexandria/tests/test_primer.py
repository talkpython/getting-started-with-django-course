# Alexandria/test/test_primer.py
from django.test import TestCase

class PrimerTestCase(TestCase):
    def test_say_hello(self):
        response = self.client.get('/say_hello/')
        self.assertEqual(200, response.status_code)
        self.assertIn("Hello", str(response.content))
