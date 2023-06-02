from django.urls import path
from .view import add_movie

urlpatterns = [
        path('movie/', add_movies)
]
