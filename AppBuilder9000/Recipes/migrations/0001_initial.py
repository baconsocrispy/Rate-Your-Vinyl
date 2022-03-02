# Generated by Django 2.2.5 on 2022-03-02 16:53

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
                ('recipe_name', models.CharField(default='Enter recipe name', max_length=30)),
                ('recipe_description', models.TextField(default='Enter a brief description')),
                ('cook_time', models.IntegerField(default='60')),
                ('ingredients', models.TextField(default='list, ingredients, separated, by, commas')),
                ('instructions', models.TextField(default='1.\n\n2.\n\n3.')),
            ],
            managers=[
                ('Recipe', django.db.models.manager.Manager()),
            ],
        ),
    ]
