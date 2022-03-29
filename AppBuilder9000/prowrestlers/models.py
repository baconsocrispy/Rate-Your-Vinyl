from django.db import models
from django.forms import ModelForm


# Create your models here.
class Wrestler(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    win_number = models.IntegerField()

    object = models.manager()