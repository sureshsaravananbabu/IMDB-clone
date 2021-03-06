# Generated by Django 3.0.8 on 2020-07-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_auto_20200718_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='cast',
        ),
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(related_name='movies', to='movie.Cast'),
        ),
    ]
