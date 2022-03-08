# Generated by Django 2.2.5 on 2022-03-07 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('defenses', models.IntegerField(default=0)),
                ('p4p_rank', models.IntegerField(default=0)),
                ('record', models.CharField(max_length=20)),
            ],
        ),
    ]
