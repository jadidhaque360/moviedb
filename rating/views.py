# notes/views.py
from rest_framework import viewsets
from rest_framework import permissions
from .models import Rating
from movies.models import Movie
from .serializers import RatingSerializer
from rest_framework.exceptions import PermissionDenied

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Rating.objects.all()
        else:
            raise PermissionDenied()

    # Set user as owner of a Movie object.
    def perform_create(self, serializer):
        user = self.request.user
        movie = Movie.objects.get(id=self.request.data['movie_id'])
        dublicateRating = Rating.objects.all().filter(owner_id=user,movie_id=movie)
        if user.is_authenticated and not dublicateRating.exists():
            r = Rating(owner_id=user,movie_id=movie,rate=self.request.data['rate'])
            r.save()
        else:
            raise PermissionDenied()