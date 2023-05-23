from django.urls import path
from .view import add_movie

urlpatterns = [
        path('movies/', add_movies)
]
