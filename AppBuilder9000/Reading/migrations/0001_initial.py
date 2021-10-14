# Generated by Django 2.2.5 on 2021-10-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(blank=True, default='', max_length=60)),
                ('author', models.CharField(blank=True, default='', max_length=60)),
                ('number_of_pages_read', models.IntegerField()),
                ('description_of_passage_read', models.TextField(blank=True, default='', max_length=300)),
            ],
        ),
    ]
