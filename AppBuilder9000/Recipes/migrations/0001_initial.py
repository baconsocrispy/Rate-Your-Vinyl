<<<<<<< HEAD
# Generated by Django 2.2.5 on 2021-09-30 19:11
=======
# Generated by Django 2.2.5 on 2021-09-30 20:01
>>>>>>> jk-10105-createModel

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dessert', 'Dessert'), ('Dinner', 'Dinner')], max_length=9)),
                ('user_name', models.CharField(blank=True, default='', max_length=24)),
                ('recipe_name', models.CharField(blank=True, default='', max_length=24)),
                ('main_ingredient', models.CharField(blank=True, default='', max_length=14)),
                ('main_ingredient_2', models.CharField(blank=True, default='', max_length=14, null=True)),
                ('steps', models.TextField(blank=True, default='', max_length=400)),
            ],
        ),
    ]
