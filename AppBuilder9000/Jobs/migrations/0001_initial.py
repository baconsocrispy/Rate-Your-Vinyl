# Generated by Django 2.2.5 on 2022-05-09 03:52

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=30)),
                ('receive_updates', models.BooleanField()),
            ],
            managers=[
                ('Accounts', django.db.models.manager.Manager()),
            ],
        ),
    ]
