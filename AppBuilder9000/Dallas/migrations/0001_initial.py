# Generated by Django 2.2.5 on 2022-05-17 17:13

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dallas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('fav_sports_team', models.CharField(choices=[('dallas cowboys', 'Dallas Cowboys'), ('dallas mavericks', 'Dallas Mavericks'), ('texas rangers', 'Texas Rangers'), ('dallas stars', 'Dallas Stars'), ('dallas wings', 'Dallas Wings'), ('fc dallas', 'FC Dallas')], default='Dallas Cowboys', max_length=50)),
                ('fav_activity', models.TextField(default='', max_length=150)),
            ],
            managers=[
                ('Dallas', django.db.models.manager.Manager()),
            ],
        ),
    ]
