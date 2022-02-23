from django.db import models


class Recipes(models.Model):
    recipe_name = models.CharField(max_length=30)
    cook_time = models.IntegerField(default='')
    instructions = models.TextField()
    Recipe = models.Manager()

    def __str__(self):
        return self.recipe_name
