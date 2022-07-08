from django.db import models

Type_Color = [
    ('Red', 'Red'),
    ('White', 'White'),
    ('Pink', 'Pink'),
]

Region_Choices = [
    ('France', 'France'),
    ('Italy', 'Italy'),
    ('Spain', 'Spain'),
    ('Germany', 'Germany'),
    ('U.S.A', 'U.S.A'),
    ('Argentina', 'Argentina'),
    ('Chile', 'Chile'),
]


class Wines(models.Model):
    type = models.CharField(max_length=20, choices=Type_Color)
    varietal = models.CharField(max_length=60)
    region = models.CharField(max_length=60, choices=Region_Choices)

    objects = models.Manager()

    def __str__(self):
        return self.type