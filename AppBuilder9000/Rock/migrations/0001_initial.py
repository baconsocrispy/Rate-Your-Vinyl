# Generated by Django 2.2.5 on 2021-12-08 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HardRock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Band', models.CharField(max_length=60)),
                ('member', models.CharField(max_length=60)),
                ('Genre', models.CharField(max_length=60)),
                ('Instrument', models.CharField(max_length=60)),
            ],
        ),
    ]
