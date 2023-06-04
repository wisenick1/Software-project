from django.db import models


# from sgv.common.models import CustomUser

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    genre1 = models.TextField(default='')
    genre2 = models.TextField(default='')
    item_name = models.CharField(max_length=100)  # title
    choice = models.BooleanField(default=False)
    description = models.TextField(default='')
    image_url = models.TextField(default='')

    class Meta:
        db_table = 'movies'
