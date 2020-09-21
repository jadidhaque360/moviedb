# notes/views.py
from rest_framework import viewsets
from rest_framework import permissions
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.exceptions import PermissionDenied

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Movie.objects.all()
        else:
            raise PermissionDenied()

    # Set user as owner of a Movie object.
    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(owner=user)
        else:
            raise PermissionDenied()
        