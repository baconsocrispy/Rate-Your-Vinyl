from django.db import models

# Create your models here.


class Deck(models.Model):
    commander = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    key_pieces = models.TextField(max_length=1000)
    image = models.CharField(max_length=1000)

    Deck = models.Manager()

    def __str__(self):
        return self.commander
