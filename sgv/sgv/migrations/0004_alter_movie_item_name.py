# Generated by Django 4.0.3 on 2023-06-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgv', '0003_delete_genre_remove_movie_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
    ]
