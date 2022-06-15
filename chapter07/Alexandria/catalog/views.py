# Alexandria/catalog/views.py
from django.shortcuts import render, get_object_or_404

from catalog.models import Book

def book_listing(request):
    data = {
        'books':Book.objects.order_by('author__last_name', 'title'),
    }

    return render(request, 'book_listing.html', data)

def book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book.html', {'book':book})
