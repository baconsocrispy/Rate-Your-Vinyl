# Generated by Django 2.2.5 on 2022-01-13 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BestCities', '0002_auto_20220113_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='cost_of_living_average',
            field=models.CharField(choices=[('Above Average', 'Above Average'), ('Below Average', 'Below Average'), ('Average', 'Average')], max_length=60),
        ),
    ]
