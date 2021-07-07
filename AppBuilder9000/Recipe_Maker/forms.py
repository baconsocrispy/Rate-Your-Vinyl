from django.forms import ModelForm
from .models import Recipe, Ingredients, Instructions


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        # instead of writing out all the fields from the model, use '__all__'
        # grabs all the fields from within Recipe
        # passes it into the form
        fields = '__all__'


class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'


class Instructions(ModelForm):
    class Meta:
        model = Instructions
        fields = '__all__'





"""
 old code to experiment with later

# instead of grabbing a class from model.py, its grabbing from admin.py
# class RecipeAdmin has models Ingredients and Instructions inline
from .admin import RecipeAdmin


class RecipeForm(ModelForm):
    class Meta:
        model = RecipeAdmin
        # instead of writing out all the fields from the model, use '__all__'
        # grabs all the fields from within RecipeAdmin
        # passes it into the form
        fields = '__all__'
"""