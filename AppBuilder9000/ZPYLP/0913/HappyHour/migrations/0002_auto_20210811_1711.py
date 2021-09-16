# Generated by Django 2.2.5 on 2021-08-12 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HappyHour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='highlights',
            field=models.CharField(choices=[('good food', 'good food'), ('good drinks', 'good drinks'), ('stiff pour', 'stiff pour'), ('budget friendly', 'budget friendly'), ('late night HH', 'late night HH'), ('dietary options', 'dietary options'), ('ambiance', 'ambiance'), ('location', 'location')], max_length=50),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='rating',
            field=models.CharField(choices=[('one star', 'one star'), ('two star', 'two star'), ('three star', 'three star'), ('four star', 'four star'), ('five star', 'five star')], max_length=50),
        ),
    ]