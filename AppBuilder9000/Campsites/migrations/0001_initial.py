# Generated by Django 2.2.5 on 2021-12-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampSites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Campsites', 'Campsites'), ('RVs', 'RVs'), ('Both', 'Both')], max_length=60)),
                ('site_amenities', models.CharField(choices=[('Pets Allow', 'Pets Allow'), ('Toilets', 'Toilets'), ('Campfires', 'Campfires'), ('Water', 'Water'), ('Showers', 'Showers'), ('Picnic Tables', 'Picnic Tables'), ('Wifi', 'Wifi')], default='', max_length=60)),
                ('site_activities', models.CharField(choices=[('Hiking', 'Hiking'), ('Swimming', 'Swimming'), ('Fishing', 'Fishing'), ('Biking', 'Biking'), ('Off-Roading', 'Off-Roading'), ('Wildlife Watching', 'Wildlife Watching')], default='', max_length=60)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
                ('city', models.CharField(blank=True, default='', max_length=500)),
                ('state', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
    ]
