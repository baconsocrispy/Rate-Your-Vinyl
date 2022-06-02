# Generated by Django 2.2.5 on 2022-06-02 10:03

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResortListings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort_name', models.CharField(max_length=100)),
                ('resort_type', models.CharField(choices=[('Adult-Only', 'Adult-Only'), ('Family', 'Family')], max_length=50)),
                ('resort_country', models.CharField(max_length=100)),
                ('resort_rating', models.CharField(choices=[('1 Star', '1 Star'), ('2 Stars', '2 Stars'), ('3 Stars', '3 Stars'), ('4 Stars', '4 Stars'), ('5 Stars', '5 Stars')], max_length=20)),
                ('resort_description', models.CharField(max_length=500)),
            ],
            managers=[
                ('Resorts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ResortTraveler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traveler_name', models.CharField(max_length=100)),
                ('traveler_party_size', models.CharField(max_length=2)),
                ('traveler_resort', models.CharField(max_length=100)),
                ('traveler_contact', models.CharField(max_length=50)),
            ],
        ),
    ]
