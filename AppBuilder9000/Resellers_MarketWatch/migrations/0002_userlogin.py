# Generated by Django 2.2.5 on 2021-05-05 23:17

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Resellers_MarketWatch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
            ],
            managers=[
                ('User', django.db.models.manager.Manager()),
            ],
        ),
    ]
