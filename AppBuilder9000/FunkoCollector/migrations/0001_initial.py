# Generated by Django 2.2.5 on 2021-11-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FunkoPopName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('Regular', '4_inch'), ('Medium', '6_inch'), ('Jumbo', '10_inch')], max_length=7)),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('fandome', models.CharField(max_length=60)),
                ('chase', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], max_length=3, verbose_name='Chase')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
