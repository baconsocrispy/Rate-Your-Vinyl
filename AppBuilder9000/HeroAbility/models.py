from django.db import models

THREAT = [  # establish threat levels
    ('0', 'Nonexistent'),
    ('1', 'Mild Inconvenience'),
    ('2', 'Minor Threat'),
    ('3', 'Robin Equivalent'),
    ('4', 'Major Threat'),
    ('5', 'World Ending'),
]


# set up the Heroes class for the db.
class Heroes(models.Model):
    alias = models.CharField(max_length=30, default="", blank=False, null=False)
    secret_Identity = models.CharField(max_length=50, default="", blank=True, null=False)
    ability_Name = models.CharField(max_length=25, default="", blank=False, null=False)
    ability_Summary = models.TextField(max_length=200, default="", blank=False, null=False)
    weakness = models.CharField(max_length=25, default="", blank=True, null=False)
    threat_Level = models.CharField(max_length=2, default="0", choices=THREAT)

    # assign a manager
    heroes = models.Manager()

    def __str__(self):
        return self.alias
