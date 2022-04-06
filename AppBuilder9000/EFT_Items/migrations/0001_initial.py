# Generated by Django 2.2.5 on 2022-04-05 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EFTItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Barter', 'Barter'), ('Keys', 'Keys'), ('Gear', 'Gear'), ('Weapons', 'Weapons'), ('Provisions', 'Provisions'), ('Meds', 'Meds'), ('Others', 'Others')], max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('amount_required', models.IntegerField(blank=True, null=True)),
                ('hideout', models.CharField(blank=True, max_length=100)),
                ('quest', models.CharField(blank=True, max_length=100)),
                ('found_in_raid', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=5)),
            ],
        ),
    ]
