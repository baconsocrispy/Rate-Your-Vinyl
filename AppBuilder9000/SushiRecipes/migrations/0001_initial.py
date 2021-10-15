# Generated by Django 2.2.5 on 2021-10-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SushiRecipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=60)),
                ('ingredients', models.CharField(max_length=100)),
                ('steps', models.TextField(max_length=200)),
                ('notes', models.CharField(max_length=100)),
            ],
        ),
    ]
