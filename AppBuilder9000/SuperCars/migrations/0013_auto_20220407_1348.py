# Generated by Django 2.2.5 on 2022-04-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperCars', '0012_auto_20220407_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supercars',
            name='type',
            field=models.CharField(choices=[('Bugatti', 'Bugatti'), ('McClaren', 'McClaren'), ('Lambo', 'Lambo'), ('Ferrari', 'Ferrari')], max_length=60),
        ),
    ]
