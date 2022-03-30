from django.db import models
from django import forms

# Create your models here.
Genre_Choices = (
    ('comedy','Comedy'),
    ('anime', 'Anime'),
    ('horror','Horror'),
    ('sitcom', 'Sitcom'),
    ('musical', 'Musical'),
    ('slice of life','Slice of LIfe'),
    ('early animation','Early Animation'),
)

class Cartoon(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=30)
    premier_date = models.DateField()
    brief_description = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=Genre_Choices, default='select one')

    Cartoons = models.Manager()

    def __str__(self):
        return self.title
