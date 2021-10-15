from django.db import models

class RockLoc(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    location_description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
