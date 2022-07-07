from django.db import models


SKIN_CHOICES = {
    ('meat','meat'),
    ('metal','metal'),
    ('fungus','fungus'),
    ('scale','scale'),
    ('gem','gem'),
}

BEAST_CHOICES = {
    ('unknown','unknown'),
    ('dog','canine'),
    ('cat','feline'),
    ('reptile','reptilian'),
    ('bird','avian'),
    ('frog','amphibian'),
}

POWER_CHOICES = {
    ('presence','ominous presence'),
    ('dust','deadly dust'),
    ('spikes','menacing spikes'),
    ('fire','firey breath'),
    ('webs','sticky webs'),
}

# Create your models here.
class Fbeast(models.Model):
    name = models.CharField(max_length=60, default="", null=False)
    title = models.CharField(max_length=60, default="Forgotten Beast")
    skin = models.CharField(max_length=60, choices=SKIN_CHOICES)
    species = models.CharField(max_length=60, choices=BEAST_CHOICES)
    power = models.CharField(max_length=60, choices=POWER_CHOICES)

    Fbeasts = models.Manager()

    def __str__(self):
        return self.name