# Generated by Django 2.2.5 on 2022-07-26 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bucketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('April', 'April'), ('May', 'May'), ('January', 'January'), ('December', 'December'), ('August', 'August'), ('March', 'March'), ('October', 'October'), ('July', 'July'), ('November', 'November'), ('June', 'June'), ('February', 'February'), ('September', 'September')], max_length=30)),
                ('activity', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('required_items', models.CharField(max_length=30)),
            ],
        ),
    ]
