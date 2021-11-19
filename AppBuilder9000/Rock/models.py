from django.db import models

# Create your models here.


class HardRock(models.Model):
    artist = models.CharField(max_length=60)
    member = models.CharField(max_length=60)
    Genre = models.CharField(max_length=60)
    album = models.CharField(max_length=60)

    objects = models.Manager()
