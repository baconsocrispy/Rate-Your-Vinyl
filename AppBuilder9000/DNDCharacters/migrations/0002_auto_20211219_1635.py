# Generated by Django 2.2.5 on 2021-12-19 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNDCharacters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='Character_Class',
            field=models.CharField(choices=[('Fighter', 'Fighter'), ('Ranger', 'Ranger'), ('Warlock', 'Warlock'), ('Barbarian', 'Barbarian'), ('Bard', 'Bard'), ('Druid', 'Driud'), ('Wizard', 'Wizard'), ('Sorcerer', 'Sorcerer'), ('Cleric', 'Cleric')], max_length=60),
        ),
    ]
