# Generated by Django 2.2.5 on 2021-05-03 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrackApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='CHOICES',
        ),
        migrations.DeleteModel(
            name='TrackApp',
        ),
    ]
