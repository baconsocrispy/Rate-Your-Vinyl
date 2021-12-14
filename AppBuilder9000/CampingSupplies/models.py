from django.db import models

color_choices = [
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Orange', 'Orange'),
    ('Yellow', 'Yellow'),
    ('Green', 'Green'),
    ('Purple', 'Purple'),
]

size_choices = [
    ('Extra Small', 'Extra Small'),
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
    ('Extra Large', 'Extra Large'),
]

class Tent(models.Model):
    Color = models.CharField(max_length=30, default="", choices=color_choices)
    PersonCount = models.IntegerField(max_length=2)
    Price = models.FloatField(max_length=30)

class CookingTool(models.Model):
    Product_Name = models.CharField(max_length=30)
    Price = models.FloatField(max_length=30)
    Material = models.CharField(max_length=30)

class Pants(models.Model):
    Size = models.CharField(max_length=30, default="", choices=size_choices)
    Price = models.FloatField(max_length=30)
    Color = models.CharField(max_length=30, default="", choices=color_choices)


class Coat(models.Model):
    Size = models.CharField(max_length=30)
    Price = models.FloatField(max_length=30)
    Color = models.CharField(max_length=30, default="", choices=color_choices)

    object = models.Manager

    def __str__(self):
        return self.name

# Create your models here.
