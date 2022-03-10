from django.db import models

# This is the basic model for the database.#


class Recipes(models.Model):
    recipe_name = models.CharField(default='Enter recipe name', max_length=40)
    recipe_description = models.TextField(default='Enter a brief description')
    grandma_story = models.TextField(default='Remember a time you made this with Grandma! ')
    cook_time = models.IntegerField(default='60')
    ingredients = models.TextField(default='list, ingredients, separated, by, commas')
    instructions = models.TextField(default='1.\n\n2.\n\n3.')
    Recipe = models.Manager()

    def __str__(self):
        return self.recipe_name
