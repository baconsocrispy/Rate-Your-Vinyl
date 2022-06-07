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

#Comments Section


class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    Comments = models.Manager()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name
