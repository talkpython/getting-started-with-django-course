# Alexandria/catalog/models.py

from django.db import models

class Author(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True)
    birth_year = models.IntegerField()

class Book(models.Model):
    title = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True,
        null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

### Uncommented in chapter 4 {
#    def __str__(self):
#        return f"Book(id={self.id}, title={self.title}, author_id={self.author.id})"
### }
