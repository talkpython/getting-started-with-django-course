# Alexandria/review/urls.py

from django.urls import path

from review import views

urlpatterns = [
    path('review_book/<int:book_id>/', views.review_book, name="review_book"),
]
