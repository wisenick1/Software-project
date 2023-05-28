from django.urls import path

from . import views

app_name = 'sgv'

urlpatterns = [
    path('', views.index),
    path('preference/', views.preference, name='preference'),
    path('recommend/', views.preference, name='recommend'),
    path('update-movie-choice/', views.update_movie_choice, name='update-movie-choice'),
    path('preference/toggle-movie/<int:movie_id>/', views.toggle_movie, name='toggle_movie'),
]