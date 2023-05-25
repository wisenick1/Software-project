from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('preference/', views.preference, name='preference'),
    path('recommend/', views.preference, name='recommend',),
    path('toggle-movie/<int:movie_id>/', views.toggle_movie, name='toggle_movie'),
    path('preference/toggle-movie/<int:movie_id>/', views.toggle_movie, name='toggle_movie'),
]