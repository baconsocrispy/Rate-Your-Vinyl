from django.db import models


# Create your models here.
class Profile(models.Model):
    TEAM_OPTIONS = (
        ('Anaheim Ducks', 'Anaheim Ducks'),
        ('Arizona Coyotes', 'Arizona Coyotes'),
        ('Boston Bruins', 'Boston Bruins'),
        ('Buffalo Sabres', 'Buffalo Sabres'),
        ('Calgary Flames', 'Calgary Flames'),
        ('Carolina Hurricanes', 'Carolina Hurricanes'),
        ('Colorado Avalanche', 'Colorado Avalanche'),
        ('Columbus Blue Jackets', 'Columbus Blue Jackets'),
        ('Dallas Stars', 'Dallas Stars'),
        ('Detroit Red Wings', 'Detroit Red Wings'),
        ('Edmonton Oilers', 'Edmonton Oilers'),
        ('Florida Panthers', 'Florida Panthers'),
        ('Los Angeles Kings', 'Los Angeles Kings'),
        ('Minnesota Wild', 'Minnesota Wild'),
        ('Montreal Canadiens', 'Montreal Canadiens'),
        ('Nashville Predators', 'Nashville Predators'),
        ('New Jersey Devils', 'New Jersey Devils'),
        ('New York Rangers', 'New York Rangers'),
        ('New York Islanders', 'New York Islanders'),
        ('Ottawa Senators', 'Ottawa Senators'),
        ('Philadelphia Flyers', 'Philadelphia Flyers'),
        ('Pittsburgh Penguins', 'Pittsburgh Penguins'),
        ('San Jose Sharks', 'San Jose Sharks'),
        ('Seattle Kraken', 'Seattle Kraken'),
        ('St. Louis Blues', 'St. Louis Blues'),
        ('Tampa Bay Lightning', 'Tampa Bay Lightning'),
        ('Toronto Maple Leafs', 'Toronto Maple Leafs'),
        ('Vancouver Canucks', 'Vancouver Canucks'),
        ('Vegas Golden Knights', 'Vegas Golden Knights'),
        ('Washington Capitals', 'Washington Capitals'),
        ('Winnipeg Jets', 'Winnipeg Jets'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    favorite_team = models.CharField(max_length=30, choices=TEAM_OPTIONS)
    favorite_player = models.CharField(max_length=50)

    Profile = models.Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class FavTeam(models.Model):
    my_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    current_points = models.DecimalField(max_digits=3, decimal_places=0)
    current_wins = models.DecimalField(max_digits=2, decimal_places=0)
    current_losses = models.DecimalField(max_digits=2, decimal_places=0)
    current_otls = models.DecimalField(max_digits=2, decimal_places=0)
    current_sols = models.DecimalField(max_digits=2, decimal_places=0)


class FavPlayer(models.Model):
    my_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    current_points = models.DecimalField(max_digits=3, decimal_places=0)
    current_goals = models.DecimalField(max_digits=2, decimal_places=0)
    current_assists = models.DecimalField(max_digits=2, decimal_places=0)
    current_pims = models.DecimalField(max_digits=2, decimal_places=0)
    allstar_appearances = models.DecimalField(max_digits=2, decimal_places=0)
