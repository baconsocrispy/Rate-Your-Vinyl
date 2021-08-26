from django.db import models


# Create your models here.
class Player(models.Model):
    Name = models.CharField(max_length=30)
    Win_Shares = models.DecimalField(max_digits=5, decimal_places=1)
    Player_Efficiency_Rating = models.DecimalField(max_digits=5, decimal_places=1)
    Points_Per_Game = models.DecimalField(max_digits=5, decimal_places=1)
    Seasons = models.IntegerField(default='')
    Hall_of_Fame = models.BooleanField(default=False, null=False, blank=False)

    objects = models.Manager()

    def __str__(self):
        return self.Name
