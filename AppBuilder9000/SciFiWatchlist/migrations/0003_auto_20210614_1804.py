# Generated by Django 2.2.5 on 2021-06-14 22:04

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('SciFiWatchlist', '0002_auto_20210614_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FilmName', models.CharField(max_length=100)),
                ('ReleaseYear', models.IntegerField(blank=True)),
                ('StarNames', models.CharField(blank=True, max_length=100)),
                ('DirectorName', models.CharField(blank=True, max_length=60)),
                ('Viewed', models.BooleanField(blank=True, default=False)),
                ('Enjoyed', models.BooleanField(blank=True, default=False)),
                ('MovieSummary', models.TextField(blank=True)),
            ],
            managers=[
                ('Movies', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='Film',
        ),
    ]