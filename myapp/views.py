from django.shortcuts import render
from rest_framework import viewsets
from .models import SimpleMovie
from .serializers import SimpleMovieSerializer

# Create your views here.

# Class-based view to automatically handle CRUD operations on SimpleMovie
# Handles GET (all), GET (one), POST, PUT, PATCH, DELETE
class SimpleMovieViewSet(viewsets.ModelViewSet):
    queryset = SimpleMovie.objects.all()
    serializer_class = SimpleMovieSerializer

