# Generated by Django 2.2.5 on 2021-01-05 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SteamInterestAppBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_title', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=20)),
                ('date_released', models.DateTimeField()),
                ('date_purchased', models.DateTimeField()),
                ('interest_level', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
    ]