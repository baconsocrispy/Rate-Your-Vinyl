# Generated by Django 2.2.5 on 2021-02-19 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UpcomingConcertsApp', '0008_auto_20210219_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concert',
            old_name='date',
            new_name='concert_date',
        ),
    ]
