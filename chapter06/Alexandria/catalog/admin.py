# Alexandria/catalog/admin.py

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from catalog.models import Book, Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
#    pass
    list_display = ('id', 'last_name', 'first_name', 'show_books')

    def show_books(self, obj):
        count = Book.objects.filter(author=obj).count()
        url = reverse('admin:catalog_book_changelist') + f'?author__id={obj.id}'
        plural = 's' if count != 1 else ''

        return format_html('<a href="{}">{} Book{}</a>', url, count, plural)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
#    list_display = ('id', 'title')
    list_display = ('id', 'title', 'author_last_name')
    list_filter = ('author', )

    def author_last_name(self, obj):
        return obj.author.last_name
