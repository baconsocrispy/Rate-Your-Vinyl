# Generated by Django 2.2.5 on 2020-11-25 19:24

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('AstronomyApp', '0004_auto_20201124_2259'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='planet',
            managers=[
                ('planets', django.db.models.manager.Manager()),
            ],
        ),
    ]
