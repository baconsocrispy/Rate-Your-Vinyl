# Generated by Django 2.2.5 on 2021-11-11 00:02

import CocktailRecipes.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cocktail_name', models.CharField(max_length=50, unique=True)),
                ('ingredient_1', CocktailRecipes.models.IngredientMultiModelField(blank=True)),
                ('ingredient_2', CocktailRecipes.models.IngredientMultiModelField(blank=True)),
                ('ingredient_3', CocktailRecipes.models.IngredientMultiModelField(blank=True)),
                ('ingredient_4', CocktailRecipes.models.IngredientMultiModelField(blank=True)),
                ('ingredient_5', CocktailRecipes.models.IngredientMultiModelField(blank=True)),
                ('ingredient_6', CocktailRecipes.models.IngredientMultiModelField(blank=True)),
                ('ingredient_7', CocktailRecipes.models.IngredientMultiModelField(blank=True)),
                ('ingredient_8', CocktailRecipes.models.IngredientMultiModelField(blank=True)),
                ('ingredient_9', CocktailRecipes.models.IngredientMultiModelField(blank=True)),
                ('description', models.TextField()),
                ('directions', models.TextField()),
                ('avg_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
            ],
            managers=[
                ('Cocktails', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('rating', models.PositiveSmallIntegerField()),
                ('comments', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CocktailRecipes.Cocktail')),
            ],
            managers=[
                ('Reviews', django.db.models.manager.Manager()),
            ],
        ),
    ]
