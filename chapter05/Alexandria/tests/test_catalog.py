# Alexandria/test/test_catalog.py
from django.test import TestCase
from django.test import Client

from catalog.models import Author, Book

class CatalogTestCase(TestCase):
    def print_state(self, msg):
        num_books = Book.objects.count()
        num_authors = Author.objects.count()
        print(f"{msg}; #books={num_books} #authors={num_authors}")

    def setUp(self):
        print(55*"=")
        self.print_state("Starting setUp()")

        author = Author.objects.create(last_name="McTest", birth_year=2000)
        Book.objects.create(title="The art of test", author=author)

        self.print_state("Finished setUp()")

    def test_stringify(self):
        self.print_state("Starting test_stringify()")

        book = Book.objects.get(id=1)
        result = str(book)
        self.assertIn(f"author_id={book.author.id}", result)

        self.print_state("Finished test_stringify()")

    def test_listing(self):
        self.print_state("Starting test_listing()")

        response = self.client.get('/catalog/book_listing/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.context["books"]))

        self.print_state("Finished test_listing()")
