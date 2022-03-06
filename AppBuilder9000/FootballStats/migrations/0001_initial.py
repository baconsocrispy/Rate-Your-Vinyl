# Generated by Django 2.2.5 on 2022-03-05 22:34

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('passing_yards', models.IntegerField(default='')),
                ('touchdowns', models.IntegerField(default='')),
                ('rushing_yards', models.IntegerField(default='')),
                ('receptions', models.IntegerField(default='')),
                ('tackles', models.IntegerField(default='')),
                ('sacks', models.IntegerField(default='')),
                ('interceptions', models.IntegerField(default='')),
            ],
            managers=[
                ('Player', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('passing_yards', models.IntegerField(default='')),
                ('touchdowns', models.IntegerField(default='')),
                ('rushing_yards', models.IntegerField(default='')),
                ('receptions', models.IntegerField(default='')),
                ('tackles', models.IntegerField(default='')),
                ('sacks', models.IntegerField(default='')),
                ('interceptions', models.IntegerField(default='')),
            ],
            managers=[
                ('Stat', django.db.models.manager.Manager()),
            ],
        ),
    ]
