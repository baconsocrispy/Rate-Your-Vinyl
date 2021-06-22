from django.db import models

WHICH_AFFILIATION = {
    ('light', 'light'),
    ('dark', 'dark'),
    ('neutral', 'neutral')
}


class Character(models.Model):
    Name_of_Character = models.CharField(max_length=100)
    First_Appearance = models.CharField(max_length=60, default='', blank=True)
    Race_Type = models.CharField(max_length=60, default='', blank=True)
    Affiliation = models.CharField(max_length=60, default='neutral', choices=WHICH_AFFILIATION)
    Additional_Details = models.TextField(blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Name_of_Character
