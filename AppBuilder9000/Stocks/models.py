from django.db import models


class Stocks(models.Model):
    ticker = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.ticker

