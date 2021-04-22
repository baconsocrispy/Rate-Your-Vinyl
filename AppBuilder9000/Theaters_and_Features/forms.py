from django.forms import ModelForm
from django import forms
from .models import Theaters


class TheaterForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Theaters
        fields = '__all__'
