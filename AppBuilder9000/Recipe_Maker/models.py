from django.db import models

# Dictionary
TYPE_CHOICES = {
    ("Appetizers", "Appetizers"),
    ("Entrees", "Entrees"),
    ("Drinks", "Drinks"),
    ("Snacks", "Snacks"),
}


# When a recipe is created these are the fields of info that are filled out
class RecipeName(models.Model):
    recipe_type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    # blank=False does not allow for the forms on the webpage to be left blank
    # null=False does not allow for the it to be blank in the database
    recipe_name = models.CharField(max_length=100, default="", blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.recipe_name


class Ingredients(models.Model):
    recipe = models.ForeignKey(RecipeName, on_delete=models.CASCADE)
    recipe_ingredients = models.CharField(max_length=100, default="", blank=True)

    def __str__(self):
        return self.recipe_ingredients


class Description(models.Model):
    recipe = models.ForeignKey(RecipeName, on_delete=models.CASCADE)
    recipe_description = models.TextField()

    def __str__(self):
        return self.recipe_description
