# Generated by Django 2.2.5 on 2022-05-03 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('type', models.CharField(choices=[('ANI', 'Anime'), ('BOOK', 'Book'), ('CMC', 'Comic'), ('FILM', 'Movie'), ('TV', 'Television Series'), ('VG', 'Video Game'), ('OTH', 'Other')], max_length=20)),
                ('creator', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default='')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('NB', 'Non-Binary'), ('O', 'Other')], max_length=15)),
                ('species', models.CharField(max_length=50)),
                ('skill', models.CharField(max_length=100)),
                ('alignment', models.CharField(blank=True, choices=[('Lawful Good', 'Lawful Good'), ('Neutral Good', 'Neutral Good'), ('Chaotic Good', 'Chaotic Good'), ('Lawful Neutral', 'Lawful Neutral'), ('True Neutral', 'True Neutral'), ('Chaotic Neutral', 'Chaotic Neutral'), ('Lawful Evil', 'Lawful Evil'), ('Neutral Evil', 'Neutral Evil'), ('Chaotic Evil', 'Chaotic Evil')], max_length=19, null=True)),
                ('notes', models.CharField(blank=True, max_length=500, null=True)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FictionalCharacters.Series')),
            ],
        ),
    ]
