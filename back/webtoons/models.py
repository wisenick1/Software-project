from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Webtoon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.TextField()
    story_author = models.TextField()
    image_author = models.TextField()
    type = models.TextField()
    genre = models.TextField()
    description = models.TextField()
    thumbnail = models.TextField()
    item_id = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'webtoon'
