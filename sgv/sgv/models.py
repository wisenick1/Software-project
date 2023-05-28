from django.db import models

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    genre = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=150)
    choice = models.BooleanField(default=False)


    def __str__(self):
        return self.title

