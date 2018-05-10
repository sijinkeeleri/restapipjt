from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    publisher = models.CharField(max_length=256)
    language = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
