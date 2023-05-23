# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import AbstractUser, User
# from django.db import models

# class UserForm(UserCreationForm):
#     # 최초 방문여부
#     visit = models.BooleanField(default=False)
#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2")

# class User(AbstractUser):
#     visit = models.BooleanField(default=False)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

