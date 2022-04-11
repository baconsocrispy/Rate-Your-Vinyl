# Generated by Django 2.2.5 on 2022-04-11 01:36

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=60)),
                ('o_average_score', models.FloatField(default=0, max_length=5)),
                ('c_average_score', models.FloatField(default=0, max_length=5)),
                ('e_average_score', models.FloatField(default=0, max_length=5)),
                ('a_average_score', models.FloatField(default=0, max_length=5)),
                ('n_average_score', models.FloatField(default=0, max_length=5)),
            ],
            managers=[
                ('Persons', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='SelectPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personality.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ComparedPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_percentile', models.IntegerField(blank=True, null=True)),
                ('c_percentile', models.IntegerField(blank=True, null=True)),
                ('e_percentile', models.IntegerField(blank=True, null=True)),
                ('a_percentile', models.IntegerField(blank=True, null=True)),
                ('n_percentile', models.IntegerField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personality.Person')),
            ],
            managers=[
                ('ComparedPersons', django.db.models.manager.Manager()),
            ],
        ),
    ]
