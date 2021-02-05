# Generated by Django 2.2.5 on 2020-11-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('TE', 'TE'), ('QB', 'QB'), ('OL', 'OL'), ('DB', 'DB'), ('LB', 'LB'), ('WR', 'WR'), ('DL', 'DL'), ('RB', 'RB')], max_length=2)),
                ('name', models.CharField(default='', max_length=60)),
                ('height', models.PositiveIntegerField(max_length=3)),
                ('weight', models.PositiveIntegerField(max_length=3)),
                ('team', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
