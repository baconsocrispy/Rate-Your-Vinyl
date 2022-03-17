from django.db import models


# Create your models here.

class ChefKnives(models.Model):
    brands = models.CharField(max_length=60)
    price = models.IntegerField(default='')
    country_origin = models.CharField(max_length=60)
    steal = models.CharField(max_length=60)
    blade_style = models.CharField(max_length=60)

    objects = models.Manager()

    def __str__(self):
        return self.brands
