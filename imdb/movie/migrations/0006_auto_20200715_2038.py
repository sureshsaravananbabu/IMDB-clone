# Generated by Django 3.0.8 on 2020-07-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique_for_date='publish'),
        ),
    ]