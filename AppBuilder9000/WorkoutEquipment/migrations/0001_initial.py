# Generated by Django 2.2.5 on 2022-03-24 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('benches', 'benches'), ('treadmills', 'treadmills'), ('stationary bikes', 'stationary bikes'), ('Free weights', 'Free weights'), ('Mechanical weight set', 'Mechanical weight set'), ('Racks', 'Racks')], max_length=60)),
                ('name', models.CharField(blank=True, default='', max_length=60)),
                ('description', models.TextField(blank=True, default='', max_length=300)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
                ('image', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]