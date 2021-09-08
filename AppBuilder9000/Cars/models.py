from django.db import models

class description(models.Model):
    make = models.CharField(max_length=60, default='', null=False)
    model = models.CharField(max_length=60, default='', null=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)

    objects = models.Manager()

    def __str__(self):
        return self.name

# Create your models here.
