from django.db import models

STYLES = [
    ('Melee', 'Melee'),
    ('Ranged', 'Ranged'),
    ('Magic', 'Magic'),
]


class Item(models.Model):
    # General Information
    type = models.CharField(max_length=20, default="", choices=STYLES )
    name = models.CharField(max_length=20, default="")
    # Attack Bonuses
    atk_stab = models.IntegerField()
    atk_slash = models.IntegerField()
    atk_crush = models.IntegerField()
    atk_magic = models.IntegerField()
    atk_range = models.IntegerField()
    # Defence Bonuses
    def_stab = models.IntegerField()
    def_slash = models.IntegerField()
    def_crush = models.IntegerField()
    def_magic = models.IntegerField()
    def_range = models.IntegerField()
    # Other Bonuses
    bns_strength = models.IntegerField()
    bns_range = models.IntegerField()
    bns_magic = models.IntegerField()
    bns_prayer = models.IntegerField()
    # Weapon Slot
    slot = models.CharField(max_length=60, default="")
    # Weapon Speed
    speed = models.IntegerField()
    # Range
    range = models.IntegerField()
    # Images
    image = models.URLField(max_length=255, default="")

    # Renaming the models manager to a new variable
    objects = models.Manager()

    def __str__(self):
        return self.name
