from django.db import models

# Create your models here.
type_choices = [
    ('ATV', 'ATV'),
    ('Motorcycle', 'Motorcycle'),
    ('Side by Side', 'Side by Side'),
]

trail_type = [
    ('Grass', 'Grass'),
    ('Dirt', 'Dirt'),
    ('Concrete', 'Concrete'),
    ('Gravel', 'Gravel'),
    ('Sand', 'Sand'),
    ('Woodchips', 'Woodchips'),
]


class AtvTrails(models.Model):
    trail_name = models.CharField(max_length=50, default="", blank=True)
    vehicle_type = models.CharField(max_length=60, choices=type_choices)
    trail_distance = models.DecimalField(max_digits=4, decimal_places=2, default="", blank=True)
    trail_terrain = models.CharField(max_length=60, default="", choices=trail_type)
    trail_description = models.TextField(max_length=500, default="", blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.trail_name
