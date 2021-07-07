from django.db import models

# Dictionary
TYPE_CHOICES = {
    ("Appetizers", "Appetizers"),
    ("Entrees", "Entrees"),
    ("Drinks", "Drinks"),
    ("Snacks", "Snacks"),
}


# When a recipe is created these are the fields of info that are filled out
class Recipe(models.Model):
    recipe_type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    # blank=False does not allow for the forms on the webpage to be left blank
    # null=False does not allow for the it to be blank in the database
    recipe_name = models.CharField(max_length=100, default="", blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.recipe_name


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_ingredients = models.TextField(default="Please write you're ingredients and amounts", blank=False)

    def __str__(self):
        return self.recipe_ingredients


class Instructions(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_instructions = models.Textfield(default='Please write your instructions here', blank=False)

    def __str__(self):
        return self.recipe_instructions
