from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

zone_type = [('1a', '1a'), ('1b', '1b'), ('2a', '2a'), ('2b', '2b'), ('3a', '3a'), ('3b', '3b'), ('4a', '4a'),
             ('4b', '4b'), ('5a', '5a'), ('5b', '5b'), ('6a', '6a'), ('6b', '6b'), ('7a', '7a'), ('7b', '7b'),
             ('8a', '8b'),
             ('9a', '9b'), ('9a', '9b'), ('10a', '10a'), ('10b', '10b'), ('11a', '11a'), ('11b', '11b'),
             ('12a', '12a'), ('12b', '12b'), ('13a', '13a'), ('13b', '13b'),
             ]


class Planner(models.Model):
    Growing_Year = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    Growing_Zone = models.CharField(max_length=30, blank=True)
    Vegetable_Name = models.CharField(max_length=30, default='', blank=True, null=False)
    Sowing_Time_Frame = models.CharField(max_length=30, default='', blank=True, null=False)
    Harvest_Notes = models.TextField(max_length=300, default='', blank=True, null=True)
    General_Care_Notes = models.TextField(max_length=500, default='', blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = "Garden Planner"

    def __str__(self):
        return self.Growing_Zone


class Eval(models.Model):
    Planner = models.ForeignKey(Planner, on_delete=models.CASCADE)
    Growing_Season_Observations = models.TextField(max_length=500, default='', blank=True, null=True)
    Harvest_Weight = models.TextField(max_length=300, blank=True)
    Harvest_Observations = models.TextField(max_length=500, default='', blank=True, null=True)

