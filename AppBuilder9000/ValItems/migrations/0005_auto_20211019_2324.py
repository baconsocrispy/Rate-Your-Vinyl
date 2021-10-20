# Generated by Django 2.2.5 on 2021-10-20 06:24

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('ValItems', '0004_auto_20211016_2253'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='item',
            managers=[
                ('Items', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('MATERIALS', 'Materials'), ('TOOLS', 'Tools'), ('WEAPONS', 'Weapons'), ('ARMOR', 'Armor')], max_length=20),
        ),
    ]
