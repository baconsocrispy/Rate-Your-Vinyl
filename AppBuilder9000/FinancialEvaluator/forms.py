from django.forms import ModelForm
from django import forms
from .models import Evaluation


class EvaluationForm(ModelForm):
    class Meta:
        model = Evaluation
        fields = ['symbol', 'style']
