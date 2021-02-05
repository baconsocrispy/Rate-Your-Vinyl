# Generated by Django 2.2.5 on 2020-09-04 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SendItApp', '0006_auto_20200903_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='status',
            field=models.CharField(choices=[('ToDo', 'To Do'), ('Pinkpoint', 'Pinkpoint'), ('Onsight', 'Onsight'), ('Flail', 'Flail'), ('Flash', 'Flash'), ('Redpoint', 'Redpoint'), ('Blackpoint', 'Blackpoint')], max_length=40),
        ),
        migrations.AlterField(
            model_name='route',
            name='type',
            field=models.CharField(choices=[('Trad', 'Trad'), ('Sport', 'Sport'), ('Alpine', 'Alpine'), ('Ice', 'Ice'), ('Boulder', 'Boulder')], max_length=40),
        ),
    ]
