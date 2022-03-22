from django.db import models


class House(models.Model):
    tagline = models.CharField(max_length=60)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()
    squareFootage = models.PositiveIntegerField()
    price = models.CharField(max_length=15)
    notes = models.TextField()

    def __str__(self):
        return self.tagline
