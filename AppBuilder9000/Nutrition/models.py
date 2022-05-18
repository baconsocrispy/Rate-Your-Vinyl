from django.db import models
from datetime import date

Gender_options = {
    ('Male', 'Male'),
    ('Female', 'Female'),
}

class User(models.Model):
    Username = models.CharField(max_length = 40)
    Password = models.CharField(max_length = 40)
    Age = models.IntegerField(default='')
    Gender = models.CharField(default='', max_length=40, choices=Gender_options)
    Height = models.IntegerField(default='')
    Weight = models.IntegerField(default = '')
    BMI = models.FloatField()
    FatPercent = models.FloatField()
    Phase = models.CharField(max_length=40)
    Calories = models.IntegerField(default='')
    Protein = models.IntegerField(default='')

    def get_BMI(self):
        User.BMI = (User.Weight * 703)/(User.Height**2)

    def get_FatPercent(self):
        if User.Gender == 'Male':
            User.FatPercent = (User.BMI * 1.39) + (User.Age * 0.16) - 19.34
        else:
            User.FatPercent = (User.BMI * 1.39) + (User.Age * 0.16) - 9

    def get_Phase(self):
        if User.BMI >= 25:
            User.Phase = 'Fat Burning'
        elif User.BMI < 25 & User.FatPercent > 15 & User.Gender == 'Male':
            User.Phase = 'Shredding'
        elif User.BMI < 25 & User.FatPercent > 20 & User.Gender == 'Female':
            User.Phase = 'Shredding'
        elif User.BMI < 25 & User.FatPercent <= 15 & User.Gender == 'Male':
            User.Phase = 'Bulking'
        elif User.BMI < 25 & User.FatPercent <= 20 & User.Gender == 'Female':
            User.Phase = 'Bulking'

    def get_Nutrition(self):
        if User.Phase == 'Fat Burning' & User.Weight >= 220:
            User.Calories = 2400
            User.Protein = 180
        elif User.Phase == 'Fat Burning' & User.Weight < 220 & User.Weight >= 200:
            User.Calories = 2200
            User.Protein = 165
        elif User.Phase == 'Fat Burning' & User.Weight < 200 & User.Weight >= 180:
            User.Calories = 2000
            User.Protein = 150
        elif User.Phase == 'Fat Burning' & User.Weight < 180 & User.Weight >= 160:
            User.Calories = 1800
            User.Protein = 135
        elif User.Phase == 'Fat Burning' & User.Weight < 160:
            User.Calories = 1600
            User.Protein = 120
        elif User.Phase == 'Shredding':
            User.Calories = User.Weight * 12
            User.Protein = User.Weight * 0.8
        elif User.Phase == 'Bulking':
            User.Calories = User.Weight * 15
            User.Protein = User.Weight

    Users = models.Manager()

    def __str__(self):
        return self.Username

class ChooseUser(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)