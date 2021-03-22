# Generated by Django 2.2.5 on 2021-01-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Speedster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('green', models.CharField(choices=[('Electric', 'Electric'), ('Hybrid', 'Hybrid')], max_length=50)),
                ('year', models.IntegerField()),
                ('color', models.CharField(choices=[('Red', 'Red'), ('White', 'White'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('Black', 'Black')], max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]