from rest_framework import serializers
from .models import SimpleMovie

class SimpleMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleMovie
        fields = ['id', 'title', 'description', 'rating']
        