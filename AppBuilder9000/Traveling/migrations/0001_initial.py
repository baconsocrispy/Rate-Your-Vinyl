# Generated by Django 2.2.5 on 2022-03-24 00:29

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
            ],
            managers=[
                ('places', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
            managers=[
                ('travelers', django.db.models.manager.Manager()),
            ],
        ),
    ]
