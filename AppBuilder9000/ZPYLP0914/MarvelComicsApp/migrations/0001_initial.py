# Generated by Django 2.2.5 on 2020-12-07 18:38

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Character name')),
                ('hero_name', models.CharField(max_length=50, verbose_name='Hero Name')),
                ('dob', models.DateField(max_length=20, verbose_name='Date of Birth')),
                ('team', models.CharField(choices=[('The Avengers', 'The Avengers'), ('The X-Men', 'The X-Men'), ('Inhumans', 'Inhumans'), ('Fantastic 4', 'Fantastic 4'), ('Guardians of the Galaxy', 'Guardians of the Galaxy'), ('Other', 'Other')], default='', max_length=50, verbose_name='What super team are they affiliated with?')),
                ('preference', models.CharField(choices=[('Hero', 'Hero'), ('Villain', 'Villain'), ('Other', 'Other')], default='', max_length=10, verbose_name='Are they a hero or a villain?')),
                ('powers', models.CharField(max_length=100, verbose_name='Powers')),
                ('bio', models.TextField(verbose_name='Biography')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='Character name')),
                ('description', models.CharField(blank=True, default='', max_length=500, verbose_name='Description')),
                ('path', models.CharField(max_length=100, verbose_name='Path')),
                ('extension', models.CharField(default='', max_length=50, verbose_name='Extension')),
                ('api_id', models.CharField(default='', max_length=50, verbose_name='ID')),
                ('link', models.CharField(blank=True, default=True, max_length=150, verbose_name='Link')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
