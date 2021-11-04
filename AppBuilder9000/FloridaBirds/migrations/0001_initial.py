# Generated by Django 2.2.5 on 2021-11-04 14:26

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirdDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bird_name', models.CharField(max_length=30)),
                ('date_seen', models.DateField()),
                ('habitat', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
            managers=[
                ('BirdDescription', django.db.models.manager.Manager()),
            ],
        ),
    ]
