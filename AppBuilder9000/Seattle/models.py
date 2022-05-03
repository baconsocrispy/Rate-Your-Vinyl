from django.db import models

Place_Type = [
    ('Food', 'Food'),
    ('Hotel', 'Hotel'),
    ('Parking', 'Parking'),
    ('Parks', 'Parks'),
    ('Attraction', 'Attraction')
]

class Places(models.Model):
    category = models.CharField(max_length=50, choices=Place_Type, default='')
    place = models.CharField(max_length=20, default='', blank=True, null=False)
    desc = models.CharField(max_length=500, default='', blank=True, null=False)
    duration = models.IntegerField(max_length=2, default='0', blank=True, null=False)

    Places = models.Manager

    def __str__(self):
        return self.place

