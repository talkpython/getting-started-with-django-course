# Alexandria/catalog/views.py
from pathlib import Path

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from catalog.models import Author, Book
from catalog.serializers import AuthorSerializer

def book_listing(request):
    data = {
        'books':Book.objects.order_by('author__last_name', 'title'),
    }

    return render(request, 'book_listing.html', data)


def book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book.html', {'book':book})


def author_listing(request):
    data = {
        'authors':Author.objects.order_by('last_name'),
    }
    return render(request, 'author_listing.html', data)


def author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'author.html', {'author':author})


@login_required
def upload_author_photo(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    data = {
        'author':author,
    }

    if request.method == 'GET':
        return render(request, 'upload_author_photo.html', data)

    # POST
    upload = request.FILES['author_photo']
    path = Path(settings.MEDIA_ROOT) / f'{request.user.id}_{upload.name}'
    with open(path, 'wb+') as output:
        for chunk in upload.chunks():
            output.write(chunk)

    author.picture = path.name
    author.save()

    return redirect('author', author.id)


@api_view(["GET"])
def list_authors_api(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    content = {
        "authors": serializer.data,
    }

    return Response(content)
