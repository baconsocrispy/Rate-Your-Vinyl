# Generated by Django 2.2.5 on 2022-01-14 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BestCities', '0009_auto_20220114_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='cost_of_living_average',
            field=models.CharField(choices=[('Below Average', 'Below Average'), ('Average', 'Average'), ('Above Average', 'Above Average')], max_length=60),
        ),
    ]
