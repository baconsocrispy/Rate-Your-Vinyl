# Generated by Django 2.2.5 on 2022-03-07 22:48

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('number', models.PositiveSmallIntegerField(default=1)),
                ('position', models.CharField(max_length=2)),
            ],
            managers=[
                ('FavPlayer', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('favorite_team', models.CharField(choices=[('Anaheim Ducks', 'Anaheim Ducks'), ('Arizona Coyotes', 'Arizona Coyotes'), ('Boston Bruins', 'Boston Bruins'), ('Buffalo Sabres', 'Buffalo Sabres'), ('Calgary Flames', 'Calgary Flames'), ('Carolina Hurricanes', 'Carolina Hurricanes'), ('Colorado Avalanche', 'Colorado Avalanche'), ('Columbus Blue Jackets', 'Columbus Blue Jackets'), ('Dallas Stars', 'Dallas Stars'), ('Detroit Red Wings', 'Detroit Red Wings'), ('Edmonton Oilers', 'Edmonton Oilers'), ('Florida Panthers', 'Florida Panthers'), ('Los Angeles Kings', 'Los Angeles Kings'), ('Minnesota Wild', 'Minnesota Wild'), ('Montreal Canadiens', 'Montreal Canadiens'), ('Nashville Predators', 'Nashville Predators'), ('New Jersey Devils', 'New Jersey Devils'), ('New York Rangers', 'New York Rangers'), ('New York Islanders', 'New York Islanders'), ('Ottawa Senators', 'Ottawa Senators'), ('Philadelphia Flyers', 'Philadelphia Flyers'), ('Pittsburgh Penguins', 'Pittsburgh Penguins'), ('San Jose Sharks', 'San Jose Sharks'), ('Seattle Kraken', 'Seattle Kraken'), ('St. Louis Blues', 'St. Louis Blues'), ('Tampa Bay Lightning', 'Tampa Bay Lightning'), ('Toronto Maple Leafs', 'Toronto Maple Leafs'), ('Vancouver Canucks', 'Vancouver Canucks'), ('Vegas Golden Knights', 'Vegas Golden Knights'), ('Washington Capitals', 'Washington Capitals'), ('Winnipeg Jets', 'Winnipeg Jets')], max_length=30)),
                ('favorite_player', models.CharField(max_length=50)),
                ('favorite_player_list', models.ManyToManyField(blank=True, default=None, related_name='favorite', to='IceHockey.FavPlayer')),
            ],
            managers=[
                ('Profile', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='favplayer',
            name='my_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IceHockey.Profile'),
        ),
        migrations.AlterUniqueTogether(
            name='favplayer',
            unique_together={('my_profile', 'name')},
        ),
    ]
