# Alexandria/catalog/views.py

from django.shortcuts import render

from catalog.models import Book

def book_listing(request):
    data = {
        'books':Book.objects.order_by('author__last_name', 'title'),
    }

    return render(request, 'book_listing.html', data)
