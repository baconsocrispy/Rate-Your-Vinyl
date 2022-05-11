from django .forms import ModelForm
from .models import ResortListings
from django import forms


class ResortListings(ModelForm):
    class Meta:
        model = ResortListings
        fields = '__all__'