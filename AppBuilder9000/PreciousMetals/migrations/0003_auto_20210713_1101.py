# Generated by Django 2.2.5 on 2021-07-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PreciousMetals', '0002_preciousmetalsitem_ounces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preciousmetalsitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]