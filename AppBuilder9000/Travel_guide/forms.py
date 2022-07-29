from django.forms import ModelForm
from django import forms
from .models import Destination


class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = ['Country', 'Region']