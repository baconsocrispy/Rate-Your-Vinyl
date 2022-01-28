from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ('Prefer not to say', 'Prefer not to say'),

]

area_of_health_choices = [
    ('Immune Health', 'Immune Health'),
    ('Energy and Focus', 'Energy and Focus'),
    ('Joint Health', 'Joint Health'),
    ('Cognition and Memory', 'Cognition and Memory'),
    ('Stress Relief', 'Stress Relief'),
    ('Sleep Hygiene', 'Sleep Hygiene'),
    ('Skin, Hair, and Nails', 'Skin, Hair, and Nails'),
]

supplement_type_choices = [
    ('Herbs', 'Herbs'),
    ('Vitamins', 'Vitamins'),
    ('Minerals', 'Minerals'),
    ('Phytonutrients', 'Phytonutrients'),
    ('Other', 'Other'),
    ('Any', 'Any'),
]

class Account(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(130),MinValueValidator(18)])
    gender = models.CharField(max_length=60, default="", choices=gender_choices)
    email = models.EmailField(max_length=150)

    Accounts = models.Manager()

    # allows references to a specific account to be returned as the owner's name not the primary key
    def __str__(self):
        return self.name

class PersonalizedNutrition(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(130),MinValueValidator(18)])
    gender = models.CharField(max_length=60, default="", choices=gender_choices)

    area_of_health = models.CharField(max_length=100, default="", choices=area_of_health_choices)
    supplement_type = models.CharField(max_length=60, default="", choices=supplement_type_choices)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


    Personalized = models.Manager()

    def __str__(self):
        return self.area_of_health + ' | ' + self.supplement_type

#Below is a model representing the capture of API responses from the Nutritionix API, storing user search query and Nutrition Info
class NutritionixInfoReceived(models.Model):
    calories = models.FloatField()
    total_Fat = models.FloatField()
    saturated_fat = models.FloatField()
    cholesterol = models.FloatField()
    sodium = models.FloatField()
    total_carbohydrate = models.FloatField()
    dietary_fiber = models.FloatField()
    sugars = models.FloatField()
    protein = models.FloatField()
    potassium = models.FloatField()
    search_query = models.CharField(max_length=250)

    Queries = models.Manager()

    def __str__(self):
        return self.search_query