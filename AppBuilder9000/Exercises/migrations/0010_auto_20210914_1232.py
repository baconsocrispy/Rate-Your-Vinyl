# Generated by Django 2.2.5 on 2021-09-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0009_auto_20210914_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='repetitions',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exercises',
            name='sets',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exercises',
            name='target_muscle',
            field=models.CharField(choices=[('Legs', 'Legs'), ('Chest', 'Chest'), ('Shoulders', 'Shoulders'), ('Back', 'Back'), ('Arms', 'Arms')], max_length=60),
        ),
    ]
