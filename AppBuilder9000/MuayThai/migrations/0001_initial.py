# Generated by Django 2.2.5 on 2022-04-19 02:22

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Flyweight', 'Flyweight'), ('Bantamweight', 'Bantamweight'), ('Featherweight', 'Featherweight'), ('Welterweight', 'Welterweight'), ('Middleweight', 'Middleweight'), ('Heavyweight', 'Heavyweight')], default='Choose your weight class!', max_length=60)),
                ('first_name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
                ('country', models.CharField(blank=True, default='', max_length=60)),
                ('weight_in_lbs', models.CharField(blank=True, default='', max_length=20)),
                ('gym', models.CharField(blank=True, default='', max_length=60)),
            ],
            managers=[
                ('Fighter', django.db.models.manager.Manager()),
            ],
        ),
    ]
