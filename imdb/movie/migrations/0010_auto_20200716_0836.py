# Generated by Django 3.0.8 on 2020-07-16 03:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_movie_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 3, 6, 34, 920511, tzinfo=utc)),
        ),
    ]