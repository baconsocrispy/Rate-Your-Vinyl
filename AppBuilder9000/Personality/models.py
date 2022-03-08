from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=2)
    sex = models.BooleanField()
    o_average_score = models.FloatField(max_length=5)
    c_average_score = models.FloatField(max_length=5)
    e_average_score = models.FloatField(max_length=5)
    a_average_score = models.FloatField(max_length=5)
    n_average_score = models.FloatField(max_length=5)
    o_percentile = models.IntegerField(max_length=2)
    c_percentile = models.IntegerField(max_length=2)
    e_percentile = models.IntegerField(max_length=2)
    a_percentile = models.IntegerField(max_length=2)
    n_percentile = models.IntegerField(max_length=2)

    def __str__(self):
        return self.name
