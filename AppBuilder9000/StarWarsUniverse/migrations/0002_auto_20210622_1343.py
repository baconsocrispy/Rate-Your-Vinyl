# Generated by Django 2.2.5 on 2021-06-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StarWarsUniverse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='Affiliation',
            field=models.CharField(choices=[('dark', 'dark'), ('light', 'light'), ('neutral', 'neutral')], default='neutral', max_length=60),
        ),
    ]