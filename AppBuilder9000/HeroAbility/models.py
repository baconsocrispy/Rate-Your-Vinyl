from django.db import models

THREAT = { #establish threat levels
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
}

#set up the Heroes class for the db.
class Heroes(models.Model):
    alias = models.CharField(max_length=30, default="", blank=False, null=False)
    secretIdentity = models.CharField(max_length=50, default="", blank=True, null=False)
    abilityName = models.CharField(max_length=25, default="", blank=False, null=False)
    abilitySummary = models.CharField(max_length=100, default="", blank=False, null=False)
    weakness = models.CharField(max_length=25, default="", blank=True, null=False)
    threatLevel = models.CharField(max_length=2, default="", choices=THREAT)

    #assign a manager
    heroes = models.Manager()

    def __str__(self):
        return self.alias
