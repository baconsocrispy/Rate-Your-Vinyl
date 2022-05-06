from django.db import models


# Create your models here.
class Activities(models.Model):
    activity_name = models.CharField(max_length=50)
    activity_snacks = models.CharField(max_length=50)
    activity_description = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=5, decimal_places=0, default="")

    ActivitiesManager = models.Manager()

    def __str__(self):
        return self.activity_name
