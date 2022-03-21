# Generated by Django 2.2.5 on 2022-03-21 17:10

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Snack', 'Snack'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Sunday Meal', 'Sunday Meal'), ('Sweets', 'Sweets')], default='Pick from the dropdown!', max_length=20)),
                ('name', models.CharField(default='What did Grandma Call it?', max_length=40)),
                ('prep_time', models.CharField(default='60 minutes', max_length=30)),
                ('grandma_story', models.TextField(default='Recall a time you made this with Grandma! Tell everyone about it... ')),
                ('ingredients', models.TextField(default='list, ingredients, separated, by, commas')),
                ('instructions', models.TextField(default='Remember How Grandma Used to Do it? Tell about it!')),
            ],
            managers=[
                ('Recipes', django.db.models.manager.Manager()),
            ],
        ),
    ]
