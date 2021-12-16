# Generated by Django 2.2.5 on 2021-12-16 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotSprings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hot_springs_name', models.CharField(max_length=50)),
                ('hot_springs_type', models.CharField(choices=[('Outdoor', 'Outdoor'), ('Indoor', 'Indoor'), ('Both', 'Both')], max_length=60)),
                ('clothing_optional', models.CharField(choices=[('Required', 'Required'), ('Optional', 'Optional')], max_length=60)),
                ('stay_accommodations', models.CharField(choices=[('Tent Camping', 'Tent Camping'), ('Trailer Hookups', 'Trailer Hookups'), ('Cabin Rentals', 'Cabin Rentals'), ('Resort', 'Resort'), ('Camping & Rentals', 'Camping & Rentals'), ('No Overnight Stay', 'No Overnight Stay')], default='', max_length=60)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('hotsprings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='HotSprings.HotSprings')),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
            bases=('HotSprings.hotsprings',),
        ),
    ]
