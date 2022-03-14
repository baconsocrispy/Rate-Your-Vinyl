# Generated by Django 2.2.5 on 2022-03-10 19:11

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, default='', max_length=4)),
                ('vehicle_make', models.CharField(blank=True, default='', max_length=50)),
                ('vehicle_model', models.CharField(default='', max_length=50)),
                ('vehicle_type', models.CharField(blank=True, default='', max_length=50)),
                ('cylinders', models.CharField(blank=True, default='', max_length=50)),
                ('horsepower', models.CharField(blank=True, default='', max_length=50)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
