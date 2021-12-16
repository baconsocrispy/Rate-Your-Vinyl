# Generated by Django 2.2.5 on 2021-12-16 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('pre-mix', 'pre-mix'), ('post-mix/pre-master', 'post-mix/pre-master'), ('post-master', 'post-master')], max_length=60)),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('genre', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
    ]
