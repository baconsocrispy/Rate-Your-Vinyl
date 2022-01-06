# Generated by Django 2.2.5 on 2022-01-06 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('username', models.CharField(default='', max_length=60)),
                ('email', models.EmailField(default='', max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Goal_Type', models.CharField(choices=[('skill', 'Gain New Skill'), ('improve', 'Improve Existing Skill'), ('break', 'Break Bad Habit'), ('unsure', 'Not Sure')], max_length=25)),
                ('Goal_Name', models.CharField(default='', max_length=100)),
                ('Goal_Description', models.TextField(default='', max_length=300)),
                ('Reason', models.TextField(default='', max_length=350)),
                ('Target_Range', models.CharField(choices=[('2wks', 'By 2-Weeks'), ('1mo', 'By 1-Month'), ('6wks', 'By 6-Weeks'), ('2mo', 'By 2-Months'), ('3mo', 'By 3-Months'), ('6mo', 'By 6-Months')], default='', max_length=20)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='StudyApp.Register')),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Daily_Hours_Spent', models.CharField(choices=[('lt1', '<1'), ('1to3', '1-3'), ('4to6', '4-6'), ('gt6', '6+')], default='', max_length=5)),
                ('Task_Completed', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('Entry_Date', models.DateTimeField(auto_now=True)),
                ('Entry', models.TextField(max_length=400)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='StudyApp.Register')),
            ],
        ),
    ]
