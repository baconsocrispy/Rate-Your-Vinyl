from django.db import models

# The models I created required a lot of choice selections so for the next little bit here are the choices.
# The first field in the choices is what will be stored in the dB, the second field is what the user sees.


timeZoneChoices = (
    ('1', 'Azores'),
    ('2', 'Iceland'),
    ('3', 'Portugal, UK, Canary Islands'),
    ('4', 'Western Europe, Scandinavia, Central Europe'),
    ('5', 'Finland, Ukraine, Romania, Greece'),
    ('6', 'Belarus, Western Russia, Turkey'),
    ('7', 'Georgia, Azerbaijan')
)

safetyChoices = (
    ('1', 'Not safe at all'),
    ('2', 'Not safe, would not bring family'),
    ('3', 'Decently safe, just be careful and wise'),
    ('4', 'No safety threats, but there are areas I would not go'),
    ('5', 'Really safe, my grandma would be ok')
)

priceChoices = (
    ('1', 'Extremely cheap to visit'),
    ('2', 'Not the cheapest, but close'),
    ('3', 'Average price'),
    ('4', 'A little lavish'),
    ('5', 'Only for the high rollers')
)

# I'm creating 3 basic models here to contain pertinent information about destinations in Europe


class Location(models.Model):
    city = models.CharField(primary_key=True, max_length=200, help_text="Which city are we talking about?")
    timeZone = models.CharField(max_length=200, help_text="Please select from the list, to convert it's time zone.",
                                choices=timeZoneChoices)
    safety = models.CharField(max_length=200, help_text="Please choose a safety rating for this location.",
                              choices=safetyChoices)
    prices = models.CharField(max_length=150, help_text="Please consider the total price of the trip when rating",
                              choices=priceChoices)

    objects = models.Manager()

    def __str__(self):
        return self.city


