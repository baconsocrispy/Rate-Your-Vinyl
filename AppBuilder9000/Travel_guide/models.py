#imports
from django.db import models

# Models;
class Destination(models.Model):
    Country = models.CharField(max_length=35)
    Region = models.CharField(max_length=35)
    Description = models.CharField(max_length=50)

    # Model Manager;
    Entry = models.Manager()

    # str() Method;
    def __str__(self):
        return self.Location

