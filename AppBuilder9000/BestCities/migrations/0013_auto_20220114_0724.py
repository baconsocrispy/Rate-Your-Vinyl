# Generated by Django 2.2.5 on 2022-01-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BestCities', '0012_auto_20220114_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='cost_of_living_average',
            field=models.CharField(choices=[('Above Average', 'Above Average'), ('Average', 'Average'), ('Below Average', 'Below Average')], max_length=60),
        ),
    ]
