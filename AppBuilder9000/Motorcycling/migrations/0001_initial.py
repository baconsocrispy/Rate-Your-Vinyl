# Generated by Django 2.2.5 on 2022-03-31 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motorcycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TYPE_MOTORCYCLE', models.CharField(blank=True, choices=[('Sport', 'Sport'), ('Cruiser', 'Cruiser'), ('Touring', 'Touring'), ('Adventure', 'Adventure'), ('Standard', 'Standard')], default='', max_length=20)),
                ('BRAND_MOTORCYCLE', models.CharField(blank=True, choices=[('BMW', 'BMW'), ('Harley Davidson', 'Harley Davidson'), ('Kawasaki', 'Kawasaki'), ('Honda', 'Honda'), ('Yamaha', 'Yamaha'), ('Triumph', 'Triumph'), ('Ducati', 'Ducati'), ('Indian', 'Indian'), ('Victory', 'Victory'), ('KTM', 'KTM')], default='', max_length=20)),
                ('ENGINE_SIZE', models.CharField(blank=True, default='', max_length=10)),
                ('MODEL_TYPE', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('RATING', models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('START_DESTINATION', models.CharField(default='', max_length=50)),
                ('END_DESTINATION', models.CharField(default='', max_length=50)),
                ('RATING', models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1)),
            ],
        ),
    ]
