# Generated by Django 2.2.5 on 2021-07-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZooAnimals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='SSP',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=60),
        ),
    ]