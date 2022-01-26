from django.db import models


# Create your models here.
class Profile(models.Model):
    TEAM_OPTIONS = (
        ('AN', 'Anaheim Ducks'),
        ('AZ', 'Arizona Coyotes'),
        ('BO', 'Boston Bruins'),
        ('BU', 'Buffalo Sabres'),
        ('CY', 'Calgary Flames'),
        ('CA', 'Carolina Hurricanes'),
        ('CO', 'Colorado Avalanche'),
        ('CS', 'Columbus Blue Jackets'),
        ('DA', 'Dallas Stars'),
        ('DT', 'Detroit Red Wings'),
        ('ED', 'Edmonton Oilers'),
        ('FL', 'Florida Panthers'),
        ('LA', 'Los Angeles Kings'),
        ('MN', 'Minnesota Wild'),
        ('MT', 'Montreal Canadiens'),
        ('NS', 'Nashville Predators'),
        ('NJ', 'New Jersey Devils'),
        ('NY', 'New York Rangers'),
        ('NI', 'New York Islanders'),
        ('OT', 'Ottawa Senators'),
        ('PH', 'Philadelphia Flyers'),
        ('PT', 'Pittsburgh Penguins'),
        ('SJ', 'San Jose Sharks'),
        ('SE', 'Seattle Kraken'),
        ('ST', 'St. Louis Blues'),
        ('TB', 'Tampa Bay Lightning'),
        ('TM', 'Toronto Maple Leafs'),
        ('VC', 'Vancouver Canucks'),
        ('VG', 'Vegas Golden Knights'),
        ('WC', 'Washington Capitals'),
        ('WJ', 'Winnipeg Jets'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    favorite_team = models.CharField(max_length=2, choices=TEAM_OPTIONS)

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
