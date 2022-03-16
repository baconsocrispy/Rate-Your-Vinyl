from django import forms
from .models import ChefKnives


class KnifeForm(forms.ModelForm):
    class Meta:
        model = ChefKnives
        fields = '__all__'
