# Generated by Django 2.2.5 on 2022-01-15 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BestCities', '0035_auto_20220115_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='cost_of_living_average',
            field=models.CharField(choices=[('Below Average', 'Below Average'), ('Above Average', 'Above Average'), ('Average', 'Average')], max_length=60),
        ),
    ]
