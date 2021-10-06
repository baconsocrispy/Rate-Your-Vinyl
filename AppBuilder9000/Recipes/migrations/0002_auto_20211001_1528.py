# Generated by Django 2.2.5 on 2021-10-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('Lunch', 'Lunch'), ('Breakfast', 'Breakfast'), ('Dessert', 'Dessert'), ('Dinner', 'Dinner')], max_length=9),
        ),
    ]
