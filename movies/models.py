from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Movie(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    director = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name