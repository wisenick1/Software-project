from django.urls import path
from .view import add_webtoon

urlpatterns = [
        path('movie/', add_webtoons)
]
