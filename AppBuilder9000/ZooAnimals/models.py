from django.db import models

###Creating the choice for SSP
SSP_Choices = (
    ('Yes', 'Yes'),
    ('No', 'No')
)

###Creating the location choices
Location = (
    ('Africa', 'Africa'),
    ('The Arctics', 'The Arctics'),
    ('Asia', 'Asia'),
    ('Australia', 'Australia'),
    ('Europe','Europe'),
    ('Education', 'Education'),
    ('North America', 'North America'),
    ('South America', 'South America'),
    ('World Oceans', 'World Oceans'),
)

class Species(models.Model):
    commonName = models.CharField(max_length=120, default="", blank=True, null=False, verbose_name='Common Name')
    latinName = models.CharField(max_length=120, default="", blank=True, null=False, verbose_name='Latin Name')
    location = models.CharField(max_length=60, choices= Location)
    SSP = models.CharField(max_length=60, choices= SSP_Choices)

    objects= models.Manager

    def __str__(self):
        return self.commonName

