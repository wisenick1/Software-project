# Generated by Django 4.0.3 on 2023-05-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='choice',
            field=models.BooleanField(default=False),
        ),
    ]
