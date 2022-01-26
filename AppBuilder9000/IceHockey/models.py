from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class User(models.Model):
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
    favorite_player = models.CharField(max_length=80)
    favorite_team = models.CharField(max_length=2, choices=TEAM_OPTIONS)

    User = models.Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class CreateAPlayer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jersey_number = models.DecimalField(
        max_digits=2,
        decimal_places= 0,
        default=1,
        validators=[MaxValueValidator(99), MinValueValidator(1)]
     )
    height_feet = models.DecimalField(
        max_digits=1,
        default=5,
        decimal_places=0,
        validators=[MaxValueValidator(6), MinValueValidator(4)]
     )
    height_inches = models.DecimalField(
        max_digits=2,
        default=0,
        decimal_places=0,
        validators=[MaxValueValidator(11), MinValueValidator(0)]
    )