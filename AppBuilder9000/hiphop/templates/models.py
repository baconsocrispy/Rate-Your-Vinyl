from django.db import models
from django import forms

TYPE_CHOICES = {
    ('1 mic', '1 mic'),
    ('2 mic', '2 mic'),
    ('3 mic', '3 mic'),
    ('4 mic', '4 mic'),
    ('5 mic', '5 mic'),
}


class Choice(models.model):
    80 = models.CharField(max_length=50, default="", blank=True, null=False)
    90 = models.CharField(max_length=50, default="", blank=True, null=False)
    2000 = models.CharField(max_length=50, default="", blank=True, null=False)
    todays = models.TextField(max_length=300, default="", blank=True, null=False)
    mics = models.CharField(max_length=10, choices=TYPE_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.mics
