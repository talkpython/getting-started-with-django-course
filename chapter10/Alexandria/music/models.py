# Alexandria/music/models.py
from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=50)

# uncomment during Chapter 10
#    artist_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Song(id={self.id}, title={self.title})"
