# Generated by Django 2.2.5 on 2021-12-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNDCharacters', '0011_auto_20211221_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='Character_Class',
            field=models.CharField(choices=[('Druid', 'Driud'), ('Cleric', 'Cleric'), ('Warlock', 'Warlock'), ('Sorcerer', 'Sorcerer'), ('Fighter', 'Fighter'), ('Ranger', 'Ranger'), ('Barbarian', 'Barbarian'), ('Wizard', 'Wizard'), ('Bard', 'Bard')], max_length=60),
        ),
    ]
