# Generated by Django 2.2.5 on 2022-01-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BestCities', '0028_auto_20220115_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='cost_of_living_average',
            field=models.CharField(choices=[('Above Average', 'Above Average'), ('Below Average', 'Below Average'), ('Average', 'Average')], max_length=60),
        ),
    ]
