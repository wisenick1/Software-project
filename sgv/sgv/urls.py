from django.urls import path

from . import views

app_name = 'sgv'

urlpatterns = [
    path('', views.index),
    path('preference/', views.preference, name='preference'),
    path('preference/choice/', views.preference_choice, name='preference_choice'),
    path('recommend/', views.preference, name='recommend'),
    path('preference/update_choice/<int:movie_id>/', views.update_choice, name='update_choice'),
    path('preference/<int:movie_id>/', views.preference, name='preference_detail'),
]