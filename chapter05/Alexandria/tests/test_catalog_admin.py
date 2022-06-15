# Alexandria/tests/test_catalog_admin.py
from django.contrib import admin
from django.contrib.admin.utils import lookup_field
from django.contrib.auth.models import User
from django.test import TestCase

from catalog.admin import AuthorAdmin
from catalog.models import Author

class CatalogAdminTestCase(TestCase):
    ADMIN_USER = "admin"
    ADMIN_EMAIL = "admin@example.com"
    ADMIN_PASSWORD = "hjsafd.k$oipwer"

    def setUp(self):
        super().setUp()
        self.site = admin.sites.AdminSite()
        self.admin_user = User.objects.create_user(self.ADMIN_USER, 
            self.ADMIN_EMAIL, self.ADMIN_PASSWORD)
        self.admin_user.is_staff = True
        self.admin_user.is_superuser = True
        self.admin_user.save()

    def test_book_listing(self):
        # Authenticate as admin user
        response = self.client.login(username=self.ADMIN_USER, 
            password=self.ADMIN_PASSWORD)
        self.assertTrue(response)

        # Fetch book listing page
        response = self.client.get("/admin/catalog/book/")
        self.assertEqual(200, response.status_code)

        # Check show_books field
        author = Author.objects.create(last_name="McTest", birth_year=2000)
        author_admin = AuthorAdmin(author, self.site)

        _, _, value = lookup_field("show_books", author, author_admin)
        self.assertIn(f"?author__id={author.id}", value)
