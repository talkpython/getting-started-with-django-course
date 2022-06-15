# people/models.py
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from catalog.models import Book

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_books = models.ManyToManyField(Book)

@receiver(post_save, sender=User)
def user_post_save(sender, **kwargs):
    # Create Reader object if User object is new and not loaded from fixture
    if kwargs['created'] and not kwargs['raw']:
        user = kwargs['instance']
        try:
            # Double check Reader doesn't exist already (admin might create it
            # before the signal fires)
            reader = Reader.objects.get(user=user)
        except Reader.DoesNotExist:
            # No Reader exists for this user, create one
            Reader.objects.create(user=user)
