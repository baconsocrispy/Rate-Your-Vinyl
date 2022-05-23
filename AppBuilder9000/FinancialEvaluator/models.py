from django.db import models

# Create your models here.


class Account(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=50, default="")

    Accounts = models.Manager()


Stock = [('IP', 'IP'), ('GPKG', 'GPKG'), ('NVDA', 'NVDA'), ('KO', 'KO')]
Docs = [('BalanceSheet', 'BalanceSheet'), ('Chart', 'Chart'), ('PriceRating', 'PriceRating')]
Type = [('Appreciation', 'Appreciation'), ('Consistent Growth', 'Consistent Growth'), ('Dividends', 'Dividends'), ('Options', 'Options')]


class Evaluation(models.Model):
    symbol = models.CharField(max_length=4, blank=False, default="AAPL")
    style = models.CharField(max_length=30, choices=Type, default="", blank=False, null=False)

    Evaluations = models.Manager()

class Approach(models.Model):
    security = models.CharField(max_length=7, choices=Stock, default="", blank=False, null=False)
    documents = models.CharField(max_length=30, choices=Docs, blank=False, null=False)

    Approaches = models.Manager()


