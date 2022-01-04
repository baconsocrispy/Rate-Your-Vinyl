from django.db import models


# defining sex choices
SEX_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class Pet(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    weight = models.IntegerField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    description = models.TextField(max_length=500)

    # reference the pet by name
    def __str__(self):
        return self.name

    # objects manager
    Pets = models.Manager()


