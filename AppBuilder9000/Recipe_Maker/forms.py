from django.forms import ModelForm
# instead of grabbing a class from model.py, its grabbing from admin.py
# class RecipeAdmin has models Ingredients and Descriptions inline
from .admin import RecipeAdmin


class RecipeForm(ModelForm):
    class Meta:
        model = RecipeAdmin
        # instead of writing out all the fields from the model, use '__all__'
        # grabs all the fields from within RecipeAdmin
        # passes it into the form
        fields = '__all__'