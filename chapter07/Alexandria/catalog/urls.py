# Alexandria/catalog/urls.py

from django.urls import path

from catalog import views

urlpatterns = [
    path('book_listing/', views.book_listing, name="book_listing"),
    path('book/<int:book_id>/', views.book, name="book"),
]
