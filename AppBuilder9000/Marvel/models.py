from django.db import models

# Create your models here.

TYPE_CHOICES = {
    ('Hero', 'Hero'),
    ('Villain', 'Villain'),
}


class Character(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100, default="", blank=True, null=False)
    description = models.TextField(max_length=100, default="", blank=True)
    image = models.CharField(max_length=255, default='', blank=True)

    Characters = models.Manager()

    def __str__(self):
        return self.name
