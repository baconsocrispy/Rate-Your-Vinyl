# Generated by Django 2.2.5 on 2021-04-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharacterApp', '0005_auto_20210428_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character_create',
            name='race',
            field=models.CharField(choices=[('Night Elf', 'Night Elf'), ('Human', 'Human'), ('Undead', 'Undead'), ('Troll', 'Troll'), ('Blood Elf', 'Blood Elf'), ('Gnome', 'Gnome'), ('Dranei', 'Dranei'), ('Orc', 'Orc')], max_length=60),
        ),
        migrations.AlterField(
            model_name='character_create',
            name='sex',
            field=models.CharField(choices=[('Other', 'Other'), ('Female', 'Female'), ('Male', 'Male')], max_length=60),
        ),
    ]
