from django.db import models

# Create your models here.

class Account(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, default="")

    Accounts = models.Manager()


Stock = ['IP', 'GPKG', 'NVDA', 'KO', 'DEL', 'F', 'TSLA', 'X', 'BRYN', 'SHEL', 'AMD', 'DIS', 'XOM', 'BAC', 'GM', 'WMT']
AppreciationDocs = ['BalanceSheet', 'Chart', 'PriceRating']


class Evaluation(models.Model):
    stock = models.CharField(max_length=7, choices=Stock, default="", blank=False, null=False)
    documents = models.CharField(max_length=30, choices=AppreciationDocs, blank=False, null=False)

    Evaluations = models.Manager()




