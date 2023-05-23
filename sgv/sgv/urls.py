from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('preference/', views.preference, name='preference'),
    path('recommend/', views.preference, name='recommend',),
]