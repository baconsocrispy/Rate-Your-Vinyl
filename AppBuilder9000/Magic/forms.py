from django.forms import ModelForm
from django import forms
from .models import Deck


class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = '__all__'
