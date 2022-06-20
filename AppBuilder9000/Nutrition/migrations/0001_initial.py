# Generated by Django 2.2.5 on 2022-06-20 17:34

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=40)),
                ('Age', models.IntegerField(default='')),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=40)),
                ('Height', models.IntegerField(default='')),
                ('Weight', models.IntegerField(default='')),
                ('BMI', models.FloatField()),
                ('FatPercent', models.FloatField()),
                ('Phase', models.CharField(max_length=40)),
                ('Calories', models.IntegerField(default='')),
                ('Protein', models.IntegerField(default='')),
            ],
            managers=[
                ('Users', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ChooseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nutrition.User')),
            ],
        ),
    ]
