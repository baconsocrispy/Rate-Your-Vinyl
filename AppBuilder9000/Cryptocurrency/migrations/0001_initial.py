# Generated by Django 2.2.5 on 2022-07-12 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('crypto', models.CharField(max_length=50)),
                ('ticker', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=1000000)),
                ('body', models.TextField(max_length=1000)),
                ('rating', models.CharField(choices=[('Bullish', 'Bullish'), ('Bearish', 'Bearish'), ('Neutral', 'Neutral')], max_length=10)),
            ],
        ),
    ]
