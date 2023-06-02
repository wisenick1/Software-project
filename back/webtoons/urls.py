from django.urls import path
from .views import add_webtoon

urlpatterns = [
        path('movie/', add_webtoon)
]
