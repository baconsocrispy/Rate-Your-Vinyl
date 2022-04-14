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

# weight class drop down
# basic model for database
class Fighter(models.Model):
    category = models.CharField(max_length=60, choices=WeightClass_Dropdown, default='Choose your weight class!')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=60)
    weight_in_lbs = models.CharField(max_length=20)
    gym = models.CharField(max_length=60)

    Fighter = models.Manager()

    def __str__(self):
        return self.first_name
