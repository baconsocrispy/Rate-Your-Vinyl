# Generated by Django 2.2.5 on 2022-04-05 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personality', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=60),
        ),
    ]
