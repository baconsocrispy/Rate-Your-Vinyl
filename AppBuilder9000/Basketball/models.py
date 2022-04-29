from django.db import models

# Create your models here.
position_choices = (
    ('pg', 'Point Guard'),
    ('sg', 'Shooting Guard'),
    ('sf', 'Small Forward'),
    ('pf', 'Power Forward'),
    ('c', 'Center')
)


class Pickup(models.Model):
    position = models.CharField(max_length=30, choices=position_choices, default='Point Guard')
    date = models.DateField()
    points = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()
    rebounds = models.PositiveIntegerField()
    steals = models.PositiveIntegerField()
    blocks = models.PositiveIntegerField()
    turnovers = models.PositiveIntegerField()
