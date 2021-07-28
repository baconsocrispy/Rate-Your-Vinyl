from django.db import models


class Album(models.Model):
    Name = models.CharField(max_length=50, null=False, blank=False)
    Artist = models.CharField(max_length=30, null=False, blank=False)
    Year = models.IntegerField
    Genre = models.CharField(max_length=50)
    Rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    Review = models.TextField

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.Name, self.Artist)
