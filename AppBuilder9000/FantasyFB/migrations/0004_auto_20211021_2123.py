# Generated by Django 2.2.5 on 2021-10-22 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FantasyFB', '0003_auto_20211021_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='reason',
            field=models.TextField(default='', max_length=100),
        ),
    ]
