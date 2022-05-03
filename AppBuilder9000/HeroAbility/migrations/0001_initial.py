# Generated by Django 2.2.5 on 2022-05-03 04:11

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(default='', max_length=30)),
                ('secret_Identity', models.CharField(blank=True, default='', max_length=50)),
                ('ability_Name', models.CharField(default='', max_length=25)),
                ('ability_Summary', models.TextField(default='', max_length=200)),
                ('weakness', models.CharField(blank=True, default='', max_length=25)),
                ('threat_Level', models.CharField(choices=[('Nonexistent', 'Nonexistent'), ('Mild Inconvenience', 'Mild Inconvenience'), ('Minor Threat', 'Minor Threat'), ('Robin Equivalent', 'Robin Equivalent'), ('Major Threat', 'Major Threat'), ('World Ending', 'World Ending')], default='', max_length=20)),
            ],
            managers=[
                ('heroes', django.db.models.manager.Manager()),
            ],
        ),
    ]
