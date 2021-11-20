# Generated by Django 2.2.5 on 2021-11-18 04:12

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('team', models.CharField(choices=[('Marvel', 'Marvel'), ('DC', 'DC')], max_length=6)),
                ('position', models.CharField(choices=[('QB', 'Quarterback'), ('RB', 'Running Back'), ('FB', 'Full Back'), ('WR', 'Wide Receiver'), ('TE', 'Tight End'), ('DL', 'Defensive Lineman'), ('LB', 'Linebacker'), ('S', 'Safety'), ('CB', 'Cornerback'), ('K', 'Kicker'), ('C', 'Coach')], max_length=2)),
                ('reason', models.TextField(default='', max_length=500)),
            ],
            managers=[
                ('Players', django.db.models.manager.Manager()),
            ],
        ),
    ]
