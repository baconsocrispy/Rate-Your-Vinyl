from django.db import models

# Create your models here.

# PreciousMetals model for database
formTypes = [('coin', 'coin'), ('bar', 'bar'), ('raw', 'raw')]
metalTypes = [('Silver', 'Silver'), ('Gold', 'Gold')]


class PreciousMetalsItem(models.Model):
    type = models.CharField(max_length=10, choices=metalTypes)
    make = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    ounces = models.IntegerField()
    form = models.CharField(max_length=10, choices=formTypes)
    count = models.IntegerField()
    metals = models.Manager()

    def __str__(self):
        return self.make + ' ' + self.year

