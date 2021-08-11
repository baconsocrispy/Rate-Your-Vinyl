from django.db import models

# Create your models here.



HIGHLIGHT_CHOICES =  {
    ('good food','good food'),
    ('good drinks','good drinks'),
    ('stiff pour','stiff pour'),
    ('budget friendly','budget friendly'),
    ('late night HH','late night HH'),
    ('dietary options','dietary options'),
    ('ambiance','ambiance'),
    ('location','location'),
}

class Restaurants(models.Model):
    r_name = models.CharField(max_length=50)
    r_address = models.CharField(max_length=250)
    r_highlights = models.CharField(max_length=50, choices=HIGHLIGHT_CHOICES)
    r_review = models.TextField(max_length= 500)
    r_image = models.CharField(max_length=255, default='', blank=True)

    objects = models.Manager()

    # Allows references to a specific account to be returned
    # as the owner's name not the primary key
    def __str__(self):
        return self.r_name


