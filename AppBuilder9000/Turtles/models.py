from django.db import models

# Defining a new tuple object(species of turtles)
TYPE_CHOICES = (
    ('Turtle', 'Turtle'),
    ('Tortoise','Tortoise'),
    ('Terrapin','Terrapin')
)

# Defining a new tuple object(native region of turtles)
LOCALITY_CHOICES =(
    ('Americas', 'Americas'),
    ('Europe', 'Europe'),
    ('Asia', 'Asia')
)

class Turtles(models.Model):
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=15, choices=TYPE_CHOICES)
    size = models.
    locality = models.CharField(max_length=15, choices=LOCALITY_CHOICES)

    # Using dunder method to reference Turtles class
    def __str__(self):
        return self.name

    # Objects manager
    Turtles = models.Model()

