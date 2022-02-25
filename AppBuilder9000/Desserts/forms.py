from django.forms import ModelForm
from .models import Recipe


# define RecipeForm
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
