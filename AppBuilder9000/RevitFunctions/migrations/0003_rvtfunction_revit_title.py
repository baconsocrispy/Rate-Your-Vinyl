# Generated by Django 2.2.5 on 2021-09-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RevitFunctions', '0002_auto_20210929_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='rvtfunction',
            name='revit_title',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
    ]