# Alexandria/review/admin.py
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import Truncator

from review.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_user', 'show_book', 'rating', 'show_summary')

    def show_user(self, obj):
        url = reverse('admin:auth_user_changelist') + f'?id={obj.user.id}'
        return format_html('<a href="{}">{}</a>', url, obj.user.username)

    def show_book(self, obj):
        url = reverse('admin:catalog_book_changelist') + f'?id={obj.book.id}'
        return format_html('<a href="{}">{}</a>', url, obj.book.title)

    def show_summary(self, obj):
        return Truncator(obj.text).words(5, truncate=' ...') 
