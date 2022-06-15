# Alexandria/tests/test_cmds.py
from io import StringIO

from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase

from catalog.models import Author, Book

class CommandsTestCase(TestCase):
    def run_command(self, name, *args, **options):
        stdout = StringIO()
        options['stdout'] = stdout
        call_command(name, *args, **options)
        return stdout.getvalue()

    def setUp(self):
        super().setUp()

        self.author = Author.objects.create(first_name='fname',
            last_name='lname', birth_year=1900)
        self.book1 = Book.objects.create(title='title1', author=self.author)
        self.book2 = Book.objects.create(title='title2', author=self.author)

    def test_author(self):
        out = self.run_command('authors')
        self.assertEqual(1, out.count('\n'))
        self.assertIn('lname', out)

    def test_book(self):
        # Test the --all switch
        out = self.run_command('book', all=True)
        self.assertEqual(2, out.count('\n'))
        self.assertIn('title1', out)
        self.assertIn('title2', out)

        # Test id argument
        out = self.run_command('book', self.book1.id)
        self.assertEqual(1, out.count('\n'))
        self.assertIn('title1', out)

        # Test error management
        with self.assertRaises(CommandError):
            self.run_command('book')
