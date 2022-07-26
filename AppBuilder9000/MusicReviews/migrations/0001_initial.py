# Generated by Django 2.2.5 on 2022-07-26 01:05

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_genre', models.CharField(choices=[('Blues', 'Blues'), ('Country', 'Country'), ('Easy Listening', 'Easy Listening '), ('Electronic', 'Electronic'), ('Hip hop', 'Hip hop'), ('Jazz', 'Jazz'), ('Pop', 'Pop'), ('R&B and Soul', 'R&B and Soul'), ('Rock', 'Rock'), ('Metal', 'Metal'), ('Punk', 'Punk'), ('African', 'African'), ('Eastern Europe', 'Eastern Europe'), ('Asian', 'Asian'), ('Middle Eastern', 'Middle Eastern'), ('Caribbean and Caribbean-influenced', 'Caribbean and Caribbean-influenced'), ('Latin', 'Latin'), ('Religious', 'Religious'), ('Traditional Folk', 'Traditional Folk'), ('Other', 'Other')], max_length=20)),
                ('music_title', models.CharField(max_length=100)),
                ('music_Composer', models.CharField(max_length=100)),
                ('music_description', models.CharField(max_length=100)),
                ('Music_RATING', models.CharField(choices=[('1/5', '1/5'), ('2/5', '2/5'), ('3/5', '3/5'), ('4/5', '4/5'), ('5/5', '5/5')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Composer', models.CharField(max_length=100)),
                ('Rating', models.CharField(max_length=100)),
                ('Source', models.CharField(max_length=100)),
            ],
            managers=[
                ('Favorite_Music', django.db.models.manager.Manager()),
            ],
        ),
    ]
