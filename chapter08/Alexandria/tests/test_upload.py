# Alexandria/tests/test_upload.py
from pathlib import Path

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Author, Book

class UploadTestCase(TestCase):
    PASSWORD = 'asdfasdf33'

    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(f'testy', f'testy@example.com',
            self.PASSWORD)

    def test_photo_upload(self):
        author = Author.objects.create(first_name="Bob", last_name="Loblaw",
            birth_year=1960)
        author_url = reverse('author', args=(author.id, ))
        upload_url = reverse('upload_author_photo', args=(author.id, ))

        # Test upload button isn't there if not signed in
        response = self.client.get(author_url)
        self.assertEqual(200, response.status_code)
        self.assertNotIn('id="id_author_upload"', str(response.content))

        # Test login_required fires
        response = self.client.get(upload_url)
        self.assertEqual(302, response.status_code)
        self.assertIn('login', response.url)

        # Sign-in, check for button
        self.client.login(username=self.user, password=self.PASSWORD)
        response = self.client.get(author_url)
        self.assertEqual(200, response.status_code)
        self.assertIn('id="id_author_upload"', str(response.content))

        # Test image upload
        with open('tests/data/Michael.jpg', 'rb') as f:
            content = f.read()
            photo = SimpleUploadedFile("Michael.jpg", f.read(), 'image/jpeg')
            data = {
                'author_photo':photo,
            }

            response = self.client.post(upload_url, data)
            self.assertEqual(302, response.status_code)
            self.assertIn('author', response.url)

        # Refetch Author, should now have a file field
        author = Author.objects.get(id=author.id)
        self.assertEqual('1_Michael.jpg', author.picture.name)

        # Clean up
        path = Path(settings.MEDIA_ROOT) / '1_Michael.jpg'
        path.unlink()
