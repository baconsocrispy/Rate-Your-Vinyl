# Imports;
from django.db import models

# Models;
class Skater(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    hometown = models.CharField(max_length=50)

    # Model Manager;
    Entry = models.Manager()

    # str() Method;
    def __str__(self):
        return self.first_name + '' + self.last_name