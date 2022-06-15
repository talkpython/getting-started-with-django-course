# Alexandria/catalog/serializers.py
from rest_framework import serializers

from catalog.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name", "birth_year"]
