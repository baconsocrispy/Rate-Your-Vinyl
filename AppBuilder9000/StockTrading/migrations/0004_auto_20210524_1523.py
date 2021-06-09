# Generated by Django 2.2.5 on 2021-05-24 20:23

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('StockTrading', '0003_resources_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resources',
            new_name='Resource',
        ),
        migrations.RenameModel(
            old_name='Stories',
            new_name='Story',
        ),
        migrations.AlterModelManagers(
            name='resource',
            managers=[
                ('Resources', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='story',
            managers=[
                ('Stories', django.db.models.manager.Manager()),
            ],
        ),
    ]