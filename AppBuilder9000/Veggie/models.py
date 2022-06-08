from django.db import models


class Recipe(models.Model):
    title_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    number_of_ingredients = models.IntegerField()
    making_time = models.IntegerField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title_name
