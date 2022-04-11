# Generated by Django 2.2.5 on 2022-04-11 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewTrail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_name', models.CharField(max_length=60)),
                ('rider_name', models.CharField(blank=True, max_length=60)),
                ('nearest_city', models.CharField(blank=True, max_length=60)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NV', 'Nevada'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=60)),
                ('water_available', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Only with purifier', 'Only with purifier')], max_length=20)),
                ('review', models.TextField()),
                ('difficulty', models.CharField(choices=[('Easy', '1 - Easy'), ('Easy/Intermediate', '2 - Easy/Intermediate'), ('Intermediate', '3 - Intermediate'), ('Intermediate/Difficult', '4 - Intermediate/Difficult'), ('Difficult', '5 - Difficult'), ('Very Difficult', '6 - Very Difficult')], max_length=60)),
            ],
        ),
    ]
