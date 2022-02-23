# Generated by Django 2.2.5 on 2022-02-22 23:31

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='vehicles',
            managers=[
                ('Vehicle', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='vehicles',
            name='cylinders',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='vehicles',
            name='horsepower',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
