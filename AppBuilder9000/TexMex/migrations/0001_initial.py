# Generated by Django 2.2.5 on 2022-07-26 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('desserts', 'desserts'), ('entrees', 'entrees'), ('soups', 'soups'), ('appetizers', 'appetizers'), ('beverages', 'beverages')], max_length=12)),
                ('name', models.CharField(blank=True, default='', max_length=60)),
                ('servings', models.IntegerField(default=0)),
                ('recipe', models.TextField(blank=True, default='', max_length=1000)),
                ('dateSubmitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
