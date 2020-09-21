from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner_id', 'movie_id', 'rate')
        model = Rating