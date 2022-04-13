from django.db import models

# Dropdown menu
WeightClass_Dropdown = [
    ('Flyweight', 'Flyweight'),
    ('Bantamweight', 'Bantamweight'),
    ('Featherweight', 'Featherweight'),
    ('Welterweight', 'Welterweight'),
    ('Middleweight', 'Middleweight'),
    ('Heavyweight', 'Heavyweight'),
]

# basic model for database
class Fighter(models.Model):
    category = models.CharField(max_length=60, choices=WeightClass_Dropdown, default='Choose your weight class!')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ring_name = models.CharField(max_length=60)
    weight_class = models.CharField(max_length=60)
    record = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

    Fighter = models.Manager()