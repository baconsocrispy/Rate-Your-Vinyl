from django.forms import ModelForm
from .models import Jobs
from django import forms

class JobsForm(ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'