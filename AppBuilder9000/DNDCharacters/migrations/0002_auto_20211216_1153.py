# Generated by Django 2.2.5 on 2021-12-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNDCharacters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='Character_Class',
            field=models.CharField(choices=[('Wizard', 'Wizard'), ('Sorcerer', 'Sorcerer'), ('Cleric', 'Cleric'), ('Barbarian', 'Barbarian'), ('Druid', 'Driud'), ('Bard', 'Bard'), ('Fighter', 'Fighter'), ('Ranger', 'Ranger'), ('Warlock', 'Warlock')], max_length=60),
        ),
    ]
