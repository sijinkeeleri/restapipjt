from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'pk',
            'name',
            'author',
            'publisher',
        ]
        #convert to json
        # validation for data passed
        