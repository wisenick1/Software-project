from django.urls import path

from . import views

app_name = 'sgv'

urlpatterns = [
    path('', views.index),
    path('preference/', views.preference, name='preference'),
    path('preference/<int:movie_id>/toggle_choice/', views.toggle_choice, name='toggle_choice'),
    path('recommend/', views.preference, name='recommend'),
]