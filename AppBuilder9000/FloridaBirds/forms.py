from django import forms
from django.forms import ModelForm
from .models import BirdDescription


class BirdDescriptionForm(ModelForm):
    class Meta:
        model = BirdDescription
        fields = '__all__'