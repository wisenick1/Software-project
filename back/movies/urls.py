from django.urls import path
from .views import add_movie

urlpatterns = [
        path('movie/', add_movie)
]
