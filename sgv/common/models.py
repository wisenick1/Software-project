from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add your custom fields here
    visit = models.BooleanField(default=False)
