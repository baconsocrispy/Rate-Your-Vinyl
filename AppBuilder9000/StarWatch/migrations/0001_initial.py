# Generated by Django 2.2.5 on 2022-03-31 21:00

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='celestialObjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_name', models.CharField(default='Enter an object name', max_length=30)),
                ('object_nickName', models.CharField(default='Enter an object nickname name', max_length=30)),
                ('object_type', models.CharField(choices=[('Moon', 'Moon'), ('Planet', 'Planet'), ('Star', 'Star'), ('Other', 'Other'), ('Unknown', 'Unknown')], max_length=10)),
                ('object_description', models.TextField(default='Enter a description')),
                ('object_brightness', models.IntegerField(default='0')),
                ('object_direction', models.TextField(default='NNW')),
                ('object_latitude', models.IntegerField(default='45')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
