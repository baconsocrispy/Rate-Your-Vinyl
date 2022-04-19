# Generated by Django 2.2.5 on 2022-04-19 02:22

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Driver_Race_Key', models.CharField(default='', max_length=100, unique=True)),
                ('Driver_Name', models.CharField(choices=[('', 'Select a Driver'), ('Alex Albon', 'Alex Albon'), ('Fernando Alonso', 'Fernando Alonso'), ('Valterri Bottas', 'Valterri Bottas'), ('Pierre Gasly', 'Pierre Gasly'), ('Lewis Hamilton', 'Lewis Hamilton'), ('Nicholas Latifi', 'Nicholas Latifi'), ('Charles Leclerc', 'Charles Leclerc'), ('Kevin Magnussen', 'Kevin Magnussen'), ('Lando Norris', 'Lando Norris'), ('Esteban Ocon', 'Esteban Ocon'), ('Sergio Perez', 'Sergio Perez'), ('Daniel Ricciardo', 'Daniel Ricciardo'), ('George Russell', 'George Russell'), ('Carlos Sainz', 'Carlos Sainz'), ('Mick Schumacher', 'Mick Schumacher'), ('Lance Stroll', 'Lance Stroll'), ('Yuki Tsunoda', 'Yuki Tsunoda'), ('Max Verstappen', 'Max Verstappen'), ('Sebastian Vettel', 'Sebastian Vettel'), ('Zhou Guanyu', 'Zhou Guanyu')], default='', max_length=30)),
                ('Current_Team', models.CharField(choices=[('', 'Select a Team'), ('Alfa Romeo', 'Alfa Romeo'), ('Alpha Tauri', 'Alpha Tauri'), ('Alpine', 'Alpine'), ('Aston Martin', 'Aston Martin'), ('Ferrari', 'Ferrari'), ('Haas', 'Haas'), ('McLaren', 'McLaren'), ('Mercedes', 'Mercedes'), ('Red Bull', 'Red Bull'), ('Williams', 'Williams')], default='', max_length=30)),
                ('Race', models.CharField(choices=[('', 'Select a Race'), ('Bahrain', 'Bahrain'), ('Saudi Arabia', 'Saudi Arabia'), ('Australia', 'Australia'), ('Imola', 'Imola'), ('Miami', 'Miami'), ('Barcelona', 'Barcelona'), ('Monaco', 'Monaco'), ('Azerbaijan', 'Azerbaijan'), ('Canada', 'Canada'), ('Silverstone', 'Silverstone'), ('Austria', 'Austria'), ('France', 'France'), ('Hungary', 'Hungary'), ('Spa-Francorchamps', 'Spa-Francorchamps'), ('Zandvoort', 'Zandvoort'), ('Monza', 'Monza'), ('Singapore', 'Singapore'), ('Japan', 'Japan'), ('COTA', 'COTA'), ('Mexico', 'Mexico'), ('Brazil', 'Brazil'), ('Abu Dhabi', 'Abu Dhabi')], default='', max_length=50)),
                ('Race_Type', models.CharField(choices=[('Sprint Race', 'Sprint Race'), ('Feature Race', 'Feature Race')], default='Feature Race', max_length=15)),
                ('Finishing_Position', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('DNF', 'DNF')], default='', max_length=5)),
                ('Fastest_Lap', models.BooleanField()),
                ('Points_Earned', models.DecimalField(decimal_places=0, default='', max_digits=2)),
            ],
            managers=[
                ('results', django.db.models.manager.Manager()),
            ],
        ),
    ]
