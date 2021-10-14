# Generated by Django 2.2.5 on 2021-10-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CultClassics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Genres', 'Genres'), ('Year', 'Year'), ('Director', 'Director'), ('Color', 'Color')], max_length=25)),
                ('user_name', models.CharField(blank=True, default='', max_length=25)),
                ('Movie_Title', models.CharField(blank=True, default='', max_length=25)),
                ('Actor', models.CharField(blank=True, default='', max_length=25)),
                ('Actress', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('Description', models.TextField(blank=True, default='', max_length=500)),
            ],
        ),
    ]
