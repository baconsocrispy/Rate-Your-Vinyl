# Generated by Django 2.2.5 on 2021-12-14 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ryder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(blank=True, default='', max_length=60)),
                ('Last_Name', models.CharField(blank=True, default='', max_length=60)),
                ('Style', models.CharField(blank=True, default='', max_length=60)),
                ('Sponsor', models.CharField(blank=True, default='', max_length=60)),
            ],
        ),
    ]
