# Generated by Django 2.2.5 on 2021-06-28 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StarWarsUniverse', '0004_auto_20210622_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='Additional_Details',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]