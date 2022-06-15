# review/models.py
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from catalog.models import Book

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(5)))
    text = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'],
                name="unique_review"),
        ]

    def __str__(self):
        return f"Review(id={self.id}, user={self.user.username}, book={self.book.title})"
