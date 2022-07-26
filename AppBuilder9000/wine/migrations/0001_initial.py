# Generated by Django 2.2.5 on 2022-07-26 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Red', 'Red'), ('White', 'White'), ('Pink', 'Pink')], max_length=20)),
                ('varietal', models.CharField(choices=[('Chardonnay', 'Chardonnay'), ('Pinot Gris', 'Pinot Gris'), ('Riesling', 'Riesling'), ('Pinot Noir', 'Pinot Noir'), ('Cabernet Sauvignon', 'Cabernet Sauvignon'), ('Malbec', 'Malbec')], max_length=60)),
                ('region', models.CharField(choices=[('France', 'France'), ('Italy', 'Italy'), ('Spain', 'Spain'), ('Germany', 'Germany'), ('U.S.A', 'U.S.A'), ('Argentina', 'Argentina'), ('Chile', 'Chile')], max_length=60)),
            ],
        ),
    ]
