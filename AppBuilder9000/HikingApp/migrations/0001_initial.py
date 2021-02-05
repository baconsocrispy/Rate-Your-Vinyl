# Generated by Django 2.2.5 on 2020-12-15 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('location', models.CharField(choices=[('South Dakota', 'South Dakota'), ('Pennsylvania', 'Pennsylvania'), ('Virgina', 'Virgina'), ('Mississippi', 'Mississippi'), ('Montana', 'Montana'), ('South Carolina', 'South Carolina'), ('Washington', 'Washington'), ('North Dakota', 'North Dakota'), ('West Virginia', 'West Virginia'), ('Minnesota', 'Minnesota'), ('Arkansas', 'Arkansas'), ('Idaho', 'Idaho'), ('Florida', 'Florida'), ('Illinois', 'Illinois'), ('Massachusetts', 'Massachusetts'), ('Connecticut', 'Connecticut'), ('Missouri', 'Missouri'), ('New Mexico', 'New Mexico'), ('Vermont', 'Vermont'), ('Nevada', 'Nevada'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('New Hampshire', 'New Hampshire'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Maryland', 'Maryland'), ('Rhode Island', 'Rhode Island'), ('Oregon', 'Oregon'), ('Texas', 'Texas'), ('New York', 'New York'), ('Tennessee', 'Tennessee'), ('Delaware', 'Delaware'), ('Georgia', 'Georgia'), ('Kentucky', 'Kentucky'), ('Indiana', 'Indiana'), ('Alabama', 'Alabama'), ('Wyoming', 'Wyoming'), ('Michigan', 'Michigan'), ('Nebraska', 'Nebraska'), ('California', 'California'), ('Hawaii', 'Hawaii'), ('Maine', 'Maine'), ('North Carolina', 'North Carolina'), ('New Jersey', 'New Jersey'), ('Louisiana', 'Louisiana'), ('Ohio', 'Ohio'), ('Wisconsin', 'Wisconsin'), ('Colorado', 'Colorado'), ('Utah', 'Utah'), ('Oklahoma', 'Oklahoma')], max_length=60)),
                ('difficulty', models.CharField(choices=[('Hard', 'Hard'), ('Easy', 'Easy'), ('Medium', 'Medium')], max_length=60)),
                ('length', models.CharField(blank=True, default='', max_length=50)),
                ('camping', models.NullBooleanField(default=False)),
                ('image', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]
