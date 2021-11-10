# Generated by Django 2.2.5 on 2021-11-08 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection', models.CharField(choices=[('Song', 'Song'), ('Artist', 'Artist'), ('Album', 'Album')], max_length=50)),
                ('artist_name', models.CharField(blank=True, default='', max_length=50)),
                ('song_title', models.CharField(blank=True, default='', max_length=50)),
                ('album_title', models.CharField(blank=True, default='', max_length=50)),
                ('rank_this_week', models.IntegerField()),
            ],
        ),
    ]
