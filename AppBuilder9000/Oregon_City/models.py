from django.db import models


# Create your models here.
class Activities(models.Model):
    activity_name = models.CharField(max_length=50)
    activity_snacks = models.CharField(max_length=50)
    activity_description = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=5, decimal_places=0, default="")

    Activities = models.Manager()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.is_valid = Activities
        self.title = None
