from django.forms import ModelForm
from .models import Recipe
from django import forms


# define RecipeForm
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


CATEGORY_OPTIONS = (
        ('Indian High Tea Recipe', 'Indian High Tea Recipe'),
        ('Indian Comfort Food Recipe', 'Indian Comfort Food Recipe'),
        ('Indian Street Food Recipe', 'Indian Street Food Recipe'),
        ('Indian Chicken Recipe', 'Indian Chicken Recipe'),
        ('Beverages Recipe', 'Beverages Recipe'),
    )


class SearchForm(forms.Form):
    category_type = forms.ChoiceField(choices=CATEGORY_OPTIONS)
