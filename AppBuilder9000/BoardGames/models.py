from django.db import models


class Publisher(models.Model):
    Name = models.CharField(max_length=30, null=False, blank=False)
    pass


class BoardGame(models.Model):
    Name = models.CharField(max_length=50, null=False, blank=False)
    Publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    Year = models.IntegerField(default=2021)
    Description = models.TextField(default="Type your review here (optional)")
    Thumbnail = models.FilePathField(max_length=100, null=False, blank=True)
    Image = models.FilePathField(max_length=100, null=False, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Name
