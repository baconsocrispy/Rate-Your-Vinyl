from django.db import models

# Create your models here.
ATT_CHOICES = {
    (8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),
}
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
    background = models.TextField(max_length=300, default="", blank=True)
    Strength = models.IntegerField(choices=ATT_CHOICES)
    Dexterity = models.IntegerField(choices=ATT_CHOICES)
    Constitution = models.IntegerField(choices=ATT_CHOICES)
    Intellegence = models.IntegerField(choices=ATT_CHOICES)
    Wisdom = models.IntegerField(choices=ATT_CHOICES)
    Charisma = models.IntegerField(choices=ATT_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.Character_Name


