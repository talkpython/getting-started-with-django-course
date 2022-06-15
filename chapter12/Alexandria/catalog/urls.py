# Alexandria/catalog/urls.py

from django.urls import path

from catalog import views

urlpatterns = [
    path('book_listing/', views.book_listing, name="book_listing"),
    path('book/<int:book_id>/', views.book, name="book"),
    path('author_listing/', views.author_listing, name="author_listing"),
    path('author/<int:author_id>/', views.author, name="author"),
    path('upload_author_photo/<int:author_id>/', views.upload_author_photo, 
        name="upload_author_photo"),

    path('list_authors_api/', views.list_authors_api),
]
