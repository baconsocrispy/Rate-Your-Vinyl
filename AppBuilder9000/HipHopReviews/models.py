from django.db import models
from django.forms import ModelForm

class Reviews(models.Model):
    ArtistName = models.CharField(max_length=60)
    AlbumName = models.CharField(max_length=60, blank=True)
    ReleaseYear = models.IntegerField(max_length=4, blank=True)


    objects = models.Manager()

    def __str__(self):
        return self.ArtistName, self.AlbumName, self.ReleaseYear