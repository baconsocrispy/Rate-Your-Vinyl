# Generated by Django 2.2.5 on 2022-03-29 19:53

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Prowrestlers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='wrestler',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
