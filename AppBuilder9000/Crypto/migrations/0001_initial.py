# Generated by Django 2.2.5 on 2022-06-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddCrypto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crypto_name', models.CharField(max_length=100)),
                ('ticker_symbol', models.CharField(max_length=100)),
                ('crypto_rating', models.CharField(choices=[('1/5', '1/5'), ('2/5', '2/5'), ('3/5', '3/5'), ('4/5', '4/5'), ('5/5', '5/5')], max_length=20)),
            ],
        ),
    ]
