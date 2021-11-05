from django.db import models


# Create your models here.


class BirdDescription(models.Model):
    bird_name = models.CharField(max_length=30, blank=True)
    date_seen = models.DateField(blank=True)
    habitat = models.TextField(max_length=300)
    description = models.TextField(max_length=300)
    image = models.ImageField(blank=True)

# BirdDescription is the models manager for accessing the dB.
    BirdDescriptions = models.Manager()

    def __str__(self):
        return str(self.bird_name)





