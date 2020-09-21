from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'director')
        model = Movie