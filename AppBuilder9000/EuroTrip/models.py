from django.db import models

# The models I created required a lot of choice selections so for the next little bit here are the choices.
# The first field in the choices is what will be stored in the dB, the second field is what the user sees.
duration_of_Activity_Choices = (
    ('30', '30 Minutes'),
    ('60', '1 Hour'),
    ('90', '1 Hour 30 Minutes'),
    ('120', '2 Hours'),
    ('180', '3 Hours'),
    ('360', '6 Hours'),
    ('720', '12 Hours'),
    ('1440', '24 Hours'),
    ('3000', 'A Few Days')
)

ratingChoices = (
    ('1', 'Horrible'),
    ('2', 'I\'ve seen worse'),
    ('3', 'It was okay'),
    ('4', 'It was good'),
    ('5', 'Wow! Simply the best thing since sliced bread')
)

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

cleanlinessChoices = (
    ('1', 'Extremely dirty'),
    ('2', 'Not the dirtiest, but less than desirable'),
    ('3', 'Average cleanliness'),
    ('4', 'A little cleaner than most'),
    ('5', 'Extremely clean')
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


class thingsToDo(models.Model):
    activity = models.CharField(max_length=200, help_text="Please briefly explain the fun things you did there.")
    duration_of_Activity = models.CharField(max_length=200, help_text="How long did you spend doing the activity?",
                                            choices=duration_of_Activity_Choices)
    startDate = models.DateField(help_text="Is this activity time sensitive? Is it only for a weekend, month, etc?")
    endDate = models.DateField(help_text="If there was a start date, is there an end date?")
    rating = models.CharField(max_length=100, choices=ratingChoices, help_text="Please rate your experience.")
    country = models.CharField(max_length=100, help_text="In which European country does this occur?")
    city = models.ForeignKey(Location, on_delete=models.PROTECT, max_length=200, help_text="It occurs in which city?")

    objects = models.Manager()

    def __str__(self):
        return self.activity


class Accommodations(models.Model):
    city = models.ForeignKey(Location, on_delete=models.PROTECT, max_length=200, help_text="Where ya staying?")
    diningFacilities = models.BooleanField(help_text="Does the hotel have dining services?")
    cleanliness = models.CharField(max_length=200, help_text="How clean was this place?", choices=cleanlinessChoices)
    healthcare = models.BooleanField(help_text="Was the hotel within 10 minutes of a healthcare facility?")
    accommodationName = models.CharField(max_length=200, help_text="What was the name of where you stayed?")

    objects = models.Manager()

    def __str__(self):
        return self.accommodationName


class Pricing(models.Model):
    city = models.ForeignKey(Location, on_delete=models.PROTECT, max_length=200, help_text="Where did you travel to?")
    prices = models.CharField(max_length=150, help_text="How pricey was the location?", choices=priceChoices)
    airlineprices = models.CharField(max_length=150, help_text="Choose a price category for the airfare, please.",
                                     choices=priceChoices)

    objects = models.Manager()

    def __str__(self):
        return self.city
