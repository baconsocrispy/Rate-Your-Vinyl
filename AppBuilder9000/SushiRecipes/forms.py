from django.forms import ModelForm

from .models import SushiRecipes


class SushiForm(ModelForm):
    class Meta:
        model = SushiRecipes
        exclude = ["notes"]
