from django.db import models


# Create your models here.
HALL_OF_FAME = [
    ('YES', 'Yes'),
    ('NO', 'No'),
]


class Players(models.Model):
    name = models.CharField(max_length=50)
    seasons_played = models.IntegerField(default='')
    mvp_awards = models.IntegerField(default='')
    championships = models.IntegerField(default='')
    hall_of_fame = models.CharField(max_length=3, choices=HALL_OF_FAME)

    Player = models.Manager()

    def __str__(self):
        return self.name
