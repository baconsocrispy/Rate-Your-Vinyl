# Generated by Django 2.2.5 on 2021-09-30 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0007_auto_20210930_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('Dinner', 'Dinner'), ('Breakfast', 'Breakfast'), ('Dessert', 'Dessert'), ('Lunch', 'Lunch')], max_length=9),
        ),
    ]
