# Generated by Django 2.2.5 on 2022-03-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personality', '0002_auto_20220311_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=60),
        ),
    ]
