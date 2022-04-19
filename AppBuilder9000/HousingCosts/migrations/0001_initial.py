# Generated by Django 2.2.5 on 2022-04-19 02:22

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=2)),
                ('bedrooms', models.PositiveSmallIntegerField()),
                ('bathrooms', models.PositiveSmallIntegerField()),
                ('squareFootage', models.PositiveIntegerField()),
                ('price', models.CharField(max_length=15)),
                ('notes', models.TextField(blank=True)),
            ],
            managers=[
                ('Homes', django.db.models.manager.Manager()),
            ],
        ),
    ]
