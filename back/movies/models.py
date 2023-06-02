from django.db import models

# Create your models here.

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.TextField()
    genre1 = models.TextField()
    genre2 = models.TextField()
    description = models.TextField()

    class Meta:
        db_table = 'movies'
