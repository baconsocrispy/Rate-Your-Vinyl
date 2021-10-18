from django.db import models

# Create your models here.

SONG_CHOICES = (('Kiss & Cry', 'Beautiful World'),
                ('Flavor of Life (Ballad Version)', 'Sakura Drops'),
                ('Simple & Clean', 'Sanctuary'),
                ('Keep Trying', 'Automatic'),
                ('Hikari', 'Passion'))

class Music(models.Model):
    songs = models.CharField(max_length=70, choices=SONG_CHOICES)
    #user will select a song from the list and it will play
    year = models.IntegerField()
    image = models.CharField(max_length=500)

    Songs = models.Manager()

    def __str__(self):#intake
        return self.songs

