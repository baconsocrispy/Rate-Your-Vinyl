from django.db import models

TRACK_ME = [
    ('startTracking', 'startTracking'),
    ('dontTrack', 'dontTrack'),
]
CHOICES = [
    ('yes', 'yes'),
    ('no', 'no'),
]

class TrackApp(models.Model):
    location = models.CharField(max_length=50, choices=TRACK_ME)

class CHOICES(models.Model):
    YES = models.CharField(max_length=20)
    NO = models.CharField(max_length=20)

class Name(models.Model):
    submit = models.CharField(max_length=50)

def __str__(self):
    return self.TrackMe