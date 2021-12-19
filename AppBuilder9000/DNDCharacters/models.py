from django.db import models

# Create your models here.

CLASS_CHOICES = {
    ('Fighter','Fighter'),
    ('Barbarian','Barbarian'),
    ('Ranger','Ranger'),
    ('Cleric','Cleric'),
    ('Druid','Driud'),
    ('Wizard','Wizard'),
    ('Bard','Bard'),
    ('Sorcerer','Sorcerer'),
    ('Warlock','Warlock'),
}
class Characters(models.Model):
    Character_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Character_Class = models.CharField(max_length=60, choices=CLASS_CHOICES)
    Strength = models.IntegerField(choices=list(zip(range(8,19), range(8,19))),unique=True)
    Dexterity = models.IntegerField(choices=list(zip(range(8,19), range(8,19))),unique=True)
    Constitution = models.IntegerField(choices=list(zip(range(8,19), range(8,19))),unique=True)
    Intellegence = models.IntegerField(choices=list(zip(range(8,19), range(8,19))),unique=True)
    Wisdom = models.IntegerField(choices=list(zip(range(8,19), range(8,19))),unique=True)
    Charisma = models.IntegerField(choices=list(zip(range(8,19), range(8,19))),unique=True)
    Background = models.TextField(max_length=300, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Character_Name


