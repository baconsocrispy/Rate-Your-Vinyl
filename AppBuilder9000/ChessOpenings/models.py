from django.db import models


# Create your models here.
class Games(models.Model):

    title = models.CharField(max_length=50)
    playerWhite = models.CharField(max_length=50)
    playerBlack = models.CharField(max_length=50)
    yearPlayed = models.IntegerField(max_length=4)
    fen_string = models.CharField(max_length=150)
    winner = models.CharField(max_length=10)

    Game = models.Manager()

    def __str__(self):
        return self.title or "{}, {}".format(self.playerWhite, self.playerBlack)


from django.db import models

# Create your models here.
