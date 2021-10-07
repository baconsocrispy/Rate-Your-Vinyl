# Generated by Django 2.2.5 on 2021-10-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(help_text='Which country are we talking about?', max_length=200, null=True)),
                ('city', models.CharField(help_text='Which city are we talking about?', max_length=200)),
                ('timeZone', models.CharField(choices=[('5', 'Finland, Ukraine, Romania, Greece'), ('6', 'Belarus, Western Russia, Turkey'), ('7', 'Georgia, Azerbaijan')], help_text="Please select from the list, to convert it's time zone.", max_length=200)),
                ('safety', models.CharField(choices=[('not safe, do not visit', 'Not safe at all'), ('not safe', 'Not safe, would not bring family'), ('somewhat safe', 'Decently safe, just be careful and wise'), ('safer than others', 'No safety threats, but there are areas I would not go'), ('Extremely Safe', 'Really safe, my grandma would be ok')], help_text='Please choose a safety rating for this location.', max_length=200)),
                ('prices', models.CharField(choices=[('dirt cheap', 'Extremely cheap to visit'), ('somewhat cheap', 'Not the cheapest, but close'), ('average price', 'Average price'), ('somewhat decadent', 'A little lavish'), ('very decadent', 'Only for the high rollers')], help_text='Please consider the total price of the trip when rating', max_length=150)),
            ],
        ),
    ]
