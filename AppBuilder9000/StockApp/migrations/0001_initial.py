# Generated by Django 2.2.5 on 2021-04-16 18:53

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('market_cap', models.CharField(max_length=30)),
                ('time_stamp', models.TimeField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            managers=[
                ('Stock', django.db.models.manager.Manager()),
            ],
        ),
    ]
