# Generated by Django 2.2.5 on 2022-05-10 03:55

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Child_Name', models.CharField(max_length=60)),
                ('Child_Grade', models.CharField(choices=[('2nd-3rd', '2nd-3rd'), ('6th-7th', '6th-7th'), ('4th-5th', '4th-5th'), ('K-1st', 'K-1st')], max_length=10)),
                ('Jersey_Number', models.IntegerField(default='0')),
                ('Parent_Name', models.CharField(max_length=60)),
                ('Parent_Phone', models.CharField(max_length=60)),
                ('Parent_Email', models.CharField(max_length=60)),
            ],
            managers=[
                ('Children', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Coach_Name', models.CharField(max_length=60)),
                ('Coach_Email', models.CharField(max_length=30)),
                ('Coach_Grade', models.CharField(choices=[('2nd-3rd', '2nd-3rd'), ('6th-7th', '6th-7th'), ('4th-5th', '4th-5th'), ('K-1st', 'K-1st')], max_length=10)),
            ],
            managers=[
                ('Coaches', django.db.models.manager.Manager()),
            ],
        ),
    ]
