from django.db import models


class BoardGame(models.Model):
    Name = models.CharField(max_length=50, null=False, blank=False)
    Publisher = models.CharField(max_length=50, null=False, blank=False)
    Year = models.IntegerField(default=2021)
    Description = models.TextField(default="Type your review here (optional)")
    Thumbnail = models.CharField(max_length=200, null=False, blank=True)
    Image = models.CharField(max_length=200, null=False, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Name
