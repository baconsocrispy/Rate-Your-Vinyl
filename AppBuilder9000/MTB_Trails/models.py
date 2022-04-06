from django.db import models


TRAIL_DIFFICULTY = [
    ("1", "1 - Easy"),
    ("2", "2 - Easy/Intermediate"),
    ("3", "3 - Intermediate"),
    ("4", "4 - Intermediate/Difficult"),
    ("5", "5 - Difficult"),
    ("6", "6 - Very Difficult"),
]

US_STATES = [
    ("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"),
    ("CA", "California"), ("CO", "Colorado"), ("CT", "Connecticut"), ("DE", "Delaware"),
    ("FL", "Florida"), ("GA", "Georgia"), ("HI", "Hawaii"), ("ID", "Idaho"),
    ("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"), ("KS", "Kansas"),
    ("KY", "Kentucky"), ("LA", "Louisiana"), ("ME", "Maine"), ("MD", "Maryland"),
    ("MA", "Massachusetts"), ("MI", "Michigan"), ("MN", "Minnesota"), ("MS", "Mississippi"),
    ("MO", "Missouri"), ("MT", "Montana"), ("NE", "Nebraska"), ("NH", "New Hampshire"),
    ("NJ", "New Jersey"), ("NM", "New Mexico"), ("NY", "New York"), ("NC", "North Carolina"),
    ("ND", "North Dakota"), ("NV", "Nevada"), ("OH", "Ohio"), ("OK", "Oklahoma"),
    ("OR", "Oregon"), ("PA", "Pennsylvania"), ("RI", "Rhode Island"), ("SC", "South Carolina"),
    ("SD", "South Dakota"), ("TN", "Tennessee"), ("TX", "Texas"), ("UT", "Utah"),
    ("VA", "Virginia"), ("VT", "Vermont"), ("WA", "Washington"), ("WV", "West Virginia"),
    ("WI", "Wisconsin"), ("WY", "Wyoming"),
]


class ReviewTrail(models.Model):
    trail_name = models.CharField(max_length=60)
    nearest_city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=60, choices=US_STATES)
    review = models.TextField()
    difficulty = models.CharField(max_length=60, choices=TRAIL_DIFFICULTY)

    objects = models.Manager()

    def __str__(self):
        return self.trail_name


class CreateTrail(models.Model):
    trail_name = models.CharField(max_length=60)
    nearest_city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=60, choices=US_STATES)
    directions = models.TextField(blank=True, default="How do we get there?")
    need_to_know = models.TextField(blank=True, default="Sketchy sections, flooded areas. Whatever"
                                                              " fellow bikers need to know.")
    difficulty = models.CharField(max_length=60, choices=TRAIL_DIFFICULTY)

    objects = models.Manager()

    def __str__(self):
        return self.trail_name
