from django.db import models


# Create your models here.
class Players(models.Model):
    name = models.CharField(max_length=50)
    seasons_played = models.IntegerField(default='')
    mvp_awards = models.IntegerField(default='')
    championships = models.IntegerField(default='')

    Player = models.Manager()

    def __str__(self):
        return self.name
