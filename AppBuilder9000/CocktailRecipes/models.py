from django.db import models


class Cocktail(models.Model):
    cocktail_name = models.CharField(max_length=50, unique=True)
    ingredient_1 = models.CharField(max_length=50)
    quantity_1 = models.DecimalField(max_digits=3, decimal_places=1)
    unit_1 = models.CharField(max_length=15)
    ingredient_2 = models.CharField(max_length=50, blank=True)
    quantity_2 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    unit_2 = models.CharField(max_length=15, blank=True)
    ingredient_3 = models.CharField(max_length=50, blank=True)
    quantity_3 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    unit_3 = models.CharField(max_length=15, blank=True)
    ingredient_4 = models.CharField(max_length=50, blank=True)
    quantity_4 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    unit_4 = models.CharField(max_length=15, blank=True)
    ingredient_5 = models.CharField(max_length=50, blank=True)
    quantity_5 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    unit_5 = models.CharField(max_length=15, blank=True)
    ingredient_6 = models.CharField(max_length=50, blank=True)
    quantity_6 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    unit_6 = models.CharField(max_length=15, blank=True)
    ingredient_7 = models.CharField(max_length=50, blank=True)
    quantity_7 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    unit_7 = models.CharField(max_length=15, blank=True)
    ingredient_8 = models.CharField(max_length=50, blank=True)
    quantity_8 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    unit_8 = models.CharField(max_length=15, blank=True)
    ingredient_9 = models.CharField(max_length=50, blank=True)
    quantity_9 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    unit_9 = models.CharField(max_length=15, blank=True)
    ingredient_10 = models.CharField(max_length=50, blank=True)
    quantity_10 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    unit_10 = models.CharField(max_length=15, blank=True)
    directions = models.TextField()
    avg_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    # photo = models.FileField(upload_to='static/CocktailRecipes/user_images', blank=True)

    Cocktails = models.Manager()

    def __str__(self):
        return str(self.cocktail_name)


rating_choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]


class Review(models.Model):
    user_name = models.CharField(max_length=50)
    rating = models.PositiveSmallIntegerField()
    comments = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)

    Reviews = models.Manager()
