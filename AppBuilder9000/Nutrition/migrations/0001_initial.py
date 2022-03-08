# Generated by Django 2.2.5 on 2022-03-07 22:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(130), django.core.validators.MinValueValidator(18)])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Prefer not to say', 'Prefer not to say')], default='', max_length=60)),
                ('email', models.EmailField(max_length=150)),
            ],
            managers=[
                ('Accounts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='NutritionixInfoReceived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.FloatField(null=True)),
                ('total_Fat', models.FloatField(null=True)),
                ('saturated_fat', models.FloatField(null=True)),
                ('cholesterol', models.FloatField(null=True)),
                ('sodium', models.FloatField(null=True)),
                ('total_carbohydrate', models.FloatField(null=True)),
                ('dietary_fiber', models.FloatField(null=True)),
                ('sugars', models.FloatField(null=True)),
                ('protein', models.FloatField(null=True)),
                ('potassium', models.FloatField(null=True)),
                ('search_query', models.CharField(max_length=250)),
            ],
            managers=[
                ('Queries', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalizedNutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(130), django.core.validators.MinValueValidator(18)])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Prefer not to say', 'Prefer not to say')], default='', max_length=60)),
                ('area_of_health', models.CharField(choices=[('Immune Health', 'Immune Health'), ('Energy and Focus', 'Energy and Focus'), ('Joint Health', 'Joint Health'), ('Cognition and Memory', 'Cognition and Memory'), ('Stress Relief', 'Stress Relief'), ('Sleep Hygiene', 'Sleep Hygiene'), ('Skin, Hair, and Nails', 'Skin, Hair, and Nails')], default='', max_length=100)),
                ('supplement_type', models.CharField(choices=[('Herbs', 'Herbs'), ('Vitamins', 'Vitamins'), ('Minerals', 'Minerals'), ('Phytonutrients', 'Phytonutrients'), ('Other', 'Other'), ('Any', 'Any')], default='', max_length=60)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nutrition.Account')),
            ],
            managers=[
                ('Personalized', django.db.models.manager.Manager()),
            ],
        ),
    ]
