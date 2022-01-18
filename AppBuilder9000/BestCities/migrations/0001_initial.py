# Generated by Django 2.2.5 on 2022-01-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, default='', max_length=30)),
                ('state', models.CharField(blank=True, default='', max_length=2)),
                ('state_cost_index', models.DecimalField(decimal_places=1, default=0.0, max_digits=1000)),
                ('cost_of_living_average', models.CharField(choices=[('Above Average', 'Above Average'), ('Below Average', 'Below Average'), ('Average', 'Average')], max_length=60)),
                ('description', models.TextField(blank=True, default='', max_length=300)),
            ],
        ),
    ]
