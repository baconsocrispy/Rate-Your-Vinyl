# Generated by Django 2.2.5 on 2022-03-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personality', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=60),
        ),
    ]
