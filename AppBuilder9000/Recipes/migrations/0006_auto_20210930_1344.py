# Generated by Django 2.2.5 on 2021-09-30 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0005_auto_20210930_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Dessert', 'Dessert'), ('Dinner', 'Dinner'), ('Lunch', 'Lunch')], max_length=9),
        ),
    ]
