from django.forms import ModelForm
from django import forms
from .models import Activities


class ActivitiesForm(ModelForm):
    class Meta:
        model = Activities
        fields = '__all__'
