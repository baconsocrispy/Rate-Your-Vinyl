# Generated by Django 2.2.5 on 2021-10-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreItemManagement', '0004_auto_20211016_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_contact',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
