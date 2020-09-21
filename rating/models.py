from __future__ import unicode_literals
from django.contrib.auth.models import User
from movies.models import Movie
from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)


class Rating(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.IntegerField(
        default=0,
        blank=False,
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(10)
        ]
    )
    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"