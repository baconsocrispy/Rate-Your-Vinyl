from django.db import models


# class Publisher(models.Model):
#     Name = models.CharField(max_length=30, null=False, blank=False)
#     pass
#
#     def __str__(self):
#         return self.Name


class BoardGame(models.Model):
    Name = models.CharField(max_length=50, null=False, blank=False)
    Publisher = models.CharField(max_length=50, null=False, blank=False) #ForeignKey(Publisher, on_delete=models.CASCADE)
    Year = models.IntegerField(default=2021)
    Description = models.TextField(default="Type your review here (optional)")
    Thumbnail = models.CharField(max_length=100, null=False, blank=True)
    Image = models.CharField(max_length=100, null=False, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Name
