from django.urls import path
from .view import add_webtoon

urlpatterns = [
        path('movies/', add_webtoons)
]
