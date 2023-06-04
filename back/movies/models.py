from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item_name = models.TextField()
    genre1 = models.TextField()
    genre2 = models.TextField()
    description = models.TextField()

    class Meta:
        db_table = 'movie'
