from django.db import models

# Create your models here.

# A simple movie model for early stage testing
class SimpleMovie(models.Model):
    title = models.CharField(max_length=100);
    description = models.TextField()
    rating = models.TextField()

