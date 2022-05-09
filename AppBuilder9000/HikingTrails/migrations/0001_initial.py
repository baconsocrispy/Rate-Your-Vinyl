# Generated by Django 2.2.5 on 2022-05-09 03:52

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_name', models.CharField(max_length=50)),
                ('distance', models.DecimalField(decimal_places=0, default='', max_digits=5)),
                ('state', models.CharField(max_length=50)),
            ],
            managers=[
                ('Trail', django.db.models.manager.Manager()),
            ],
        ),
    ]
