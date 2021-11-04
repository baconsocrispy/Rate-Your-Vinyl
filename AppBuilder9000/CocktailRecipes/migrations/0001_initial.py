# Generated by Django 2.2.5 on 2021-11-02 21:10

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
                ('ingredient_1', models.CharField(max_length=50)),
                ('quantity_1', models.DecimalField(decimal_places=1, max_digits=3)),
                ('unit_1', models.CharField(max_length=15)),
                ('ingredient_2', models.CharField(blank=True, max_length=50)),
                ('quantity_2', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('unit_2', models.CharField(blank=True, max_length=15)),
                ('ingredient_3', models.CharField(blank=True, max_length=50)),
                ('quantity_3', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('unit_3', models.CharField(blank=True, max_length=15)),
                ('ingredient_4', models.CharField(blank=True, max_length=50)),
                ('quantity_4', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('unit_4', models.CharField(blank=True, max_length=15)),
                ('ingredient_5', models.CharField(blank=True, max_length=50)),
                ('quantity_5', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('unit_5', models.CharField(blank=True, max_length=15)),
                ('ingredient_6', models.CharField(blank=True, max_length=50)),
                ('quantity_6', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('unit_6', models.CharField(blank=True, max_length=15)),
                ('ingredient_7', models.CharField(blank=True, max_length=50)),
                ('quantity_7', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('unit_7', models.CharField(blank=True, max_length=15)),
                ('ingredient_8', models.CharField(blank=True, max_length=50)),
                ('quantity_8', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('unit_8', models.CharField(blank=True, max_length=15)),
                ('ingredient_9', models.CharField(blank=True, max_length=50)),
                ('quantity_9', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('unit_9', models.CharField(blank=True, max_length=15)),
                ('ingredient_10', models.CharField(blank=True, max_length=50)),
                ('quantity_10', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('unit_10', models.CharField(blank=True, max_length=15)),
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
