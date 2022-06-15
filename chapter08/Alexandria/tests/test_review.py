# Alexandria/tests/test_review.py
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Author, Book
from review.models import Review

class ReviewTestCase(TestCase):
    PASSWORD = 'asdfasdf33'

    def setUp(self):
        super().setUp()
        self.users = []

        for x in range(3):
            user = User.objects.create_user(f'user{x}', f'user{x}@example.com',
                self.PASSWORD)
            self.users.append(user)

    def test_reviews(self):
        author = Author.objects.create(last_name="auth_ln",
            first_name="auth_fn", birth_year=1900)
        book = Book.objects.create(title="book", author=author)

        # Verify no-review state
        book_url = reverse('book', args=(book.id, ))
        response = self.client.get(book_url)
        self.assertEqual(200, response.status_code)
        self.assertIn("No reviews yet!", str(response.content))

        # Verify login redirect
        review_url = reverse('review_book', args=(book.id, ))
        response = self.client.get(review_url)
        self.assertEqual(302, response.status_code)
        self.assertIn('login', response.url)

        # Post a review
        review_data1 = {
            'rating':1,
            'text':'This is some review text',
        }

        self.client.login(username=self.users[0], password=self.PASSWORD)
        response = self.client.post(review_url, review_data1)
        self.assertEqual(302, response.status_code)
        self.assertEqual(f'/catalog/book/{book.id}/', response.url)

        review = book.review_set.first()
        self.assertEqual(review_data1['rating'], review.rating)
        self.assertEqual(review_data1['text'], review.text)

        # Post another review
        review_data2 = {
            'rating':2,
            'text':'More review text',
        }

        self.client.login(username=self.users[1], password=self.PASSWORD)
        self.client.post(review_url, review_data2)

        review = book.review_set.all()[1]
        self.assertEqual(review_data2['rating'], review.rating)
        self.assertEqual(review_data2['text'], review.text)

        # Verify book page has reviews
        self.client.logout()
        response = self.client.get(book_url)
        self.assertEqual(200, response.status_code)
        self.assertIn(f"{self.users[0].username} says {review_data1['rating']}",
            str(response.content))
        self.assertIn(f"{self.users[1].username} says {review_data2['rating']}",
            str(response.content))

        # Verify there are only two reviews
        num = str(response.content).count("card-body")
        self.assertEqual(2, num)
