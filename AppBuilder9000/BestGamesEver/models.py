from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    year = models.IntegerField(default='2000')
    description = models.TextField(max_length=200)

    objects = models.Manager()


    def __str__(self):
        return self.name