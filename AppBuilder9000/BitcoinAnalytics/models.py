from django.db import models


class Competitor(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    linkedIn = models.CharField(max_length=100)

    Competition = models.Manager()

    # allows references to a specific competitor as the person's name, not the primary key
    def __str__(self):
        return self.name
