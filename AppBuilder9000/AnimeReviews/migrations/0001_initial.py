# Generated by Django 2.2.5 on 2021-11-19 01:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animeName', models.CharField(max_length=100)),
                ('numOfEpisodes', models.IntegerField()),
                ('studioName', models.CharField(max_length=50)),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('review', models.TextField(max_length=1500)),
            ],
        ),
    ]