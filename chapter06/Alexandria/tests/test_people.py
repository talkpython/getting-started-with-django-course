# Alexandria/tests/test_people.py
from django.contrib.auth.models import User
from django.test import TestCase, Client

class PeopleTestCase(TestCase):
    def test_reader_signal(self):
        user = User.objects.create(username="foo", password="asdfasdf33")
        self.assertIsNotNone(user.reader)

    def test_404(self):
        response = self.client.get('/not_a_valid_url/')
        expected = 'The pages are still blank,'
        self.assertIn(expected, str(response.content))
