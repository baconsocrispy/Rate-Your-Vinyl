# Generated by Django 2.2.5 on 2022-03-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutEquipment', '0004_auto_20220306_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutequipment',
            name='type',
            field=models.CharField(choices=[('Free weights', 'Free weights'), ('benches', 'benches'), ('stationary bikes', 'stationary bikes'), ('treadmills', 'treadmills')], max_length=60),
        ),
    ]
